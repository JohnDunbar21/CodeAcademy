const robot = {
    model: '1E78V2',
    _energyLevel: 100,
    provideInfo() {
      return `I am ${this.model} and my current energy level is ${this._energyLevel}`
    },
    checkEnergy() {
        console.log(`Energy is currently at ${this._energyLevel}%.`)
    },
    recharge(){
        this._energyLevel += 30;
        console.log(`Recharged! Energy is currently at ${this._energyLevel}%.`)
    } 
}
console.log(robot.provideInfo());
robot.recharge();

/*
getter methods using the get keyword return the internal properties of an object.

when using a getter or setter method, properties cannot share the same name as the getter/setter function: otherwise
this will cause an infinite loop.
*/
const robot1 = {
    _model: '1E78V2',
    _energyLevel: 100,
    get energyLevel() {
      if (typeof this._energyLevel === 'number'){
        return `My current energy level is ${this._energyLevel}`
      } else {
        return 'System malfunction: cannot retrieve energy level'
      }
    }
};
  
console.log(robot1.energyLevel);

/*
setter methods reassign values of existing properties within an object.

you can still reassign values directly even with a setter method.
*/
const robot2 = {
    _model: '1E78V2',
    _energyLevel: 100,
    _numOfSensors: 15,
    get numOfSensors(){
      if(typeof this._numOfSensors === 'number'){
        return this._numOfSensors;
      } else {
        return 'Sensors are currently down.'
      }
    },
    set numOfSensors(num) {
      if (typeof num === 'number' && num >= 0){
        this._numOfSensors = num;
      } else {
        console.log('Pass in a number that is greater than or equal to 0')
      }   
    } 
};
  
robot2.numOfSensors = 100;
console.log(robot2.numOfSensors);


/*
factory functions create many instances of an object quickly.

these functions can have parameters that allow the object returned to be customised.
*/

let robotFactory = (model, mobile) => {
    return {
      model: model,
      mobile: mobile,
      beep() {
        console.log('Beep Boop')
      }
    }
}
const tinCan = robotFactory('P-500', true);
tinCan.beep();

/*
when using a factory function, you can use shorthand to prevent repetitive code.
*/
function robotFactory1(model, mobile){
    return {
      model,
      mobile,
      beep() {
        console.log('Beep Boop');
      }
    }
}
  
// To check that the property value shorthand technique worked:
const newRobot = robotFactory1('P-501', false)
console.log(newRobot.model)
console.log(newRobot.mobile)

/*
By assigning a variable to the name of an object property and passing in the object as a value, it will give the value and/or
any associated methods to that variable.
*/
const robot3 = {
    model: '1E78V2',
    energyLevel: 100,
    functionality: {
      beep() {
        console.log('Beep Boop');
      },
      fireLaser() {
        console.log('Pew Pew');
      },
    }
};
const {functionality} = robot3;
functionality.beep();



const robot4 = {
	model: 'SAL-1000',
  mobile: true,
  sentient: false,
  armor: 'Steel-plated',
  energyLevel: 75
};

// What is missing in the following method call?
const robotKeys = Object.keys(robot4);

console.log(robotKeys);

// Declare robotEntries below this line:
const robotEntries = Object.entries(robot4);

console.log(robotEntries);

// Declare newRobot below this line:
const newRobot2 = Object.assign({laserBlaster: true, voiceRecognition: true}, robot4);

console.log(newRobot2);