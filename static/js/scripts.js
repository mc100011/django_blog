document.addEventListener("DOMContentLoaded", function() {
    // Gestion des alertes
    let alertBox = document.querySelector(".alert");
    if (alertBox) {
        setTimeout(function() {
            alertBox.style.display = "none";
        }, 5000); // Cache l'alerte après 5 secondes
    }

    // Effet d’apparition des cartes
    document.querySelectorAll(".card").forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 200);
    });

    // Gestion des images cliquables avec lightbox
    document.querySelectorAll(".ckeditor-content img").forEach(img => {
        img.classList.add("zoomable");
        img.addEventListener("click", function() {
            let lightbox = document.createElement("div");
            lightbox.className = "lightbox";
            lightbox.style.cssText = "position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.8); display: flex; align-items: center; justify-content: center; z-index: 1000;";
            let imgElement = document.createElement("img");
            imgElement.src = this.src;
            imgElement.style.cssText = "max-width: 90%; max-height: 90%;";
            lightbox.appendChild(imgElement);

            document.body.appendChild(lightbox);

            lightbox.addEventListener("click", function() {
                document.body.removeChild(lightbox);
            });
        });
    });

    // Mode sombre si préféré par le système
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.classList.add("dark-mode");
    }
