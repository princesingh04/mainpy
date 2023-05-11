def fibb(n):
  if(n==0):
    return 0
  elif(n==1):
    return 1
  return fibb(n-1)+fibb(n-2)
n = int(input('Enter the number'))
print(f'Fibb term of {n} is ',fibb(n))
