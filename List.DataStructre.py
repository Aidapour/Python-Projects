#!/usr/bin/env python3.9
# 1.Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

from operator import length_hint


exp = [2200, 2350,2600,2130,2190]
# 1. In Feb, how many dollars you spent extra compare to January?

# extra_money = list [1] - list[0]
# print ( int(extra_money))

# 2. Find out your total expense in first quarter (first three months) of the year.

print("total expense first 3Q : ",  exp[0]+exp[1]+exp[2])

#beginner code for . fnd out if you spent exactly 2000 dollars in any month
for i in range(len(exp)) :
    if i == 2000 :
        print ("true")
    else:
        print ("more than 2000")
#pro code for same above question :       
print ("is there any expense 2000$?", 2000 in exp)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print ("June month expense is : " , exp [5])

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3]= exp[3]-200
print ("April correction after 200 $ refund:" , exp )


#next question : You have a list of your favourite marvel super heros.
 
heros=['spider man','thor','hulk','iron man','captain america']

print( 'the lenght of the heros are :' , len(heros))

# Add 'black panther' at the end of this list
heros.append( "black panther")
print ("new movie is included : " , heros )

# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'

heros.remove("black panther")
heros.insert(3, "black panther")
print (heros)

# #4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.

heros [1:3] = ["doctor strangers"]
print (heros)

# 5. Sort the list in alphabetical order
heros.sort()
print(heros)

#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max_number= int( input ("what do you think it is the max number : "))
odd_numbers = []
for i in range (1,max_number):
    if i % 2 ==1:
        odd_numbers.append(i)

print (odd_numbers)

#Create a list of all even numbers between 0 and a max number. Max number is something you need to take from a user using input() function
even_numbers = []
for i in range (0, max_number):
    if i % 2 ==0:
        even_numbers.append(i)
print (even_numbers)
