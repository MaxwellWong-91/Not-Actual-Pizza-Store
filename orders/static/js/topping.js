document.addEventListener("DOMContentLoaded", () => {
    var toppingInput = document.querySelectorAll("input[type = checkbox]");

    const maxTopping = 3;

    for (var i = 0; i < toppingInput.length; i++) {
        toppingInput[i].addEventListener("click", () => {
            if (document.querySelectorAll("input[type = checkbox]:checked").length > maxTopping) {
                event.target.checked = false;
            }
        })
    }
})