// https://codepen.io/desandro/pen/pOjMdx
// https://codepen.io/desandro/pen/WyOZjx
// https://codepen.io/MrDC/pen/JzWZXJ

// quick search regex
var qsRegex;

// init Isotope
var iso = new Isotope(".grid", {
  itemSelector: ".people-item",
  layoutMode: 'fitRows',
  filter: function(itemElem) {
    var search = qsRegex ? itemElem.textContent.match(qsRegex) : true;      
    return search;
  }
});

// use value of search field to filter
var quicksearch = document.querySelector(".quicksearch");
if (quicksearch) {
  quicksearch.addEventListener(
    "keyup",
    debounce(function() {
      qsRegex = new RegExp(quicksearch.value, "gi");
      iso.arrange();
    }, 300)
  );
}

function debounce(fn, threshold) {
  var timeout;
  threshold = threshold || 100;
  return function debounced() {
    clearTimeout(timeout);
    var args = arguments;
    var _this = this;

    function delayed() {
      fn.apply(_this, args);
    }
    timeout = setTimeout(delayed, threshold);
  };
}
