window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true
  },
  options: { skipHtmlTags: ['script','noscript','style','textarea','pre','code'] }
};

// navigation.instant swaps page content via XHR without a full reload, so MathJax must be
// re-run after every navigation (document$ fires on both instant and full page loads).
// Clearing the previous render state first avoids a race with MathJax's own typeset pass
// that otherwise sometimes leaves the first render of an equation blank.
document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
