import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f = open("output.txt")
count_array = {}
plot_array = [0]*20
plot_array_above_1000 = [0]*20
num_of_ipv4 = 0
for k in count_array:
    k = 0

line = f.readline()
if line:
    a = line.split("|")
    start_time = int(float(a[2]))
    if ":" not in a[9]:
        if a[12] not in count_array:
            count_array[a[12]] = 1
        else:
            count_array[a[12]] += 1
        
        num_of_ipv4 += 1

line = f.readline()
while line:
    a = line.split("|")
    if ":" not in a[9]:
        if a[12] not in count_array:
            count_array[a[12]] = 1
        else:
            count_array[a[12]] += 1
        num_of_ipv4 +=1 
    line = f.readline()

    


f.close()

diff_peer_asn_num = len(count_array)


for hello in count_array.values():
    plot_array[int(hello/1000)] += 1
    if hello > 1000:
        plot_array_above_1000[int(hello/1000)] += 1

print("num_of_ipv4_update : " + str(num_of_ipv4))
print("diff_origin_as_num : " + str(diff_peer_asn_num))

xlabel = range(0, 20000, 1000)
xlabel2 = range(0, 20000, 1000)
plt.plot(xlabel, plot_array)
plt.xlabel("origin-as update number")
plt.ylabel("origin-as number")
plt.title("20200930-2355")
plt.show()
print(sorted(count_array.items(), key=lambda x:x[1]))

plt.plot(xlabel2, plot_array_above_1000)
plt.xlabel("origin-as update number")
plt.ylabel("origin-as number")
plt.title("20200930-2355 (above 1000)")
plt.show()
