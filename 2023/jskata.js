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


// FAKE BINARY
function fakeBin(x) { 
  return x.split('').map(n => n < 5 ? 0 : 1).join('');
} // map() - creates a new array populated with the results of calling a provided function on every element in the calling array
// regex
function fakeBin(x) {
  return x.replace(/\d/g, d => d < 5 ? 0 : 1);
} // /\d/g is same as /[0-9]/g - it matches all digit characters (0-9)
function fakeBin(x){
  return x.replace( /[0-4]/g, "0" ).replace( /[5-9]/g, "1" )
} // [0-4] is set of individual characters '0', '1', '2', '3', '4' - same with [5-9]
// replace() - returns a new string with one, some, or all matches of a pattern replaced by a replacement
// when the string is passed in the function, replace() processes each character in the string
// my solution
function fakeBin(x){
  return x.split('').flatMap((char) =>
                              char >= 5 ? '1' : '0').join('')
} // flatMap() - returns a new array formed by applying a given callback function to each element of the array, and then flattening the result by one level. identical to a map() followed by a flat() of depth 1 (arr.map(...args).flat()), but slightly more efficient than calling those two methods separately.
// flat () - creates a new array with all sub-array elements concatenated into it recursively up to the specified depth. eg. arr1 = [0, 1, 2, [3, 4]] -> console.log(arr1.flat()) -> Array [0, 1, 2, 3, 4]


// KEEP HYDRATED!
const litres = time => Math.floor(time * 0.5) // arrow function
// my solution
function litres(time) {
  return Math.floor(time * 0.5)
}


// GET THE MIDDLE CHARACTER
function getMiddle(s){
  return s.substr(Math.ceil(s.length / 2 - 1), s.length % 2 === 0 ? 2 : 1);
} // subtr(start index, how many characters)
// eg. 'test' -> substr(Math.ceil(4/2-1), 4%2 === 0 ? 2 : 1) -> substr(Math.ceil(2-1), 2) -> substr(1, 2)
function getMiddle(s){
  return s.slice((s.length-1)/2, s.length/2+1);
} // slice(starting character, character index after the required character)
// eg. 'test' -> slice((4-1)/2, 4/2+1) -> slice(3/2, 2+1) -> slice(1.5, 3) -> slice(1, 3)
// my solution
function getMiddle(s){
  return s.length % 2 == 1 ? s.slice(s.length/2, s.length/2 + 1) : s.slice(s.length/2 - 1, s.length/2 + 1)
}


// SUM OF THE FIRST NTH TERM OF SERIES
// my solution
function SeriesSum(n){
  let sum = 0
  for(let i = 0; i < n; i++) {
    sum += 1/ (1 + 3 * i)
  }
  return sum.toFixed(2)
}


// SENTENCE SMASH
const smash = words => words.join(' ');
// my solution
function smash (words) {
  return words.toString().split(',').join(' ')
};


// GROWTH OF A POPULATION
const nbYear = (p0, percent, aug, p) => // recursive + arrow function and ternary operator
  p0 < p ? true + nbYear(p0 + p0 * percent / 100 + aug | 0, percent, aug, p) : false
// Recursive function: exit condition p0 >= p
function nbYear(p0, percent, aug, p) {
  p0 =  Math.floor(p0*(1+percent/100)+aug)
  if (p0>=p)
     return 1
  return nbYear(p0,percent,aug,p)+1
}
// my solution
function nbYear(p0, percent, aug, p) {
  let n = 0
  for (let i = p0; i < p; n++) {
    i += Math.trunc(i * (percent/100) + aug) // Math.trunc() completely strips the decimal
  }
  return n
}


