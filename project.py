import matplotlib.pyplot as plt
import numpy as np
#for line in open("project.txt"):
 #   print(line)

x = [1, 3, 5, 7, 9]
y = [1.5, 2.8, 4.0, 4.7, 6.0]

degree = int(input("Enter degree:"))

def SUM_XY(x, y, degree):
    X_SUM = []
    Y_SUM = [] 
    for i in range((2 * degree)+ 1):
        a = 0
        for n in range(len(x)):
            a += (x[n] ** i)
        X_SUM.append(a)
    for i in range(degree + 1):
        b = 0
        for n in range(len(x)):
            b += ((x[n] ** i) * y[n])
        Y_SUM.append(b)
    return X_SUM, Y_SUM

def constant(x, y, degree):
    sx, sxy = SUM_XY(x, y, degree)
    s = []
    for j in range(degree + 1):
        s.append(sx[j:j+degree+1])
    a = np.array(s)
    b = np.array(sxy)
    res = np.linalg.solve(a, b)
    return res
def f(x_co, res, degree):
    fun = []
    for n in range(len(x_co)):
        a = 0
        for i in range(degree, -1, -1): 
            a += (res[i] * (x_co[n] ** i))
        fun.append(a)
    return fun
res = constant(x, y, degree)
print("y = ",end = "") 
for i in range(degree,0,-1):
    print(res[i],"(x **", i,") + ", end = " ")
print(res[0])
print()

#output(x, y, degree)    
       
#plot(x, y,'*')
#plot(x, y)
#ylabel('y')
#xlabel('x')
#ylim(min(y), max(y))
#xlim(min(x), max(x)) 
#show()     
#res = constant(x, y, degree)
x_co = np.linspace(min(x), max(x), 100)
y_co = f(x_co, res, degree) 
plt.plot(x_co, y_co)
plt.xlim(min(x_co), max(x_co))
plt.ylim(min(y_co), max(y_co))
plt.plot(x, y,'o')
plt.show()
