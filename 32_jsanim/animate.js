//access canvas and bttons via DOM (update HTML source to align)
var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");
// ------
var radius = 100;
var radius_inc = 1;
var growing = true;
var drawCircle = () => {
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.arc(c.width/2,c.height/2,radius,0,2 * Math.PI);
    ctx.stroke()
    ctx.fill()
 }


var drawDot = (e) => {
    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
    clear();
    drawCircle();
    if (growing) {
        if (radius > c.width / 2) { //if too big
            growing = false;
        }
        radius += radius_inc;
    } 
    else {
        radius -= radius_inc;
        if (radius == 0) {  //other side when growing is set to false
            growing = true
        }
    }
};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame( requestID );

    //demensions of the image itself
    var rectWidth = 400;
    var rectHeight = 600;

    //
    var rectX = Math.random() * 100;
    var rectY = Math.random() * 100;

    // var xvel = ;
    // var yvel = ;
}


var clear = (e) => {
    e.preventDefault(); // Q: what dis? 
    ctx.clearRect(0,0,c.width,c.height);
};




var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click",drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click",stopIt);
