
A = [[3,0],
     [-6,-1],
     [5,2]]

B = [[-3,4,0],
     [1,0,-5]]

result = [[sum(a*b for a,b in zip(X_row,Y_col))
                        for Y_col in zip(*B)]
                                for X_row in A]
for r in result:
    print(r)




