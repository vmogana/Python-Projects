import math

# #----------------------------------------#
# Question 6
# Level 2
#
# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
#
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input.

def FormulaCalc():
    my_inputs=input("please input numbers separated by commas for the formula calculation :")
    my_data=my_inputs.split(',')

    C=50.
    H= 30.
    if len(my_data) == 1:
        print(round(math.sqrt((int(my_data[0])*2*C/H))))

    else:
        my_data1=filter(lambda x: x!=',',my_data)
        my_output= map(lambda x:math.sqrt((int(x)*2*C/H)  ),my_data1 )

        flag=1
        for x in my_output:
            if flag == 1:
                print(round(x),end="")
                flag=0
            else:
                print(",",round(x),end="")

# #----------------------------------------#
# Question 7
# Level 2
#
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,��Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

def Two_D_Array():
    my_input=input("\nplease input two numbers followed by comma for 2D array ")
    my_data=my_input.split(',')
    my_ooo=[[i*j for j in range(int(my_data[1]))] for i in range(int(my_data[0]))]
    print(my_ooo)

    #my_out=[]
    #my_output=[]
    # for x in range(int(my_data[0])):
    #     my_out=[]
    #     for y in range(int(my_data[1])):
    #         my_out.append(x*y)
    #     my_output.append(my_out)
    # print(my_output)


# #----------------------------------------#
# Question 8
# Level 2
#
# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


def WordSequence():
    my_sequence=input("Please enter two or more words sequences separated by commas : ")
    my_words=my_sequence.split(',')
    flag=1
    for x in sorted(my_words):
            if flag== 1:
                print(x,end='')
                flag =0
            else:
                print(',',x,end='')

# #----------------------------------------#
# Question 9
# Level 2
#
# Question��
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
def LinesSequence():
    print("Please enter the lines for capitalization and ending by a  blank line for termination ")
    my_lines=[]
    while True:
        my_line=input()
        if my_line:
            my_lines.append(my_line.upper())
        else:
            break
    for l in my_lines:
        print(l)
# #----------------------------------------#
# Question 10
# Level 2
#
# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.
def SortandRemoveDup():
    my_lines=input("Please enter sequence of whitespace separated words   ")
    my_words=my_lines.split(" ")
    my_word= set(my_words)
    for w in sorted(my_word):
        print(w,end=' ')
# #----------------------------------------#
# Question 11
# Level 2
#
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def BinaryDiv():
    my_inputs=input("Please enter four digit binary numbers separated by commas :")
    my_data=my_inputs.split(',')
    flag = 1
    my_deci=[]
    for x in my_data:
        counter= len(x)
        count= counter-1
        deci = 0
        for i in range(counter):
            deci= deci+ (2**count * int(x[i]))
            count = count-1
        if deci % 5 == 0:
                if flag == 1:
                    print(x, end='')
                    flag = 0
                else:
                    print(',', x, end='')

#
# #----------------------------------------#
# Question 12
# Level 2
#
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
def EvenPrinting():
    my_inputs=eval(input("please specify the start and end numbers for printing all even numbers in between "))
    my_list=list(my_inputs)
    my_data=[]
    for x in my_list:
        if x!= ',':
            my_data.append(x)

    flag = 1
    for x in range(my_data[0],(my_data[1]+1)):
        if x%2 == 0:
            if flag ==1:
                print(x,end="")
                flag =0
            else:
                print(",",x,end="")

# #----------------------------------------#
# Question 13
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def RecognizeLettersDigits():
    my_inputs=(input("Please enter a sentence  :"))
    my_letters = 0
    my_digits=0
    for x in my_inputs:
        if x.isalpha():
            my_letters +=1
        else:
            if x in ['0','1','2','3','4','5','6','7','8','9']:
                my_digits+=1
    print("LETTERS  ",my_letters)
    print("DIGITS   ",my_digits)

# #----------------------------------------#
# Question 14
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
def RecognizeUpperLower():
    my_inputs=(input("Please enter a sentence with upper and lower case :"))
    my_upper = 0
    my_lower=0
    for x in my_inputs:
        if x.isupper():
            my_upper +=1
        else:
            if x.islower():
                my_lower+=1
    print("UPPER CASE  ",my_upper)
    print("LOWER CASE   ",my_lower)
# #----------------------------------------#
# Question 15
# Level 2
#
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
def AplusAAplusAAAplusOn():
    my_input=input("\nPlease give a digit for computing a+aa+aaa+aaaa :")
    my_result=0
    for x in range(1,5):
        my_result = my_result + eval(my_input * x)
    print (my_result)
# #----------------------------------------#
# Question 16
# Level 2
#
# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
def SquareOfOddNumbers():
    my_inputs=eval(input("Please enter the number sequence :  "))
    my_data=[x for x in my_inputs if x!=',']
    my_output=[x*x for x in my_data if x%2 != 0]
    if len(my_output) == 1:
        print(my_output)
        return
    flag =1
    for x in my_output:
        if flag == 1:
            print(x, end='')
            flag = 0
        else:
            print(',', x, end='')

# Question 17
# Level 2
#
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# ��
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
def NetAmount():
    print("please enter the Deposit and withdrawal transaction in the following format D # and W # :")
    my_inputs=[]
    my_withdrawal=0
    my_deposit=0
    while True:
        my_inputs=input().split()
        if (my_inputs):

            if 'W' in my_inputs:
                my_withdrawal+= int(my_inputs[1])
                continue
            if 'D' in my_inputs:
                my_deposit+= int(my_inputs[1])
                continue
            else:
                print("Wrong formatt")
                break
        else:
            print(my_deposit-my_withdrawal)
            break




def main():
    print("Formula calculation")

    print("------------------")
    FormulaCalc()
    print("\nTwo D Array")
    print("-----------")
    Two_D_Array()
    print("Sort words Sequence")
    print("-------------")
    WordSequence()
    print("\nTo print Sequence of lines in upper case")
    print("---------------------------------------")
    LinesSequence()
    print("\n Sort and removing dupicates in sentence")
    print("----------------------------------------")
    SortandRemoveDup()
    print("\nBinary number division")
    print("---------------------")
    print("Binary divisin")
    print("--------------")
    BinaryDiv()
    print("\nEven number printing")
    print("---------------------")
    EvenPrinting()
    print("\nRecognise Letters and Digits")
    print("----------------------------")
    RecognizeLettersDigits()
    print("\nRecognise Upper case and Lower Case")
    print("------------------------------------")
    RecognizeUpperLower()
    print("\nCompute a+aa+aaa+aaaa")
    print("---------------------")
    AplusAAplusAAAplusOn()
    print("\nSquare of Odd numbers")
    print("---------------------")
    SquareOfOddNumbers()
    print("Calculating Net Amount")
    print("-------------------")
    NetAmount()

#if __name__ == '__main__':
#    main()

