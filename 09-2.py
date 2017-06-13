str2 = "qwertyuiopa"
print(str2)
print(str2[0:7])
print(str2[2::3])
k = int(len(str2))
if (k % 2) == 0:
    print(str2[int((k / 2) - 2):int((k / 2) + 2)])
else:
    print(str2[(int(k/2) - 2):int(k/2)], (str2[(int(k/2) + 1):int(k/2) + 3]), sep='')
#    print('{0} - {1} - {0}'.format(k, str2[(k - 1):k+1]))
#    print('%i - %s' %(k, str2[(k - 1):k+1]))