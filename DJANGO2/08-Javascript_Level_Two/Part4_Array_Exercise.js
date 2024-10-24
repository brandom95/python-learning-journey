// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks


// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(addStudent){
     addStudent = prompt("type the name of the student you want to add");
    roster.push(addStudent);

}


// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

function remove(removeStudent){
    removeStudent = prompt("type the name of the student you want to remove");
    for (var i = 0; i < roster.length; i++) {
        if ( roster[i] === removeStudent ){
             roster.pop(roster[i]);
        }
    }

}

// DISPLAY ROSTER

// Create a function called display that prints out the roster to the console.

function display(){
    console.log(roster);
}

// Start by asking if they want to use the web app
var start = prompt("WOuld you like to start the registration? y/n");

if(start === "y"){
 while(roster.length >= 0){
     var select = prompt("Please select an action: add, remove, display, or quit.");
     /////////////add
     if (select === "add"){

         addNew();
     }

     ///////////// remove
     if (select === "remove"){

         remove();
     }

     ///////////// display

      if (select === "display"){

         display();
     }

      ///////////// quit

      if (select === "quit"){
         var displaying = alert("Thanks for using the Web App! Please refresh the page to start over. ");
         break;
     }



 }
}else{
    var bye = alert("Thanks for using the Web App! Please refresh the page to start over. ");

}
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
