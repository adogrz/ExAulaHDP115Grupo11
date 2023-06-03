console.log("El archivo main.js se ha cargado correctamente.");

document.addEventListener("DOMContentLoaded", function() {
  // Función para verificar el zoom
  function checkZoom() {
    var zoomLevel = Math.round(window.devicePixelRatio * 100);
    var carouselItems = document.querySelectorAll(".carousel-item");
    var carousel = document.querySelector("div.carousel.slide");
    var heading = document.querySelector("h1.mt-4");

    // Restablecer clases de zoom
    carouselItems.forEach(function(item) {
      item.classList.remove("zoomed-in", "zoomed-out");
    });

    // Aplicar clases de zoom según el nivel
    if (zoomLevel >= 100) {
      carouselItems.forEach(function(item) {
        item.classList.add("zoomed-in");
      });
      carousel.classList.add("zoomed-in");
      heading.classList.add("zoomed-in-heading");
    } else if (zoomLevel < 100) {
      carouselItems.forEach(function(item) {
        item.classList.add("zoomed-out");
      });
      carousel.classList.add("zoomed-out");
      heading.classList.add("zoomed-out-heading");
    }
  }

  // Verificar el zoom al cargar la página
  checkZoom();

  // Verificar el zoom al cambiar el tamaño de la ventana
  window.addEventListener("resize", checkZoom);
});
