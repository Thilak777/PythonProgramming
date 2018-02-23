num_array = list()
g=0
num =int(input("Enter no of elements :"))
print ('Enter numbers : ')
for i in range(int(num)):
    n = int(input("num :"))
    num_array.append(int(n))
print ('ARRAY: ', num_array)
k=int(input())
for i in range(0,k):
   g=g+num_array[i]
print(g)    
    
