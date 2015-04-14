import numpy as np
import matplotlib.pyplot as plt
import sys
#fo = open("xval.txt")
#data = fo.read()
#res = data.strip(", \n ")
#l = res.split(",")
#x = l[:len(l) // 2]
#y = l[len(l) // 2:]
#fo.close()
x = []
y = []
for line in open("xval.txt"):
    a = line.split()
    x.append(float(a[0]))
    y.append(float(a[1]))

l = len(x)
degree =  x[l-1]
x.pop()
y.pop()

if len(x) != len(y):
   print("Enter equal number of x and y values")
   sys.exit()
#for i in range(len(x)):
   # x[i] = float(x[i])
   # y[i] = float(y[i])
           
#x = [1, 2, 3, 4, 5, 6, 7]
#y = [2.3, 5.2, 9.7, 16.5, 29.4, 35.5, 54.4]

#degree = int(input("Enter Degree:"))

z = np.polyfit(x, y, degree)

f = np.poly1d(z)
print(f)
print("\n")

x_co = np.linspace(min(x), max(x), 1000)
y_co = f(x_co)

plt.plot(x_co, y_co, label=f)
plt.xlim(min(x_co), max(x_co))
plt.ylim(min(y_co), max(y_co))
plt.legend(loc='upper left', prop={'size':14})
plt.plot(x, y,'o')
plt.show()
    
