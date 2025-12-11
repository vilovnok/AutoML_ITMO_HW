import asyncio
import time


value = 0

# async task_one():
#     print('Task 1: начало') 
#     global value
#     await asyncio.sleep(5)
#     value += 5
#     print('Task 1: ', value) 
#     print('Task 1: конец') 


# async task_two():
#     print('Task 2: начало') 
#     await global value
#     asyncio.sleep(2)
#     value -= 10
#     print('Task 2: ', value) 
#     print('Task 2: конец') 

# async task_three():
#     print('Task 3: начало') 
#     global value
#     await asyncio.sleep(2)
#     value += 5
#     print('Task 3: ', value) 
#     print('Task 3: конец') 


# async main():

value = 0
def main(x: int):
    return value


arr1 = [0,0,0]
arr2 = [3,2,1]

# arr1 = [None, None, None]

for a, b in zip(arr1, arr2):
    print(a,b)

print(list(zip(arr2, arr1))[0][0])


# a = list(filter(lambda x: 1, arr1))

# print(a)


