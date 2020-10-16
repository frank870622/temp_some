import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f = open("output.txt")
count_peer_asn = {}
count_origin_as = {}
plot_peer_asn = [0]*20
plot_peer_asn_above_1000 = [0]*20
plot_origin_as = [0]*20
plot_origin_as_above_1000 = [0]*20
num_of_ipv4 = 0

for k in count_peer_asn:
    k = 0
for k in count_origin_as:
    k = 0

line = f.readline()
if line:
    a = line.split("|")
    start_time = int(float(a[2]))
    if ":" not in a[9]:
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
        if a[7] not in count_peer_asn:
            count_peer_asn[a[7]] = 1
        else:
            count_peer_asn[a[7]] += 1
        if a[12] not in count_origin_as:
            count_origin_as[a[12]] = 1
        else:
            count_origin_as[a[12]] += 1
        num_of_ipv4 +=1 
    line = f.readline()

    


f.close()

diff_peer_asn_num = len(count_peer_asn)
diff_origin_as_num = len(count_origin_as)

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

xlabel = range(0, 20000, 1000)
xlabel2 = range(0, 20000, 1000)
plt.plot(xlabel, plot_peer_asn)
plt.xlabel("peer-asn update number")
plt.ylabel("peer-asn number")
plt.title("20200930-2355 peer asn")
plt.show()
#print(sorted(count_peer_asn.items(), key=lambda x:x[1]))

plt.plot(xlabel2, plot_peer_asn_above_1000)
plt.xlabel("peer-asn update number")
plt.ylabel("peer-asn number")
plt.title("20200930-2355 peer asn (above 1000)")
plt.show()


print("diff_origin_as_num : " + str(diff_origin_as_num))

plt.plot(xlabel, plot_origin_as)
plt.xlabel("origin-as update number")
plt.ylabel("origin-as number")
plt.title("20200930-2355 origin as")
plt.show()
#print(sorted(plot_origin_as.items(), key=lambda x:x[1]))

plt.plot(xlabel2, plot_origin_as_above_1000)
plt.xlabel("origin-as update number")
plt.ylabel("origin-as number")
plt.title("20200930-2355 origin as (above 1000)")
plt.show()

