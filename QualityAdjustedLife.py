x = int(input())
running_total = float(0)

while x > 0:
    q,r = map(float, input().split())
    running_total += q * r
    x-=1
print(running_total)