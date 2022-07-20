
const getUserChoice = userInput => {
    userInput.toLowerCase();
    switch (userInput){
        case 'rock':
            return userInput;
            break;
        case 'paper':
            return userInput;
            break;
        case 'scissors':
            return userInput;
            break;
        case 'bomb': // cheat code case.
            return userInput;
            break;
        default:
            console.log('Your input is not valid.');
    }
}
// tests
//getUserChoice('rock');
//getUserChoice('door');

function getComputerChoice(){
    randomNumberInput = Math.floor(Math.random() * 3); //initialises an integer between 0 and 2.
    switch (randomNumberInput){
        case 0:
            return 'rock';
            break;
        case 1:
            return 'paper';
            break;
        case 2:
            return 'scissors';
            break;
        default:
            return 'error';
    }
}

function determineWinner(userChoice, computerChoice){
    if (userChoice === computerChoice){
        return 'The game is a tie.';
    }
    if (userChoice === 'rock'){
        if (computerChoice === 'paper'){
            return 'The computer has beaten the user.';
        } else {
            return 'The user has beaten the computer.';
        }
    } else if (userChoice === 'paper'){
        if (computerChoice === 'scissors'){
            return 'The computer has beaten the user.';
        } else {
            return 'The user has beaten the computer.';
        }
    } else if (userChoice === 'scissors'){
        if (computerChoice === 'rock'){
            return 'The computer has beaten the user.';
        } else {
            return 'The user has beaten the computer.';
        }
    } else if (userChoice === 'bomb'){
        return 'The user has obliterated the computer.'; // cheat code to win no matter what.
    }
}

function playGame(){
    // change the userChoice variable to play against the computer.
    let userChoice = getUserChoice('scissors');
    console.log(`The user's choice is ${userChoice}.`);
    let computerChoice = getComputerChoice();
    console.log(`The computer's choice is ${computerChoice}.`);

    console.log(determineWinner(userChoice, computerChoice));
}

playGame();