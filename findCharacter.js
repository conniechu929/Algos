function FindCharacter(s1, s2){
  s1_dict = {}
  s2_dict = {}

  for(var i = 0; i < s1.length; i++){
    // var key = s1[i]
    if (!s1_dict[s1[i]]) {
      s1_dict[s1[i]] = 1
    }
    else{
      s1_dict[s1[i]] += 1
    }
  }
  for(var j = 0; j < s2.length; j++){
    if (!s2_dict[s2[j]]) {
      s2_dict[s2[j]] = 1
    }
    else{
      s2_dict[s2[j]] += 1
    }
  }
  max = 0
  result = ''
  for (var key in s1_dict) {
    // max = 0
    if (key in s2_dict){
      if(max < s1_dict[key] + s2_dict[key]){
        max = s1_dict[key] + s2_dict[key]
        result = key
      }
      else if(max === s1_dict[key] + s2_dict[key]) {
        result += key
      }
    }
  }
  if(result === ''){
    result = "No Match";
  }
  return result;
}

console.log(FindCharacter('coonnie', 'coonnie'))
