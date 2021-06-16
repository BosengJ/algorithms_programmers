a = [1,2,3,'*']

for i in range(len(a)):
    if str(a[i]) not in "*#":
        print(a[i])