// Prior to ES6, var was the only way to declare a variable, but now can be assigned using 'let' or 'const'.
var favoriteFood = 'pizza';
var numOfSlices = 8;
console.log(favoriteFood)
console.log(numOfSlices);

// You do not specify the type of variable (e.g. int, String, boolean, etc).
let changeMe = true;
changeMe = false;
console.log(changeMe);

// Once a 'const' constant variable is set, it cannot be changed: any attempt to do so will throw a Syntax Error.
const entree = 'Enchiladas';
console.log(entree);
//entree = 'Tacos';

let levelUp = 10;
let powerLevel = 9001;
let multiplyMe = 32;
let quarterMe = 1152;

// Use the mathematical assignments in the space below:
levelUp += 5;
powerLevel -= 100;
multiplyMe *= 11;
quarterMe /= 4;


// These console.log() statements below will help you check the values of the variables.
// You do not need to edit these statements. 
console.log('The value of levelUp:', levelUp); 
console.log('The value of powerLevel:', powerLevel); 
console.log('The value of multiplyMe:', multiplyMe); 
console.log('The value of quarterMe:', quarterMe);

// ++ is increment by 1, -- is decrement by 1.
let gainedDollar = 3;
let lostDollar = 50;

gainedDollar++;
lostDollar--;

let favoriteAnimal = 'Racoon';
console.log('My favourite animal: '+favoriteAnimal);

/* String interpolation allows you to directly insert a variable into a string without concatenation.

   This has to be done using the `` keys instead of the standard '' keys.
*/
let myName = 'John';
let myCity = 'Aberdeen';
console.log(`My name is ${myName}. My favorite city is ${myCity}.`)

// The typeof keyword returns the data type in the variable.
let newVariable = 'Playing around with typeof.';
console.log(typeof newVariable);
newVariable = 1;
console.log(typeof newVariable);