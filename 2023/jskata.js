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


// CONVERT A STRING TO A NUMBER
var stringToNumber = function(str){
  return parseInt(str); // will still parse the number even if it included other characters eg. '123a' will return 123
} // parseInt(value, radix) - takes a string and returns the first number and converts it from the given radix into base10
var stringToNumber = function(str){
  return Number(str); // faster than parseInt(), but if number included other characters eg. '123a' it will return NaN
} // Number() - tries to cast the input as a number
// my solution
var stringToNumber = function(str){
  return +str; // if the operand is not a number, converts it into a number. similar to Number()
} // numeric conversion - unary