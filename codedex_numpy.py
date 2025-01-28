import numpy as np
print(np.__version__)

#numpy array
rent1=np.array([1400,2399,1200,2333])
print(rent1)

electric_bill = np.array([24.33, 22.99, 50.99, 31.99, 22.99, 23.44])
gas_bill = np.array([34.55, 23.22, 23.44, 44.55, 33.22, 33.12])
wifi_bill = np.array([34.99, 34.99, 34.99, 34.99, 34.99, 34.99])

#indexing 
coffee=np.array([3,2,3,8,9])
print(coffee[0])
print(coffee[1])
print(coffee[2])
print(coffee[3])
print(coffee[4])

#slicing
coffee1=np.array([2,9,8,87,65,23])
print(coffee1[:])
print(coffee1[2:])
print(coffee1[-2:])
print(coffee1[-4:-1])

#2D array
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)

arr3=np.array([
    [1,2,3],
    [4,5,6],
    [9,8,7]
])
print(arr3)
print("index0",arr3[0])
print("index1",arr3[1])
print("index2",arr3[2])

print("index0",arr3[0][2])
print("index1",arr3[1][1])
print("index3",arr3[2][0])

#example
seating_plan=np.array([
    [1,3,4],
    [2,3,4],
    [9,8,7]
])

#student example
grades=np.array([
  [98, 98, 90, 84, 93, 73, 80],        
  [93, 95, 75, 90, 89, 84, 76],                
  [90, 89, 88, 84, 90, 67, 72],               
  [89, 84, 69, 74, 84, 70, 72]     
])

#average
egg_carton1 = np.array([
  [0.89, 0.90, 0.83, 0.89, 0.97, 0.98], 
  [0.95, 0.95, 0.89, 0.95, 0.23, 0.99]
])

egg_carton2 = np.array([
  [0.89, 0.95, 0.84, 0.92, 0.94, 0.93], 
  [0.93, 0.95, 0.02, 0.03, 0.23, 0.99]
])

egg_carton3 = np.array([
  [0.83, 0.95, 0.89, 0.54, 0.37, 0.92], 
  [0.98, 0.99, 0.19, 0.23, 0.89, 0.91]
])
average1=np.mean(egg_carton1)
average2=np.mean(egg_carton2)
print(average1)
print(average2) 

#dear data
sleep=np.array([
    [6.0,9.0,4.6,8.9,0.0,7.8],
    [8.9,7.8,6.7,5.6,4.5,3.4],
    [5.6,7.8,9.0,8.9,7.8,6.7]
])

coffee=np.array([
    [1,2,3,4,5,6,7],
    [3,4,5,6,7,8,9],
    [4,5,6,7,8,9,10]
])

exercise=np.array([
    [8,7,45,32,2,1,6],
    [3,4,5,6,7,8,9],
    [2,3,4,5,6,7,8]
])

average1=np.mean(sleep)
average2=np.mean(coffee)
average3=np.mean(exercise)
print("My sleep avearge is " +str(round(average1,2))+"hours.")
print("My coffee average is "+str(round(average2,2))+"cups.")
print("My exercise average is "+str(round(average3,2))+"minutes.")

#operators
order=np.array([1,2,3,4,5])
print(order+2)
print(order-2)
print(order*2)
print(order[1]/2)
print(order%2)

#Numpy functions
temperatures = np.array([[50, 51, 54, 59, 59, 53, 54, 51],
                         [45, 50, 38, 44, 40, 46, 43, 39],
                         [29, 31, 35, 31, 34, 30, 29, 28],
                         [10, 15, 20, 14, 10, 15, 10, 10]])

print("minimum",np.min(temperatures))
print("maximum",np.max(temperatures))
print("sum",np.sum(temperatures))
print("average",np.average(temperatures))

#axis
temperatures=np.array([[50,34,87,98,2,34,45,98],
                      [23,45,67,89,23,45,67,89],
                      [12,34,56,78,12,34,56,78],
                      [23,45,67,89,23,45,67,89]
                      ])
print("sum of each row",np.sum(temperatures,axis=1))
print("min of each column",np.min(temperatures,axis=0))

#.shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) 
print("shape of array",arr.shape)

#.reshape
arr_1=np.array([1,3,4,5,5,6,2,1])
new_arr=arr_1.reshape(2,4)
print(new_arr)

#.arange
arr_2=np.arange(10)
print(arr_2)

arr_3=np.arange(1,10,3)
print(arr_3)

#problem
passengers = np.array([
   [1, 0, 3, 22],
   [2, 1, 1, 38],
   [3, 1, 3, 26],
   [4, 1, 1, 35],
   [5, 0, 3, 35],
   [6, 0, 3, 18],
   [7, 0, 1, 54],
   [8, 0, 3, 2],
   [9, 1, 3, 27],
  [10, 1, 2, 14],
  [11, 1, 3, 4],
  [12, 1, 1, 58],
  [13, 0, 3, 20],
  [14, 0, 3, 39],
  [15, 0, 3, 14],
  [16, 1, 2, 55],
  [17, 0, 3, 2],
  [18, 1, 2, 12],
  [19, 0, 3, 31],
  [20, 1, 3, 8],
  [21, 0, 2, 35],
  [22, 1, 2, 34],
  [23, 1, 3, 15],
  [24, 1, 1, 28],
  [25, 0, 3, 8],
  [26, 1, 3, 38],
  [27, 0, 3, 2],
  [28, 0, 1, 1],
  [29, 1, 3, 5],
  [30, 0, 3, 18],
  [31, 0, 1, 40],
  [32, 1, 1, 70],
  [33, 1, 3, 33],
  [34, 0, 2, 66],
  [35, 0, 1, 28],
  [36, 0, 1, 42],
  [37, 1, 3, 5],
  [38, 0, 3, 18],
  [39, 0, 3, 18],
  [40, 1, 3, 14],
  [41, 0, 3, 40],
  [42, 0, 2, 27],
  [43, 0, 3, 29],
  [44, 1, 2, 0],
  [45, 1, 3, 19],
  [46, 0, 3, 33],
  [47, 0, 3, 14],
  [48, 1, 3, 22],
  [49, 0, 3, 41],
  [50, 0, 3, 18]
])
print("shape of an passengers array",passengers.shape)
print("the average age of passengers",np.average(passengers,axis=0)[3])
print(passengers.dtype)