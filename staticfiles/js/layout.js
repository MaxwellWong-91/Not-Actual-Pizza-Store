document.addEventListener("DOMContentLoaded", () => {

    var navTabs = document.querySelectorAll(".nav-link");
    // adds click listeners to the menu tabs at top
    for (var i = 0; i < navTabs.length; i++) {
        navTabs[i].addEventListener("click", () => {
            setActive(event);
        })
    }
})

// sets new button to be active
function setActive(event) {
    var prev = document.querySelector(".active");

    prev.className = prev.className.replace(" active", "");

    event.target.className += " active";

}