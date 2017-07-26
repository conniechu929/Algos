function commonEnding(s1, s2) {
    var my_s1 = s1.toLowerCase()
    var my_s2 = s2.toLowerCase()
    var result = ''
    var arr1_end = s1.length - 1;
    var arr2_end = s2.length - 1;
    if (s1.length > 0 && s2.length > 0 && typeof(s1) == 'string' && typeof(s2) == 'string'){
        while(arr1_end >= 0 && arr2_end >= 0){
          if (s1[arr1_end].toLowerCase() == s2[arr2_end].toLowerCase()) {
            result = s1[arr1_end].toLowerCase() + result;
            arr1_end--;
            arr2_end--;
          }
          else{
            break
          };
        }
        return result;
    }
    else{
        return "";
    }
}
