function reverseVowel(input){
  var vowels = 'aeiouAEIOU'
  var arr = input.split('')
  var start = 0
  var end = input.length - 1

  while(start < end){
    if(vowels.indexOf(arr[start]) < 0){
      start++;
      continue;
    }
    if(vowels.indexOf(arr[end]) < 0){
      end--;
      continue;
    }

    var results = '';
    results = arr[start];
    arr[start] = arr[end];
    arr[end] = results;

    start++;
    end--;

  }
  return arr.join('')
}

console.log(reverseVowel('Aluminium'))
