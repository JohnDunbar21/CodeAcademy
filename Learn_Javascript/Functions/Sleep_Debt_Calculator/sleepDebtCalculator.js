let getSleepHours = day => {
    day.toLowerCase();
    switch (day){
        case 'monday':
            return 6;
            break;
        case 'tuesday':
            return 8;
            break;
        case 'wednesday':
            return 5;
            break;
        case 'thursday':
            return 9;
            break;
        case 'friday':
            return 4;
            break;
        case 'saturday':
            return 8;
            break;
        case 'sunday':
            return 6;
            break;
        default:
            return 0;
            break;
    }
}
let getActualSleepHours = () => getSleepHours('monday')+getSleepHours('tuesday')+getSleepHours('wednesday')+getSleepHours('thursday')+getSleepHours('friday')+getSleepHours('saturday')+getSleepHours('sunday');

let getIdealSleepHours = () => {
    let idealHours = 8;
    return idealHours * 7;
}

let calculateSleepDebt = () => {
    let actualSleepHours = getActualSleepHours();
    let idealSleepHours = getIdealSleepHours();
    if (actualSleepHours === idealSleepHours){
        console.log('You do not owe any sleep. You are debt free!');
    } else if (actualSleepHours > idealSleepHours){
        console.log('You got'+(actualSleepHours-idealSleepHours)+' more sleep than you needed. You are well rested!');
    } else {
        console.log('You owe '+(idealSleepHours-actualSleepHours)+' hours of sleep. Go to sleep when possible!');
    }
}

calculateSleepDebt();