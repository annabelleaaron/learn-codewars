// SUM ARRAYS
function sum(numbers) { // js function .reduce() - return the sum of all the elements in the array
    return numbers.reduce((a, b) => a + b, 0);
    // reduce(accumulator, currentValue) => accumulator + currentValue, initialValue)
}
// my solution
function sum (numbers) {
    "use strict";
    let n = 0;
    for (let i = 0; i < numbers.length; i++) {
      n += numbers[i];
    }
    return n;    
};