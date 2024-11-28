window.addEventListener("scroll", () => {
    const backToTopButton = document.getElementById("backToTop");
    if (window.scrollY > 100) {
        backToTopButton.classList.add("show");
    } else {
        backToTopButton.classList.remove("show");
    }
});

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: "smooth" });
}


