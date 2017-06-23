nums = [3,7,4,10,11]
# [1,3,4,7]
n = 9
# 3+3+3


def pointTotal(list, n):
  list.sort()
  # list = sorted(list, key=int, reverse=True)
  i = 0

  while list[i] <= n and i < len(list) - 1:
    i+=1
  print i

  if i == 0:
    print 'i==0'
    return False
  else:
    for j in range(i, -1, -1):
      print 'j:',j
      remainder = n % list[j]
      if remainder == 0:
        return True
      else:
        if remainder in list[0:i+1]:
          return True
        else:
          continue
    return False

print pointTotal(nums, 12)
