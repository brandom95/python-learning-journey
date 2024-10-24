/*
// Restart Game Button
var restart = document.querySelector('#b');

// Grab all the squares
var squares = document.querySelectorAll("td");


// Clear Squares Function
function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = '';
  }

}
restart.addEventListener('click',clearBoard)




// Create a function that will check the square marker
function changeMarker(){
    if(this.textContent === ''){
      this.textContent = 'X';
      // console.log(marker)
    }else if (this.textContent === 'X') {
      this.textContent = 'O';
    }else {
      this.textContent = '';
    }
};

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', changeMarker);
}

*/

var reset = document.getElementById("b");

function refreshing (){
    window.location.reload();
}
reset.addEventListener("click", refreshing)

// user turn 1
var userTurn = document.querySelectorAll("td");
for(var i = 0; i < userTurn.length; i++) {
    userTurn[i].addEventListener("click", function() {
    this.textContent = "X";
    })

    userTurn[i].addEventListener("dblclick", function() {
    this.textContent = "O";
    })


}







