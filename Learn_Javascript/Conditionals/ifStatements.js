let sale = true;
//sale = false;
if (sale === true){
  console.log('Time to buy!');
} else {
    console.log('Time to wait for a sale.')
}
/* Comparison Operators:
    - < is less than.
    - > is greater than.
    - <= is less than or equal to.
    - === is equal to.
    - !== is not equal to.
*/
let hungerLevel = 7;
if (hungerLevel > 7){
  console.log('Time to eat!');
} else{
  console.log('We can eat later!')
}
/* Logical Operators:
    - && is AND.
    - || is OR.
    - ! is NOT.
*/
let mood = 'sleepy';
let tirednessLevel = 6;

if (mood === 'sleepy' && tirednessLevel > 8){
  console.log('time to sleep');
} else{
  console.log('not bed time yet')
}

let wordCount = 22;

if (wordCount) {
  console.log("Great! You've started your work!");
} else {
  console.log('Better get to work!');
}


let favoritePhrase = '';

if (favoritePhrase) {
  console.log("This string doesn't seem to be empty.");
} else {
  console.log('This string is definitely empty.');
}
/*
If you have the following code:

let username = '';
let defaultName = username || 'Stranger';

the username will be assigned to defaultUsername as the left of || is checked first if, and only if, username is not false (empty).
Otherwise, the right hand side will be assigned.
*/
let tool = '';
//tool = 'marker';

// Use short circuit evaluation to assign  writingUtensil variable below:
let writingUtensil = tool || 'pen';

console.log(`The ${writingUtensil} is mightier than the sword.`);

/* Ternary Operator:
    Is a shorthand method of writing an if-else condition as shown below.
*/
let isNightTime = true;
 
if (isNightTime) {
  console.log('Turn on the lights!');
} else {
  console.log('Turn off the lights!');
}
// becomes...
isNightTime ? console.log('Turn on the lights!') : console.log('Turn off the lights!');

let isLocked = false;

isLocked ? console.log('You will need a key to open the door.') : console.log('You will not need a key to open the door.');
/*
if (isLocked) {
  console.log('You will need a key to open the door.');
} else {
  console.log('You will not need a key to open the door.');
}
*/
let isCorrect = true;

isCorrect ? console.log('Correct!') : console.log('Incorrect!');
/*
if (isCorrect) {
  console.log('Correct!');
} else {
  console.log('Incorrect!');
}
*/
let favouritePhrase = 'Love That!';

favouritePhrase === 'Love That!' ? console.log('I love that!') : console.log("I don't love that!");
/*
if (favoritePhrase === 'Love That!') {
  console.log('I love that!');
} else {
  console.log("I don't love that!");
}
*/

// Else-if's in an if-else statement.
let season = 'summer';

if (season === 'spring') {
  console.log('It\'s spring! The trees are budding!');
} else if (season === 'winter') {
  console.log("It's winter! Everything is covered in snow.");
} else if (season === 'fall') {
  console.log("It's fall! Leaves are falling!");
} else if (season === 'summer') {
  console.log("It's sunny and warm because it's summer!");
} else {
  console.log('Invalid season.');
}

// Switch statements.
let athleteFinalPosition = 'first place';

switch (athleteFinalPosition) {
  case 'first place':
    console.log('You get the gold medal!');
    break;
  case 'second place':
    console.log('You get the silver medal!');
    break;
  case 'third place':
    console.log('You get the bronze medal!');
    break;
  default:
    console.log('No medal awarded.');
    break;
}
