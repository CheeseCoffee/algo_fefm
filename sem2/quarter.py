N = int(input())
first = second = third = fourth = 0
for i in range(N):
    x, y = str(input()).split()
    x = int(x)
    y = int(y)
    if x > 0 and y > 0:
        first += 1
    elif x > 0 and y < 0:
        fourth += 1
    elif x < 0 and y > 0:
        second += 1
    elif x < 0 and y < 0:
        third += 1
if first >= second and first >= third and first >= fourth:
    print(1, first)
elif second >= third and second >= fourth:
    print(2, second)
elif third >= fourth:
    print(3, third)
else:
    print(4, fourth)
