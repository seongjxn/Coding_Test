N = int(input())
list = list(map(int, input().split()))

count = 0

for i in list :
    for j in range(2, i) :
        if i % j == 0 :
            count += 1

print(count)