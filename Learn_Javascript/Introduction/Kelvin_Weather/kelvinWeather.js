// This value will not be changed in the program.
const kelvin = 293;
// The temperature in celsius is 273 less than kelven.
const celsius = kelvin - 273;

// This converts celsius to fahrenheit.
let fahrenheit = celsius * (9/5) + 32;
// This rounds down to the nearest integer.
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);

let newton = celsius * (33/100);
newton = Math.floor(newton);

console.log(`The temperature is ${newton} degrees using the Newton scale.`);