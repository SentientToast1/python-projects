data=[(35,5), (17,2), (18,1), (15,3)]

sdata=sorted(data,key = lambda x : x[0])

value, weights = zip(*sdata)

cwf = sum(weights)/2;cw=0

for x in range(len(weights)):
    cw += weights[x]
    if cw > cwf:
        print(value[x])
        break
    else:
        print("out of range!")