// exists outside of the function block and can be accessed by any method in the program as it is a Global variable.
const city = 'New York City'; 

function logCitySkyline(){
  let skyscraper = 'Empire State Building';
  return 'The stars over the '+skyscraper+' in '+city;
}
console.log(logCitySkyline());

// below are three global variables, these can be accessed at any point in the program.
let satellite = 'The Moon';
let galaxy = 'The Milky Way';
let stars = 'North Star';

let callMyNightSky = () => 'Night Sky: '+satellite+', '+stars+', and '+galaxy; // arrow function.
console.log(callMyNightSky());

function logVisibleLightWaves(){
  const lightWaves = 'Moonlight';
  console.log(lightWaves);
}
logVisibleLightWaves();
//console.log(lightWaves); // this will not work as lightWaves is has block-scope, meaning it can only be accessed by the method it resides in.


// reassigning a global variable in a method means that the variable has been changed until the program terminates. This is bad practice, and should not be done often.
// a better way is to have as few global variables as possible, and encapsulate where possible.
const satellite1 = 'The Moon';
const galaxy2 = 'The Milky Way';
let stars3 = 'North Star';

const callMyNightSky2 = () => {
  stars3 = 'Sirius';
	return 'Night Sky: ' + satellite + ', ' + stars + ', ' + galaxy;
};

console.log(callMyNightSky2());
console.log(stars3);

const logVisibleLightWaves = () => {
  let lightWaves = 'Moonlight';
  let region = 'The Arctic';
  // Add if statement here:
  if (region === 'The Arctic'){
    let lightWaves = 'Northern Lights';
    console.log(lightWaves); // will log 'Northern Lights'.
  }
  console.log(lightWaves); // will log 'Moonlight'.
};
  
logVisibleLightWaves();