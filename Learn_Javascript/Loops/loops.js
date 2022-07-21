for (let i = 5; i <= 10; i++){ // starts at 5 and runs to 10.
    console.log(i);
}

for (let counter = 3; counter >= 0; counter--){ // starts at 3 and runs to 0.
    console.log(counter);
}

const vacationSpots = ['Bali', 'Paris', 'Tulum'];

// Write your code below
for (let i = 0; i < vacationSpots.length; i++){
  console.log(`I would love to visit ${vacationSpots[i]}`);
}

// nested for-loop.
let bobsFollowers = ['Billy', 'James', 'Kate', 'Sally'];
let tinasFollowers = ['Kate', 'James', 'Evelyn'];
let mutualFollowers = [];
for (let i = 0; i < bobsFollowers.length; i++){
  for (let j = 0; j < tinasFollowers.length; j++){
    if (bobsFollowers[i] === tinasFollowers[j]){
      mutualFollowers.push(tinasFollowers[j]);
    }
  }
}

const cards = ['diamond', 'spade', 'heart', 'club'];

// while-loop.
let currentCard;
while (currentCard != 'spade'){
  currentCard = cards[Math.floor(Math.random() * 4)];
  console.log(currentCard);
}


/*
A do-while loop will always run at least once, regardless of the conditions, where a while loop will not execute without the necessary conditions.

The syntax is demonstrated below.
*/
let cupsOfSugarNeeded = 4;
let cupsAdded = 0;
do {
  cupsAdded++
  console.log(cupsAdded);
} while (cupsAdded < cupsOfSugarNeeded);

const rapperArray = ["Lil' Kim", "Jay-Z", "Notorious B.I.G.", "Tupac"];

// Write your code below
for (let i = 0; i < rapperArray.length; i++){
  console.log(rapperArray[i]);
  if (rapperArray[i] === 'Notorious B.I.G.'){
    break;
  }
}
console.log("And if you don't know, now you know.");

