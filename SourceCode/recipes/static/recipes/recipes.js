$("ingredients_input").keyup(function(event) {
    if (event.which == 13) {
        alert("Enter was pressed");
     }
});

var ingr_list  = [];
var ingr_input  = document.getElementById("ingredients_input");
var recipes_result  = document.getElementById("display");


function insert () {
    ingr_list.push(ingr_input.value);
    clearAndShow();
}

function clearAndShow () {
    ingr_input.value = "";
    recipes_result.innerHTML = "";
    recipes_result.innerHTML += "Ingredient searched: " + "<br>" +
        ingr_list.join(", ") + "<br/>" + 
        "<hr style='width:50%;'>" +"Results:";
}

