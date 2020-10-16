import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

input_year = input('input year')
input_month = input('input month')

num_of_ipv4 = [0]*30
for k in num_of_ipv4:
    k = 0

for i  in range(1, 31):
    f = []
    if i < 10:
        f = open("output" + '0' + str(i) + ".txt")
    else:
        f = open("output" + str(i) + ".txt")

    line = f.readline()
    while line:
        a = line.split("|")
        if ":" not in a[9]:
            num_of_ipv4[i-1] +=1 
        line = f.readline()
    

print(num_of_ipv4)

xlabel = range(1, 31)
plt.plot(xlabel, num_of_ipv4)
plt.xlabel("day")
plt.ylabel("times")
plt.title(input_year + input_month + "1200")
plt.show()


f.close()