// Team Acranauts: May and Anjini 


//retrieve node in Dom via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
//aka creates the canvas 
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

//toggle = switch | button that switches rectangle and circle 
var toggleMode = function(e) {
    var rectcirc = document.getElementById("buttonToggle");
    rectcirc.addEventListener('click', toggleMode);

    var toggleMode = (e) => {
        console.log("toggling...");
        if(mode == "rect") {
            mode = "circle"
            console.log("circle");

        }
        else {
            mode = "rect"
            console.log("rect");

        }
    }
}
