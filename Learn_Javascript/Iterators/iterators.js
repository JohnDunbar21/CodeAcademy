const checkThatTwoPlusTwoEqualsFourAMillionTimes = () => {
  for(let i = 1; i <= 1000000; i++) {
    if ( (2 + 2) != 4) {
      console.log('Something has gone very wrong :( ');
    }
  }
};
  
const isTwoPlusTwo = checkThatTwoPlusTwoEqualsFourAMillionTimes;
isTwoPlusTwo();
console.log(isTwoPlusTwo.name); // returns the function value associated with the variable, taking up much less space in memory.


const addTwo = num => {
    return num + 2;
}
  
const checkConsistentOutput = (func, val) => {
    let checkA = val + 2;
    let checkB = func(val);
    return checkA === checkB ? func(val) : 'inconsistent results'; // checks to see if the two results are valid and match.
}
  
console.log(checkConsistentOutput(addTwo, 10));


const fruits = ['mango', 'papaya', 'pineapple', 'apple'];

// 'forEach()' iterates through a list, and can be used as shown below.
fruits.forEach(fruit => console.log(`I want to eat a ${fruit}.`));


/*
The 'map()' method works similarly to 'forEach()', the major difference being that map() returns a new array.
*/
const animals = ['Hen', 'elephant', 'llama', 'leopard', 'ostrich', 'Whale', 'octopus', 'rabbit', 'lion', 'dog'];

// Create the secretMessage array below
const secretMessage = animals.map(item => {
  return item[0];
})

console.log(secretMessage.join(''));

const bigNumbers = [100, 200, 300, 400, 500];

// Create the smallNumbers array below
const smallNumbers = bigNumbers.map(number => {
  return number/100;
})


/*
The 'filter()' method works like map() but takes an argument to remove certain elements from the original array.
*/
const randomNumbers = [375, 200, 3.14, 7, 13, 852];

// Call .filter() on randomNumbers below
const smallNumbers1 = randomNumbers.filter(number => {
  return number < 250;
})

const favoriteWords = ['nostalgia', 'hyperbole', 'fervent', 'esoteric', 'serene'];


// Call .filter() on favoriteWords below
const longFavoriteWords = favoriteWords.filter(word => {
  return word.length > 7;
})


/*
The 'findIndex()' method looks for the array index of the item specified in the return argument.
*/
const animals1 = ['hippo', 'tiger', 'lion', 'seal', 'cheetah', 'monkey', 'salamander', 'elephant'];

const foundAnimal = animals1.findIndex(animal => {
  return animal === 'elephant';
})

const startsWithS = animals1.findIndex(animalS => {
  return animalS[0] === 's';
})

/*
The code below uses the reduce() method which returns a single value after iterating through all elements in an array.

It can take an optional second parameter which defines a starting value.

This is shown in the code example below.
*/
const newNumbers = [1, 3, 5, 7];

const newSum = newNumbers.reduce((accumulator, currentValue) => {
  console.log(`The value of accumulator: ${accumulator}`);
  console.log(`The value of currentValue: ${currentValue}`);
  return accumulator + currentValue;
}, 10)
console.log(newSum);



const words = ['unique', 'uncanny', 'pique', 'oxymoron', 'guise'];

// some() returns a boolean True or False based on the criteria specified in the return statement.
console.log(words.some(word => {
  return word.length < 6;
}));

const interestingWords = words.filter(word => {
  return word.length > 5;
})

// every() checks that all elements in an array meet the criteria specified in the return statement.
console.log(interestingWords.every((word) => {
  return word.length > 5;
} ));


const cities = ['Orlando', 'Dubai', 'Edinburgh', 'Chennai', 'Accra', 'Denver', 'Eskisehir', 'Medellin', 'Yokohama'];

const nums = [1, 50, 75, 200, 350, 525, 1000];

//  Choose a method that will return undefined
cities.forEach(city => console.log('Have you visited ' + city + '?'));

// Choose a method that will return a new array
const longCities = cities.filter(city => city.length > 7);

// Choose a method that will return a single value
const word = cities.reduce((acc, currVal) => {
  return acc + currVal[0]
}, "C");

console.log(word)

// Choose a method that will return a new array
const smallerNums = nums.map(num => num - 5);

// Choose a method that will return a boolean value
nums.every(num => num < 0);