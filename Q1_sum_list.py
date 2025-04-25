#This function will get the sum of all the elements contained in the (list).
def sum_list(list):
    total=0
    for num in list:
        total=total+num

    return total

#now I made the list to get the sum printed.
print(sum_list([1,2,3,4,5]))