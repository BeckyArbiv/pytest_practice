def findpoint(x1, x2, a):
    slope = (x2[1]-x1[1])/(x2[0]-x1[0])
    y = slope*(a -x1[0])+x1[0]
    print(y)
    return y


findpoint((0,0),(1,1),6)