let input = 'Well hello there'; // GENERAL KENOBI...
const vowels = ['a', 'e', 'i', 'o', 'u'];
let resultArray = [];

for (let i = 0; i < input.length; i++){
    input.toLowerCase();
    if (input[i] === 'e'){
        resultArray.push(input[i]);
    } else if (input[i] === 'u'){
        resultArray.push(input[i]);
    }
    for (let j = 0; j < vowels.length; j++){
        if (input[i] === vowels[j]){
            resultArray.push(vowels[j]);
        }
    }
}
console.log(resultArray);
let resultString = (resultArray.join()).toUpperCase();
console.log(resultString);