// CONVERT BOOLEAN VALUES TO STRINGS 'YES' OR 'NO'
function boolToWord( bool ){ // ternary operator
  return bool ? 'Yes':'No'; // (condition) ? run this code : run this code instead
}
// my solution
function boolToWord( bool ){
  if (bool === true) {
    return "Yes"
  }
  else {
    return "No"
  }
}


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


// COUNTING SHEEP
function countSheeps(arrayOfSheeps) {
  return arrayOfSheeps.filter(Boolean).length; 
} // filter() method creates a new array with all elements that pass the test implemented by the provided function - Boolean function. when an element is passed to the Boolean function, it returns true for truthy values and false for falsy values - true values will pass the test while false, null and undefined values will not pass the test. eg. [true, false, null, undefined] will become [true]. the length property returns the number of elements in the array.
// my solution
function countSheeps(sheep) {
  let s = 0
  for(let i = 0; i <= sheep.length; i++) {
    if (sheep[i] == true) {
      s += 1
    }
    else {
      s += 0
    }
  }
  return s
}


// GRASSHOPPER - SUMMATION
const summation = n => n * (n + 1) / 2;
// eg. 8 * (8 + 1) / 2 | 36 is (1+2+3+4+5+6+7+8)
// my solution
var summation = function (num) {
  let s = 0
  for(let i = 1; i <= num; i ++) {
    s += i
  }
  return s
}


// REVERSED STRINGS
function solution(str){
  return str.split('').reverse().join('');  
} // eg. 'world'.split('') -> ['w', 'o', 'r', 'l', 'd'].reverse() -> ['d', 'l', 'r', 'o', 'w'].join('') -> 'dlrow'
// my solution
function solution(str){
  let s = ''
  for(let i = str.length-1; i >= 0; i--) {
    s += str[i]
  }
  return s
}


// OPPOSITES ATTRACT
function lovefunc(flower1, flower2){
  return flower1 % 2 !== flower2 % 2;
}
// my solution
function lovefunc(flower1, flower2){
  return flower1 % 2 != flower2 % 2 ? true : false;
}


// REMOVE FIRST AND LAST CHARACTER
// my solution
function removeChar(str) {
  return str.slice(1, -1);
}