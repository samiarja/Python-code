import time
start = time.time()
timecount = time.time() - start

#method 1: input user
n = int(input("Enter the number of elements to be inserted:"))
array=[]
for i in range(n):
    enter_elements = int(input("Enter elements:"))
    array.append(enter_elements)
    count = sum(array)
    average = count/n
print("Average array for 1st method is: {}".format(average))
    
#method 2: OOP
given_list=[5,5,5,5]
def get_average(given_list):
    n=len(given_list)
    count=sum(given_list)
    average = count/n
    return average
print("Average array for 2nd method is: {}".format(get_average(given_list)))
print(timecount)
