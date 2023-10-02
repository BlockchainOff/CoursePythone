# Петя:
n = int(input())
max_number = -1
while n < 0:
n = int(input())
if max_number < n:
n = max_number
print(n)