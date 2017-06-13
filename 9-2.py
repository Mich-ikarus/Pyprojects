str2 = "qwertyuiopa"
print(str2)
# print(str2[0:7])
# print(str2[2::3])
k = int(len(str2))
#print(k)
#print(int((k / 2)))

if (k % 2) == 0:
    print(str2[int((k / 2) - 2):int((k / 2) + 2)])

else:
    k = int(k/2)
    str2[int(k - 1):2]
    print(str2)
    print(k-1)
    print(str2[(k - 1):2])
    s1 = str2[int((k / 2) - 1):2]
    s2 = str2[int((k / 2) + 2):2]