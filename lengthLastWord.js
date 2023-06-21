// 58. Length of Last Word

// Given a string s consisting of words and spaces, return the length of the last word in the string.

// A word is a maximal substring consisting of non-space characters only.


var lengthOfLastWord = function(str) {
  let split = str.split(' ');

  for (let i = split.length - 1; i >= 0; i--) {
      if (split[i] !== '') return split[i].length;
  }
};