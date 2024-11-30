/*
 * Initializes the zone map modal on the contact us page.
 */
document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById("zoneMapModal");
    var link = document.querySelector(".zone-map-link");
    var span = document.getElementsByClassName("close")[0];

    link.onclick = function (e) {
      e.preventDefault();
      modal.style.display = "block";
    };

    span.onclick = function () {
      modal.style.display = "none";
    };

    window.onclick = function (event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    };
  });
