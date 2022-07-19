// runs from 0 to 999 inclusive, giving 1000 options in total.
let raceNumber = Math.floor(Math.random() * 1000);
let registerEarly = false;
let runnerAge = 22;

if (runnerAge > 18 && registerEarly === true){
  raceNumber += 1000;
}
if (runnerAge > 18 && registerEarly == true){
  console.log(`Participant: ${raceNumber}, your race will take place at 09:30 am.`);
} else if (runnerAge > 18 && registerEarly == false){
  console.log(`Participant: ${raceNumber}, your race will take place at 11:00 am.`);
} else{
  console.log(`Participant: ${raceNumber}, all participants under the age of 18 are racing at 12:30 pm (this is regardless of the time of registration). Please visit the front desk to register if you haven't already done so.`);
}