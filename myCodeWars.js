// An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

// isIsogram("Dermatoglyphics") == true
// isIsogram("aba") == false
// isIsogram("moOse") == false // -- ignore letter case



function isIsogram(str){
    const array = {};
    str = str.toLowerCase();
    for (var i = 0; i < str.length; i++) {
      if (array[str[i]]) {
        return false;
      }
      array[str[i]] = true;
    }
    return true; 
 }
 
 
 console.log(isIsogram("Dermatoglyphics"));
 console.log(isIsogram("isogram"));
 console.log(isIsogram("aba"));
 console.log(isIsogram("moOse"));
 console.log(isIsogram("isIsogram"));
 console.log(isIsogram(""));
 