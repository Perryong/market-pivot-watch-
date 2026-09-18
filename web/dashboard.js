/* Actual TradingView widgets; no simulated chart or private layout injection. */
'use strict';
const tabs = Array.from(document.querySelectorAll('.market-tab'));
const panels = Array.from(document.querySelectorAll('.market-panel'));
function expireReports(now = Date.now()) {
  panels.forEach(panel => {
    const age = now / 1000 - Number(panel.dataset.checked);
    const stale = !Number.isFinite(age) || age > 21600 || age < -300;
    panel.querySelector('.stale-notice').hidden = !stale;
    panel.querySelector('.signal').hidden = stale;
    panel.querySelector('.decision-panel').hidden = stale;
    const code = panel.querySelector('.pine-code');
    if (code) {
      const presetAge = now / 1000 - Number(code.dataset.checked);
      code.hidden = !Number.isFinite(presetAge) || presetAge < -300;
      code.querySelector('.pine-age-warning').hidden = presetAge <= 21600;
    }
  });
}
function loadChart(panel) {
  const chart = panel.querySelector('.chart');
  if (chart.dataset.loaded) return;
  chart.dataset.loaded = 'true';
  const container = document.createElement('div');
  container.className = 'tradingview-widget-container';
  const inner = document.createElement('div');
  inner.className = 'tradingview-widget-container__widget';
  container.appendChild(inner);
  const copyright = document.createElement('div');
  copyright.className = 'tradingview-widget-copyright';
  const attribution = document.createElement('a');
  attribution.href = 'https://www.tradingview.com/';
  attribution.target = '_blank';
  attribution.rel = 'noopener noreferrer';
  attribution.textContent = 'Track all markets on TradingView';
  copyright.appendChild(attribution);
  container.appendChild(copyright);
  const script = document.createElement('script');
  script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js';
  script.async = true;
  script.textContent = JSON.stringify({autosize:true, symbol:panel.dataset.symbol,
    interval:'240', timezone:'Asia/Singapore', theme:'dark', style:'1', locale:'en',
    allow_symbol_change:false, calendar:false, support_host:'https://www.tradingview.com'});
  script.onerror = () => { chart.textContent = 'TradingView could not load. Open the chart using the link below.'; };
  container.appendChild(script);
  chart.replaceChildren(container);
}
function selectMarket(tab) {
  tabs.forEach(t => {
    t.setAttribute('aria-selected', String(t === tab));
    t.tabIndex = t === tab ? 0 : -1;
  });
  panels.forEach(p => { p.hidden = p.id !== tab.getAttribute('aria-controls'); });
  const panel = document.getElementById(tab.getAttribute('aria-controls'));
  loadChart(panel);
  expireReports();
}
tabs.forEach((tab, i) => {
  tab.addEventListener('click', () => selectMarket(tab));
  tab.addEventListener('keydown', event => {
    let next;
    if (event.key === 'ArrowRight') next = (i+1) % tabs.length;
    else if (event.key === 'ArrowLeft') next = (i+tabs.length-1) % tabs.length;
    else if (event.key === 'Home') next = 0;
    else if (event.key === 'End') next = tabs.length-1;
    else return;
    event.preventDefault(); tabs[next].focus(); selectMarket(tabs[next]);
  });
});
document.querySelectorAll('.copy-pine').forEach(button => {
  button.addEventListener('click', async () => {
    expireReports();
    if (button.closest('.pine-code').hidden) return;
    const code = document.getElementById(button.getAttribute('aria-controls'));
    const status = button.parentElement.querySelector('.copy-status');
    try {
      await navigator.clipboard.writeText(code.textContent);
      status.textContent = 'Copied.';
    } catch {
      const range = document.createRange();
      range.selectNodeContents(code);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = 'Code selected. Press Ctrl+C or ⌘C to copy.';
    }
  });
});
if (tabs.length) selectMarket(tabs[0]);
setInterval(expireReports, 60000);
