let userName = 'John Dunbar';

userName ? console.log(userName) : console.log('John Doe');

let userQuestion = 'How will I feel today?';

console.log(`Hello, ${userName}! Your question was: "${userQuestion}".`);
/* In order to make the set of numbers from the random() function to work, we need to multiply it by n+1 where n is the maximum value you seek.

The random() function gathers a value between 0 and 1, so it will be a decimal, hence the need to floor the value after multiplying it.
*/
let randomNumber = Math.floor(Math.random() * 8);
let eightBall = '';

switch (randomNumber){
  case 0:
    eightBall = 'It is certain';
    break;
  case 1:
    eightBall = 'It is decidely so';
    break;
  case 2:
    eightBall = 'Reply hazy try again';
    break;
  case 3:
    eightBall = 'Cannot predict now';
    break;
  case 4:
    eightBall = 'Do not count on it';
    break;
  case 5:
    eightBall = 'My sources say no';
    break;
  case 6:
    eightBall = 'Outlook not so good';
    break;
  case 7:
    eightBall = 'Signs point to yes';
    break;
  default:
    eightBall = 'Error!';
    break;
}
console.log(`My answer to you question is: ${eightBall}`);