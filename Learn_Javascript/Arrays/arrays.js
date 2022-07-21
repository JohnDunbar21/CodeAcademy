let newYearsResolutions = ['Keep a journal', 'Take a falconry class', 'Learn to juggle'];

console.log(newYearsResolutions);

const hobbies = ['coding', 'reading', 'painting'];

console.log(hobbies);


const famousSayings = ['Fortune favors the brave.', 'A joke is a very serious thing.', 'Where there is love there is life.'];

let listItem = famousSayings[0]; // accesses the first item of the array.
console.log(listItem);

console.log(famousSayings[2]);


let groceryList = ['bread', 'tomatoes', 'milk'];

groceryList[1] = 'avocados'; // changes the second element of the list.


let condiments = ['Ketchup', 'Mustard', 'Soy Sauce', 'Sriracha'];

const utensils = ['Fork', 'Knife', 'Chopsticks', 'Spork'];

condiments[0] = 'Mayo';
console.log(condiments);

condiments = ['Mayo'];

// a const array variable can have its items mutated, but the variable cannot be reassigned like a let variable.
utensils[3] = 'Spoon';
console.log(utensils);


const objectives = ['Learn a new language', 'Read 52 books', 'Run a marathon'];
console.log(objectives.length); // returns the number of items in the array.


const chores = ['wash dishes', 'do laundry', 'take out trash'];

chores.push('walk dogs', 'hoover');
console.log(chores);


const chores1 = ['wash dishes', 'do laundry', 'take out trash', 'cook dinner', 'mop floor'];

chores1.pop(); // removes the last item from the array.
console.log(chores1);


const groceryList = ['orange juice', 'bananas', 'coffee beans', 'brown rice', 'pasta', 'coconut oil', 'plantains'];

groceryList.shift(); // removes the first item in a list.
console.log(groceryList);

groceryList.unshift('popcorn'); // shifts the list along by 1 and adds the item specified in the brackets.
console.log(groceryList);

console.log(groceryList.slice(1, 4)); //start to end+1.
console.log(groceryList); // slice is a non-mutating method.

const pastaIndex = groceryList.indexOf('pasta'); // returns an int referrring to the index of the item.
console.log(pastaIndex);


const concept = ['arrays', 'can', 'be', 'mutated'];

function changeArr(arr){
  arr[3] = 'MUTATED';
}

changeArr(concept);
console.log(concept);

let removeElement = newArr => newArr.pop(); // arrow function notation.

removeElement(concept);
console.log(concept);


// this is a nested aka 2-d array.
let numberClusters = [[1, 2], [3, 4], [5, 6]];
const target = numberClusters[2][1];