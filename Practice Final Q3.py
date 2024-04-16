import random
import matplotlib.pyplot as plt

#Q3

random.random() #random number bewteen 0 and 1

x = [0] #array [0]
x.append(1) #array [0,1]
x.append(4) #array [0,1,4]

x = [0]
y = [0]

for i in range(1000):
    num = random.random()
    if(num >= 0 and num <= 0.25):
        x.append((x[-1]) + 1)
        y.append((y[-1]))
    elif(num > 0.25 and num <= 0.5):
        x.append((x[-1]) - 1)
        y.append((y[-1]))
    elif(num > 0.5 and num <= 0.75):
        y.append((y[-1]) + 1)
        x.append((x[-1]))
    else:
        y.append((y[-1]) - 1)
        x.append((x[-1]))

plt.plot(x, y)
plt.show()

#Q4
