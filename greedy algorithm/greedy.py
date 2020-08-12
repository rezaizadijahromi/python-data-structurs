Array = [6, 3 , 2, 7, 5, 5, 5]

Array = sorted(Array)

for i in range(len(Array)//2):
    print(Array[i], Array[~i])
    