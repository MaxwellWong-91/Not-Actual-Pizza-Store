document.addEventListener("DOMContentLoaded", () => {
    var button = document.querySelectorAll(".button");

    var CSRF_TOKEN = getCookie('csrftoken');

    for (var i = 0; i < button.length; i++) {
        button[i].addEventListener("click", () => {
            event.preventDefault();
            // get the button we clicked
            var currButton = event.currentTarget;

            // get the form to access input
            var currForm = currButton.form;
            var id = currForm.elements.id.value;
            var type = currForm.elements.type.value;
            
            const request = new XMLHttpRequest();
            
            request.open('POST', "/cancel");
            

            request.onload = () => {
                // remove the element from screen
                currButton.parentElement.parentElement.style.animationPlayState = 'running';
                currButton.parentElement.parentElement.addEventListener('animationend', () =>  {
                    currButton.parentElement.parentElement.remove();
                });

                // get new price
                const data = JSON.parse(request.responseText);

                // update price total
                document.querySelector("#total").innerHTML = "$" + data.price;

                // get rid of button if price is gone/ no more items
                if (data.price === 0) {
                    document.querySelector("#purchaseButton").remove();
                }
            }

            // send the deleted item to backend
            const data = new FormData();
            
            // send id and type 
            data.append("id", id);
            data.append('type', type);
            
            request.setRequestHeader('X-CSRFToken', CSRF_TOKEN);
            request.send(data);
        })
    }

})

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}