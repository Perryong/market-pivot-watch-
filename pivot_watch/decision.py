"""Explain existing strategy state; never place orders or create new breakout events."""
def decide(report):
    def result(decision, action, reason):
        return {'decision':decision, 'action':action, 'reason':reason}
    wait = lambda reason: result('WAIT', 'WAIT FOR CONFIRMATION', reason)
    if report.get('error'):
        return result('WAIT', 'WAIT FOR VERIFIED DATA', 'The completed candle cannot be verified. No trade decision is available.')
    if report.get('demo'):
        return result('WAIT', 'DEMO ONLY — DO NOT TRADE', 'These are synthetic examples, not current market observations.')
    if report.get('baseline'):
        return wait('The watch has just established its baseline. Existing price direction is not a newly confirmed entry.')
    events = [event for event in report.get('events', [])
              if not event.get('historical', True) and event['close_time'] == report['close_time']]
    exits = [event for event in events if event['type'] in ('EXIT_LONG', 'EXIT_SHORT')]
    if exits:
        long = exits[-1]['type'] == 'EXIT_LONG'
        return result('SELL / EXIT LONG' if long else 'BUY / EXIT SHORT',
                      'EXIT RULE TRIGGERED — IF YOU HOLD THIS POSITION',
                      'The latest completed 4H close invalidated the tracked setup. This applies to an existing long, not a new short.' if long else
                      'The latest completed 4H close invalidated the tracked setup. This applies to an existing short, not a new long.')
    setup = report.get('setup')
    if not setup:
        return wait('No tracked setup is active. Wait for a new completed 4H pivot crossing, then a later completed retest.')
    side = setup['side']
    pivot = report['upper'] if side == 'BUY' else report['lower']
    fresh_retest = any(event['type'] == 'RETEST_CONFIRMED' for event in events)
    quote = report['quote']['price']
    correct_side = quote > pivot if side == 'BUY' else quote < pivot
    if fresh_retest and correct_side:
        return result(side, 'ENTRY SETUP CONFIRMED — DO NOT CHASE',
                      f'A later completed 4H candle confirmed the {"hold above" if side == "BUY" else "rejection below"} {pivot:,.2f}. '
                      'The quote at this check remains on the breakout side. Entry eligibility is conditional on execution near the retest level; this is not a market-order instruction or a guaranteed fill.')
    if fresh_retest:
        return wait('The completed retest was confirmed, but the quote at this check has crossed back through the pivot. Wait; entry conditions are no longer aligned.')
    if setup.get('retest_close_time'):
        return result('WAIT', 'REVIEW EXISTING SETUP — NO NEW ENTRY',
                      'The retest was confirmed in an earlier check. Do not repeat the entry; manage any existing position using the invalidation level.')
    return wait(f'The {side} breakout is tracked, but a later completed 4H retest has not confirmed entry. Ignore active-candle touches.')
