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
document$.subscribe(() => {
  MathJax.typesetPromise();
});
