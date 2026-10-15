memoDb = {1: 1}

def collatz(n):
  if n in memoDb:
    return memoDb[n]

  if n % 2 == 0:
    nxt = n // 2
  else:
    nxt = 3*n + 1
  memoDb[n] = 1 + collatz(nxt)
  return memoDb[n]

for i in range(1, 1000000):
  collatz(i)

maxKey= max(memoDb, key=memoDb.get)

print(f"Number {maxKey} produces the longest chain with length {memoDb[maxKey]}")