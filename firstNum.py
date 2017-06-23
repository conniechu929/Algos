num_list = [5, 4, -1, 9]
num_list2 = [3,4,-1,1]

def firstNum(list):
  list.sort()
  for i in range(len(list)-1):
    if list[i] + 1 != list[i+1]:
      result = list[i] + 1
      if list[i] == -1 and list[i+1] == 1:
        continue
      elif result == 0:
        return result + 1
      else:
        return result
  return list[len(list)-1] + 1


print firstNum(num_list2)
