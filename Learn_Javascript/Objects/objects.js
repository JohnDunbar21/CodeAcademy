// creating object literals
/*
An object literal is designated to a variable, and is encased in {}.

An object is filled with unordered data which is then organised into key-value pairs, where the key is like a variable
and can be of any data type including functions and other objects.
*/
let fasterShip = {
    'Fuel Type': 'Turbo Fuel',
    color: 'silver'
}
// the above object has two key-value pairs that form it.

let spaceship = {
    homePlanet: 'Earth',
    color: 'silver',
    'Fuel Type': 'Turbo Fuel',
    numCrew: 5,
    'Active Mission' : true,
    'Secret Mission' : 'Discover life outside of Earth.',
    flightPath: ['Venus', 'Mars', 'Saturn']
}
  
// you use dot-notation to access data in an object, as shown below.
let crewCount = spaceship.numCrew;
let planetArray = spaceship.flightPath;

// you can also use bracket-notation to access data in an object.
let isActive = spaceship['Active Mission'];
console.log(spaceship['Active Mission']);

// you can reassign a key-value pair by letting the <object>.<property> = newValue.
spaceship.color = 'glorious gold';

// if the key you are assigning a value to does not exist, it will create it.
spaceship.numEngines = 4;

// the delete keyword will remove a key-value pair from the object.
delete spaceship['Secret Mission'];


// methods are an important concept within objects as they invoke the properties you give them, a basic example is shown below.
let retreatMessage = 'We no longer wish to conquer your planet. It is full of dogs, which we do not care for.';
const alienShip = {
  retreat() {
    console.log(retreatMessage);
  },
  takeOff() {
    console.log('Spim... Borp... Glix... Blastoff!');
  }
}
alienShip.retreat();
alienShip.takeOff();

// below is an object with initialised key-value pairs, some of which are nested properties, each having their own key-value pairs.
let spaceship1 = {
    passengers: [{name: 'Space Dog'}],
    telescope: {
      yearBuilt: 2018,
      model: "91031-XLT",
      focalLength: 2032 
    },
    crew: {
      captain: { 
        name: 'Sandra', 
        degree: 'Computer Engineering', 
        encourageTeam() { console.log('We got this!') },
       'favorite foods': ['cookies', 'cakes', 'candy', 'spinach'] }
    },
    engine: {
      model: "Nimbus2000"
    },
    nanoelectronics: {
      computer: {
        terabytes: 100,
        monitors: "HD"
      },
      'back-up': {
        battery: "Lithium",
        terabytes: 50
      }
    }
}; 
let capFave = spaceship1.crew.captain['favorite foods'][0];
let firstPassenger = spaceship1.passengers[0];


let spaceship2 = {
    'Fuel Type' : 'Turbo Fuel',
    homePlanet : 'Earth'
};
  
let greenEnergy = obj => {
    obj['Fuel Type'] = 'avocado oil';
}
  
let remotelyDisable = obj => {
    obj.disabled = true;
}
  
greenEnergy(spaceship2);
remotelyDisable(spaceship2);
console.log(spaceship2);

let spaceship3 = {
    crew: {
    captain: { 
        name: 'Lily', 
        degree: 'Computer Engineering', 
        cheerTeam() { console.log('You got this!') } 
        },
    'chief officer': { 
        name: 'Dan', 
        degree: 'Aerospace Engineering', 
        agree() { console.log('I agree, captain!') } 
        },
    medic: { 
        name: 'Clementine', 
        degree: 'Physics', 
        announce() { console.log(`Jets on!`) } },
    translator: {
        name: 'Shauna', 
        degree: 'Conservation Science', 
        powerFuel() { console.log('The tank is full!') } 
        }
    }
}; 

// Write your code below

for (let crewMember in spaceship3.crew) {
  console.log(`${crewMember}: ${spaceship3.crew[crewMember].name}`)
};

for (let crewMember in spaceship3.crew) {
  console.log(`${spaceship3.crew[crewMember].name}: ${spaceship3.crew[crewMember].degree}`)
};