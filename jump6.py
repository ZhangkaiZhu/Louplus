for a in range(0,101):
    if a%6==0:
        continue
    if a%10==6:
        continue
    if a//10==6:
        continue
    print(a)
    a=a+1
