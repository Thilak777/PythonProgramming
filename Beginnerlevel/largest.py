num_array = list()
num =input("Enter no of elements :")
print ('Enter numbers : ')
for i in range(int(num)):
    n = input("num :")
    num_array.append(int(n))
print ('ARRAY: ',num_array)
if (num_array[0]>num_array[1]and num_array[0]>num_array[2] ):
    print (num_array[0])
elif (num_array[1]>num_array[0]and num_array[1]>num_array[2] ):
    print (num_array[1])
else:
    print (num_array[2])
