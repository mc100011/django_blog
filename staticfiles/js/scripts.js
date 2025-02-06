document.addEventListener("DOMContentLoaded", function() {
    let alertBox = document.querySelector(".alert");
    if (alertBox) {
        setTimeout(function() {
            alertBox.style.display = "none";
        }, 5000);  // Cache l'alerte après 5 secondes
    }
});
document.addEventListener("DOMContentLoaded", function() {
    let alertBox = document.querySelector(".alert");
    if (alertBox) {
        setTimeout(function() {
            alertBox.style.display = "none";
        }, 5000);
    }

    // Effet d’apparition des cartes
    let cards = document.querySelectorAll(".card");
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 200);
    });
});
