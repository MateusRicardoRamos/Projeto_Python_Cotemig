(function () {
    const savedTheme = localStorage.getItem("taskflow-theme");
    const root = document.documentElement;

    if (savedTheme === "dark" || savedTheme === "light") {
        root.setAttribute("data-bs-theme", savedTheme);
    }

    function updateThemeButton() {
        const button = document.getElementById("themeToggle");
        if (!button) return;

        const isDark = root.getAttribute("data-bs-theme") === "dark";
        button.innerHTML = isDark
            ? '<i class="bi bi-sun-fill"></i>'
            : '<i class="bi bi-moon-stars-fill"></i>';
        button.title = isDark ? "Ativar modo claro" : "Ativar modo escuro";
    }

    const themeButton = document.getElementById("themeToggle");

    if (themeButton) {
        themeButton.addEventListener("click", function () {
            const current = root.getAttribute("data-bs-theme") || "light";
            const next = current === "dark" ? "light" : "dark";

            root.setAttribute("data-bs-theme", next);
            localStorage.setItem("taskflow-theme", next);
            updateThemeButton();
        });

        updateThemeButton();
    }

    async function carregarFrase() {
        const target = document.getElementById("fraseMotivacional");
        if (!target) return;

        target.textContent = "Carregando...";

        try {
            const response = await fetch("/api/frase");
            const data = await response.json();
            target.textContent = "“" + data.frase + "”";
        } catch (error) {
            target.textContent =
                "“Continue aprendendo: pequenos passos constroem grandes resultados.”";
        }
    }

    const quoteButton = document.getElementById("novaFrase");
    if (quoteButton) {
        quoteButton.addEventListener("click", carregarFrase);
        carregarFrase();
    }
})();
