const team = {
    _players: [{firstName: 'John', lastName: 'Cena', age: 48}, {firstName: 'Billy', lastName: 'Joel', age: 34}, {firstName: 'Simon', lastName: 'Pegg', age: 59}],
    _games: [{opponent: 'England', teamPoints: 43, opponentPoints: 65}, {opponent: 'Wales', teamPoints: 23, opponentPoints: 42}, {opponent: 'Ireland', teamPoints: 23, opponentPoints: 65}],
    get players (){
        return this._players;
    },
    get games (){
        return this._games;
    },
    addPlayer(newFirstName, newLastName, newAge){
        let newPlayer = {
            firstName: newFirstName,
            lastName: newLastName,
            age: newAge
        }
        return this._players.push(newPlayer);
    },
    addGame(newOpponent, newTeamPoints, newOpponentPoints){
        let newGame = {
            opponent: newOpponent,
            teamPoints: newTeamPoints,
            opponentPoints: newOpponentPoints
        }
        return this._games.push(newGame);
    }
}
team.addPlayer('Bugs', 'Bunny', 76);
console.log(team._players);
team.addGame('Titans', 100, 98);
console.log(team._games);
