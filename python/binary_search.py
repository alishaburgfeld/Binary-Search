import random

# values = random.sample(list(range(1,10000)),10)
# print(values)
values=[1,2,3,4,5,6,7,8,9,10]
def binary_search(values,target,low=0,high=len(values)):
    values.sort()
    mid= round((low + high) /2)
    print(f"low and high: {low}, {high}, {values[low:high]} ,middle  {mid}, value at index middle{values[mid]}")
    # print(values[mid], "middle")
    if target == values[mid]:
        return mid
    
    elif len(values[low:high]) == 1:
        return -1
    elif target < values[mid]:
        return binary_search(values,target,low,mid)
    elif target > values[mid]:
        return binary_search(values,target,mid+1,high)

print(binary_search(values,8))
# values.sort() # We now have a values list of 1000 unique values between 1 and 10,000

# binary_search(537, values) # this returns the index of 537 in values if it exists and -1 if it doesn't exist