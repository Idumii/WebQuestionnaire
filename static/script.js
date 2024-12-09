// Basculer le mode jour/nuit
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

// Sauvegarder la préférence dans le localStorage
function savePreference() {
    const isDarkMode = document.body.classList.contains("dark-mode");
    localStorage.setItem("darkMode", isDarkMode ? "enabled" : "disabled");
}

// Charger la préférence au démarrage
window.onload = () => {
    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
    }
}
