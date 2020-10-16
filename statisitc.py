import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


count_array = [0]*300
count_peer_asn = {}
count_origin_as = {}
count_peer_asn_in_second = {}
count_origin_asn_in_second = {}
plot_peer_asn = [0]*20
plot_peer_asn_above_1000 = [0]*20
plot_peer_asn_in_second = [0]*20
plot_origin_as = [0]*20
plot_origin_as_above_1000 = [0]*20
plot_origin_as_in_second = [0]*20
num_of_ipv4 = 0

for k in count_array:
    k = 0
for k in count_peer_asn:
    k = 0
for k in count_origin_as:
    k = 0
for k in count_peer_asn_in_second:
    k = 0
for k in count_origin_asn_in_second:
    k = 0

f = open("output.txt")
line = f.readline()
if line:
    a = line.split("|")
    start_time = int(float(a[2]))
    if ":" not in a[9]:
        count_array[int(float(a[2])) - start_time] += 1
        if a[7] not in count_peer_asn:
            count_peer_asn[a[7]] = 1
        else:
            count_peer_asn[a[7]] += 1
        if a[12] not in count_origin_as:
            count_origin_as[a[12]] = 1
        else:
            count_origin_as[a[12]] += 1
        num_of_ipv4 += 1

line = f.readline()
while line:
    a = line.split("|")
    if ":" not in a[9]:
        count_array[int(float(a[2])) - start_time] += 1
        num_of_ipv4 +=1 
        if a[7] not in count_peer_asn:
            count_peer_asn[a[7]] = 1
        else:
            count_peer_asn[a[7]] += 1
        if a[12] not in count_origin_as:
            count_origin_as[a[12]] = 1
        else:
            count_origin_as[a[12]] += 1
    line = f.readline()

diff_peer_asn_num = len(count_peer_asn)
diff_origin_as_num = len(count_origin_as)

f.close()

print("max index " + str(count_array.index(max(count_array))))
max_index = count_array.index(max(count_array))

for hello in count_peer_asn.values():
    plot_peer_asn[int(hello/1000)] += 1
    if hello > 1000:
        plot_peer_asn_above_1000[int(hello/1000)] += 1

for hello in count_origin_as.values():
    plot_origin_as[int(hello/1000)] += 1
    if hello > 1000:
        plot_origin_as_above_1000[int(hello/1000)] += 1

print("num_of_ipv4_update : " + str(num_of_ipv4))
print("diff_peer_asn_num : " + str(diff_peer_asn_num))

print(num_of_ipv4)

plt.plot(count_array)
plt.xlabel("second")
plt.ylabel("update number")
plt.title("20200930_2355 update number by second")
plt.show()

xlabel = range(0, 20000, 1000)
xlabel2 = range(0, 20000, 1000)
plt.plot(xlabel, plot_peer_asn)
plt.xlabel("update number")
plt.ylabel("peer-asn number")
plt.title("20200930-2355 peer asn")
plt.show()
#print(sorted(count_peer_asn.items(), key=lambda x:x[1]))

plt.plot(xlabel2, plot_peer_asn_above_1000)
plt.xlabel("update number")
plt.ylabel("peer-asn number")
plt.title("20200930-2355 peer asn (above 1000)")
plt.show()


print("diff_origin_as_num : " + str(diff_origin_as_num))

plt.plot(xlabel, plot_origin_as)
plt.xlabel("update number")
plt.ylabel("origin-as number")
plt.title("20200930-2355 origin as")
plt.show()
#print(sorted(plot_origin_as.items(), key=lambda x:x[1]))

plt.plot(xlabel2, plot_origin_as_above_1000)
plt.xlabel("update number")
plt.ylabel("origin-as number")
plt.title("20200930-2355 origin as (above 1000)")
plt.show()

########### max update time
f = open("output.txt")
line = f.readline()
if line:
    a = line.split("|")
    if ":" not in a[9]:
        if (int(float(a[2])) - start_time) == max_index:
            if a[7] not in count_peer_asn_in_second:
                count_peer_asn_in_second[a[7]] = 1
            else:
                count_peer_asn_in_second[a[7]] += 1
            if a[12] not in count_origin_asn_in_second:
                count_origin_asn_in_second[a[12]] = 1
            else:
                count_origin_asn_in_second[a[12]] += 1

line = f.readline()
while line:
    a = line.split("|")
    if ":" not in a[9]:
        if (int(float(a[2])) - start_time) == max_index:
            if a[7] not in count_peer_asn_in_second:
                count_peer_asn_in_second[a[7]] = 1
            else:
                count_peer_asn_in_second[a[7]] += 1
            if a[12] not in count_origin_asn_in_second:
                count_origin_asn_in_second[a[12]] = 1
            else:
                count_origin_asn_in_second[a[12]] += 1
    line = f.readline()

f.close()

for hello in count_peer_asn_in_second.values():
    plot_peer_asn_in_second[int(hello/500)] += 1

for hello in count_origin_asn_in_second.values():
    plot_origin_as_in_second[int(hello/500)] += 1

diff_peer_asn_in_second_num = len(count_peer_asn_in_second)
diff_origin_as_in_second_num = len(count_origin_asn_in_second)

print("diff_peer_asn_in_second_num " + str(count_peer_asn_in_second))
print("diff_origin_as_in_second_num " + str(count_origin_asn_in_second))

print("max_peer_asn update num " + str(count_peer_asn_in_second[max(count_peer_asn_in_second, key=count_peer_asn_in_second.get)]))
print("max_origin_as update num " + str(count_origin_asn_in_second[max(count_origin_asn_in_second, key=count_origin_asn_in_second.get)]))

xlabel3 = range(0, 10000, 500)

plt.plot(xlabel3, plot_peer_asn_in_second)
plt.xlabel("update number")
plt.ylabel("peer-asn number in " + str(max_index))
plt.title("20200930-2355 peer asn in second")
plt.show()


plt.plot(xlabel3, plot_origin_as_in_second)
plt.xlabel("update number")
plt.ylabel("origin-as number in " + str(max_index))
plt.title("20200930-2355 origin as in second")
plt.show()
