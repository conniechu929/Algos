nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# new_list = [1,2,3,4|,5,6,7,8|,9,10,11,12|,13,14,15,16]

def diagonal(a):
  passes = len(a[0])
  result = [0]*(2*passes-1)
  for i in range((2*passes)-1):
    result[i] = []
  for i in range(passes):
    for j in range(passes):
      result[i+j].append(a[i][j])
  return result

print (diagonal(nums))
