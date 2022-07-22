let story = 'Last weekend, I took literally the most beautifull bike ride of my life. The route is called "The 9W to Nyack" and it stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it literally took me an entire day. I stopped at Riverbank State Park to take some artsy photos. It was a short stop, though, because I had a freaking long way to go. After a quick photo op at the very popular Little Red Lighthouse I began my trek across the George Washington Bridge into New Jersey. The GW is a breathtaking 4,760 feet long! I was already very tired by the time I got to the other side. An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautifull park along the coast of the Hudson. Something that was very surprising to me was that near the end of the route you literally cross back into New York! At this point, you are very close to the end.';

let storyWords = story.split(' ');
let unnecessaryWord = 'literally';
let misspelledWord = 'beautifull';
let badWord = 'freaking';

// method that counts the number of words in the story.
let count = 0;
let numWords = storyWords.forEach(word => {
  count++;
})
console.log(`The number of words in the story: ${count}`);

// method that removes the value stored in the unnecessaryWord variable.
storyWords = storyWords.filter(word => {
  return word !== unnecessaryWord;
})

// method reassigns the storyWords array and changes the value specified in the conditional statement, otherwise returns same array.
storyWords = storyWords.map(word => {
  if (word === misspelledWord){
    return 'beautiful';
  } else {
    return word;
  }
})

// method finds the index value of the badWord variable inside the storyWords array.
let badWordIndex = storyWords.findIndex(word => {
  return word === badWord;
})
console.log(`The bad word is located at index: ${badWordIndex}`);
storyWords[badWordIndex] = 'really'; // replaces the word.

// method checks if all values in the array are less than 10 characters long.
let lengthCheck = storyWords.every(word => {
  return word < 10;
})
console.log(`All words in story are under 10 characters long: ${lengthCheck}`);

// method finds the index of words longer than 10 characters long.
let longWord = storyWords.findIndex(word => {
  return word.length > 10;
})
storyWords[longWord] = 'wonderful'; // replaces the word.

console.log(storyWords.join(' '));