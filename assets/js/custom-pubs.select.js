// https://codepen.io/desandro/pen/pOjMdx
// https://codepen.io/desandro/pen/WyOZjx

// init Isotope
var iso = new Isotope( '.grid', {
  itemSelector: '.element-item'
});

var filtersElem = document.querySelector('.filters-select');
filtersElem.addEventListener( 'change', function( event ) {
  var filterValue = event.target.value;
  // console.log(filterValue);
  iso.arrange({ filter: filterValue });
});


