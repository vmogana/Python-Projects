

def Divisibleby7andNotMultipleof5():
    for x in range (2000,3201):
        if x % 7 == 0 and x % 5 !=0:
            print(x, end=',')
def Factorial():
    Fact = 1
    Number = eval(input("\nInput the number for finding Factorial : "))
    Numb = Number + 1
    for factor in range(1,Numb,1):
        Fact = factor * Fact
    print ("\nFactorial of ", Number, " is ", Fact)

def GenerateDict():
    my_dict={}
    my_elements=eval(input("Please enter the no of dict elements to be generated : "))
    for x in range (1,my_elements+1):
        my_dict[x]=x*x
    print (my_dict)

def main():
    print("Divisibleby7andNotMultipleof5")
    print("-----------------------------")
    Divisibleby7andNotMultipleof5()
    print("\n\nFactorial")
    print("---------")
    Factorial()
    print("\n\nGenerating dictionary elemnts of form x : x*x ")
    print("----------------------------------------------")
    GenerateDict()
    print("Generate  List and Tuple from seg of numbers")
    print("--------------------------------------------")
    GenerateListTuple()

def GenerateListTuple():
    my_inputs= input("Please enter the numbers separated by commas :")
    my_list=[]
    my_list1=[]
    my_list = list(my_inputs)
    for x in my_list:
        if x!= ',':
            my_list1.append(x)
    print("\n",my_list1)
    print("\n",tuple(my_list1))
if __name__ =='__main__':
    main()