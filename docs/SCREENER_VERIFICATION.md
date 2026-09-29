# Screener verification — 2026-09-29

- 19 new screener tests pass.
- Full suite: 147 tests; 7 failures and 5 errors, all reproduced on untouched starting commit c618c99 (128 baseline tests). No additional failing tests.
- Python compileall and git diff --check pass.
- Browser: synthetic dashboard rendered; symbol filtering and evidence disclosure verified. Overlapping chart labels corrected.
- Live public Binance BTCUSDT and ETHUSDT scan passed using the system CA bundle (`SSL_CERT_FILE=/etc/ssl/cert.pem`); both returned WATCHING, no paper trades.
- Export and replay of the recorded BTC bundle completed; unknown costs correctly prevent paper entries.
- Live stock smoke check reported DATA_UNAVAILABLE because Alpaca credentials are absent. Alpaca aggregation, pagination, DST and early-close behavior are covered with controlled API fixtures, not a live entitlement check.
- No broker orders, Telegram messages, server deployment or cron installation performed.
- Independent review findings fixed: frozen evidence revisions; final stock half-hour; missing execution/replay history; monitoring removed symbols; long-outage unscorable paper accounting.

## Existing baseline failures

- `ERROR: test_app_hourly_failure_and_recovery_preserve_baseline (test_hourly.HourlyTests.test_app_hourly_failure_and_recovery_preserve_baseline)`
- `ERROR: test_auto_range_locks_and_excludes_latest (test_core.EngineTests.test_auto_range_locks_and_excludes_latest)`
- `ERROR: test_btcusdt_automatic_range_rebaselines_old_fixed_levels_without_signal (test_app.AppTests.test_btcusdt_automatic_range_rebaselines_old_fixed_levels_without_signal)`
- `ERROR: test_demo_cli_writes_report_pine_and_preserves_signal_dedup (test_app.AppTests.test_demo_cli_writes_report_pine_and_preserves_signal_dedup)`
- `ERROR: test_fresh_reports_offer_pine_and_escape_provider_text (test_site.SiteTests.test_fresh_reports_offer_pine_and_escape_provider_text)`
- `FAIL: test_demo_does_not_offer_tradeable_pine (test_site.SiteTests.test_demo_does_not_offer_tradeable_pine)`
- `FAIL: test_failed_render_never_sends_or_records_receipt_and_is_shared (test_telegram.TelegramTests.test_failed_render_never_sends_or_records_receipt_and_is_shared)`
- `FAIL: test_gap_does_not_produce_cross (test_core.EngineTests.test_gap_does_not_produce_cross)`
- `FAIL: test_hourly_caption_keeps_core_and_drops_wording (test_telegram.TelegramTests.test_hourly_caption_keeps_core_and_drops_wording)`
- `FAIL: test_market_order_and_independent_eth_baselines (test_app.AppTests.test_market_order_and_independent_eth_baselines)`
- `FAIL: test_photo_and_failure_message_with_receipts_prevent_repeat_send (test_telegram.TelegramTests.test_photo_and_failure_message_with_receipts_prevent_repeat_send)`
- `FAIL: test_target_touch_before_confirmation_blocks_later_retest (test_shadow.ShadowTests.test_target_touch_before_confirmation_blocks_later_retest)`
