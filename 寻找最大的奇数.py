s = "43383"
t =len(s)
for i in range(t-1,-1,-1):
    if int(s[i])%2 == 1:
        print(s[:i+1])
        break
    else:
        print("no")