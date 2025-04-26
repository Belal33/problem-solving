def absolutePermutation(n, k=0):
  per = []
  for i in range(1,n+1) :
    if i > k: 
      if per.count(i-k) or (i-k) > n:return -1 
      per.append(i-k)
    else: 
      if per.count(i+k) or (i+k) > n :return -1 
      per.append(i+k)
  return per

print(absolutePermutation(3,0))