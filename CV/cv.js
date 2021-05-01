




function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function darkMode() {
  var element = document.body;

  element.classList.toggle("dark-mode");
}
