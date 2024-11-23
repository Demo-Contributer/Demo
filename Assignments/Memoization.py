d = {}
def fibo(n):
  if n == 1 or n == 0:
    return n
  elif n in d:
    return d[n]
  else:
    value = fibo(n-1) + fibo(n-2)
    d[n] = value
    return value


for i in range(50):
    print(fibo(i))
