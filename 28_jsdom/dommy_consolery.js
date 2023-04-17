/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Acronauts :: Anjini and May
// SoftDev pd07
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-17m
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  // will add a string to the end "thelist"
  var list = document.getElementById("thelist");
  // access "thelist" created in the html file
  var newitem = document.createElement("li");
  //adds a new bullet point to add the string to 
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  //removes an item from "thelist" using the index
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  // items is a varable that contains all the bulletpoints 
  for(var i = 0; i < items.length; i++) {
    //its going to iterate through each index of items
    items[i].classList.add('red');
    //it'll add red if red isn't in the class (for "thelist" from the index.html file)
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      //even add red, odd add blue to class
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
// FAC
// GCD

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};


