// https://codepen.io/desandro/pen/pOjMdx
// https://codepen.io/desandro/pen/WyOZjx
// https://codepen.io/MrDC/pen/JzWZXJ

// trying pagination
const itemsPerPage = 25;
let currentPage = 1;
const items = document.querySelectorAll('.element-item');
const totalItems = items.length;
const totalPages = Math.ceil(totalItems / itemsPerPage);

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

      // Get the filtered items from Isotope
      const visibleItems = iso.getFilteredItemElements();

      // Reset to page 1 and update pagination
      currentPage = 1;
      setupPagination(visibleItems);
      showPage(currentPage, visibleItems);

    }, 300)
  );
}

var filtersElem = document.querySelector('.filters-select');
filtersElem.addEventListener( 'change', function( event ) {
  var filterValue = event.target.value;
  console.log(filterValue);
  filterSelector = filterValue;
  iso.arrange();

  // Get the filtered items from Isotope
  const visibleItems = iso.getFilteredItemElements();

  // Reset to page 1 and update pagination
  currentPage = 1;
  setupPagination(visibleItems);
  showPage(currentPage, visibleItems);

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

function showPage(page, filteredItems) {
  const startIndex = (page - 1) * itemsPerPage;
  const endIndex = Math.min(startIndex + itemsPerPage, filteredItems.length);

  // Hide all items first
  items.forEach(item => {
    item.style.display = 'none';
  });

  // Show only the filtered items for the current page
  filteredItems.forEach((item, index) => {
    if (index >= startIndex && index < endIndex) {
      item.style.display = 'block';
    }
  });

  // mark current page button?
  const pagbts = document.querySelectorAll("#pagination button");
  pagbts.forEach((item, index) => {
    if (index == currentPage - 1) {
      item.classList.add('currentpage');
    } else {
      item.classList.remove('currentpage');
    }
  });
  
  iso.layout(); // Re-layout Isotope
}

function setupPagination(filteredItems) {
  const paginationContainer = document.querySelector('#pagination');
  paginationContainer.innerHTML = '';

  const totalPages = Math.ceil(filteredItems.length / itemsPerPage);

  for (let i = 1; i <= totalPages; i++) {
    const button = document.createElement('button');
    button.textContent = i;
    button.addEventListener('click', () => {
      currentPage = i;
      showPage(currentPage, filteredItems);
    });
    paginationContainer.appendChild(button);
  }
}

// init pages
setupPagination(items);
showPage(currentPage, items);
