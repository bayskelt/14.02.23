# task_1
print('task_1')
n = 3
A = []
for i in range(n):
  S = []
  j = 0
  while j < n:
    x = float(input())
    if x <= 30 and x >= -10:
      S.append(x)
    else:
      print('Ви ввели невірне число!')
      j -= 1
    j += 1
  A.append(S)

# task_2
print('\ntask_2')
for i in range(n):
  s = 0
  k = 0
  for j in range(n):
    if A[i][j] >= 1 and A[i][j] <= 20:
      s += A[i][j]
      k += 1
  print(s / k)

# task_3
print('\ntask_3')
for i in range(n):
  for j in range(n):
    if i == j:
      A[i][j] = 33
for i in range(n):
  print(A[i])

# task_4
print('\ntask_4')  
k = int(input())
s = 0
for i in range(n):
  n = 0
  for j in range(n):
    if A[i][j] < k:
      n += 1
  if n == 3:
    s += 1
print(s)
