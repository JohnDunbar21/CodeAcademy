let menu = {
    _meal: '',
    _price: 0,
    set meal(mealToCheck){
        if (typeof mealToCheck === 'string'){
            return this._meal = mealToCheck;
        }
    },
    set price(priceToCheck){
        if (typeof priceToCheck === 'number'){
            return this._price = priceToCheck;
        }
    },
    get todaysSpecial(){
        if (this._meal && this._price){
            return `Today's special is ${this._meal} for $${this._price}!`
        } else {
            return 'Meal or price was not set correctly!'
        }
    }
}
// menu._meal = 4;
// menu._price = 'price';
// console.log(menu);

menu._meal = 'Beans';
menu._price = 4;
console.log(menu.todaysSpecial);
