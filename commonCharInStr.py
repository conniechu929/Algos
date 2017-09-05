def commonString(str1, str2):

  if not str1 or not str2:
    return False

  dict1 = {}
  dict2 = {}
  result = ''

  # for i in range(len(str1)):
  #   if str1[i] not in dict1:
  #     dict1[str1[i]] = 1
  #   else:
  #     dict1[str1[i]] += 1

  # for j in range(len(str2)):
  #   if str2[j] not in dict1:
  #     dict2[str2[j]] = 1
  #   else:
  #     dict2[str2[j]] += 1
  i = 0
  while i < len(str1) or i < len(str2):
    if i < len(str1):
      if str1[i] in dict2 and dict2[str1[i]] > 0:
        result = result + str1[i]
        dict2[str1[i]] -= 1
      else:
        if str1[i] not in dict1:
          dict1[str1[i]] = 1
        else:
          dict1[str1[i]] += 1

    if i < len(str2):
      if str2[i] in dict1 and dict1[str2[i]] > 0:
        result = result + str2[i]
        dict1[str2[i]] -= 1
      else:
        if str2[i] not in dict2:
          dict2[str2[i]] = 1
        else:
          dict2[str2[i]] += 1
    i+= 1
  return result

print commonString('bnnnworlld', 'cchelloccc')
