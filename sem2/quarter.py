x = int(input())
y = int(input())
if x>0 and y>0:
    print("first quarter")
elif x>0 and y<0:
    print("fourth quarter")
elif y>0:
    print("second quarter")
else:
    print("third quarter")
