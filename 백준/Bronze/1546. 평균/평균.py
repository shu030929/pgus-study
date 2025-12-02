n = int(input())
a = list(map(int, input().split()))
m = max(a)

total = 0.0
for x in a:
    total += x / m * 100

print(total / n)
