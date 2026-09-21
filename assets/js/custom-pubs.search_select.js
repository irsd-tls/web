// https://codepen.io/desandro/pen/pOjMdx
// https://codepen.io/desandro/pen/WyOZjx
// https://codepen.io/MrDC/pen/JzWZXJ

// quick search regex
var qsRegex;
var filterSelector = "*";

// init Isotope
var iso = new Isotope(".grid", {
  itemSelector: ".element-item",
  layoutMode: "vertical",
  filter: function(itemElem) {
    var search = qsRegex ? itemElem.textContent.match(qsRegex) : true;      
    var filterRes = filterSelector != '*' ? itemElem.getAttribute("data-filter") == filterSelector : true;
    return search && filterRes;
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

var filtersElem = document.querySelector('.filters-select');
filtersElem.addEventListener( 'change', function( event ) {
  var filterValue = event.target.value;
  console.log(filterValue);
  filterSelector = filterValue;
  iso.arrange();
});

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

