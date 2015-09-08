#!/usr/bin/Python

import sys

# Taking Command Line Arguments

list1 = sys.argv[1:]
list1 = sorted(list1,reverse = True)
print 'The initial list of books are: ' , list1

x = 0
# Here i take the length of the largest element from the sorted list because that is the number of elements(1d lists) that i would have to form
a = list1[0] 
final_right_list = []

#This is the function where i rearrange the sets of 5 and 4 into 4 and 4
def special_case(x,y,converted_list):
    element_removed = converted_list[x].pop()
    converted_list[x].append(0)
    converted_list[y][4] = element_removed
    return converted_list

def price_calc(final_right_list):
    count_right_0 = [row.count(0) for row in final_right_list]
    price = 0
    
    for k in range(len(count_right_0)):
        if(count_right_0[k] == 0):
            price = ((8*5) - (float(25)/100 * 8*5)) + price
        if(count_right_0[k] == 1):
            price = ((8*4) - ((float(20)/100) * (8*4))) + price     
        if(count_right_0[k] == 2):
            price = ((8*3) - ((float(10)/100) * (8*3))) + price
        if(count_right_0[k] == 3):
            price = ((8*2) - ((float(5)/100) * (8*2))) + price
        if(count_right_0[k] == 4):
            price = 8 + price
        
    return price

#Create a 2d list of a*5
final_list = [[0 for y in range(5)] for y in range(int(a))] 

for i in range(len(list1)):
    
    for j in range(int(list1[x])):
        final_list[j][i] = x + 1
    if(x < len(list1)-1):
        x = x+1

         
print "The final set formations are:", final_list

#Here i count the number of zeroes so that i can have an understanding of the number 
#of elements in each 1d list based on which the price is decided.
count_0 = [row.count(0) for row in final_list]

#Here the indices of 2 and 0 zeroes are found to see how many 1d lists need to be adjusted to get the maximum discount.
indices_0 = [g for g, h in enumerate(count_0) if h == 0]
indices_2 = [g for g, h in enumerate(count_0) if h == 2]

if(len(indices_0) > 0 and len(indices_2) > 0):
    if(len(indices_0) > len(indices_2)):
        for ind in range(len(indices_2)):
            final_right_list = special_case(indices_0[ind], indices_2[ind], final_list)
        print "The final set formations are:",final_right_list
        print "The maximum discounted price is:" ,price_calc(final_right_list), "Euros"
        
    if(len(indices_0) == len(indices_2)):
        for ind in range(len(indices_2)):
            final_right_list = special_case(indices_0[ind], indices_2[ind], final_list)
        print "The final set formations are:", final_right_list
        print "The maximum discounted price is:" ,price_calc(final_right_list), "Euros"

    if(len(indices_0) < len(indices_2)):
        for ind in range(len(indices_0)):
            final_right_list = special_case(indices_0[ind], indices_2[ind], final_list)
        print "The final set formations are:", final_right_list
        print "The maximum discounted price is:" ,price_calc(final_right_list), "Euros"
else:
    print "The maximum discounted price is:" ,price_calc(final_list), "Euros" 

    
