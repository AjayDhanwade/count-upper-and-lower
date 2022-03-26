#count uppercase and lowercase charecters

def count_letters(lis):
    countu=0
    countl=0
    for i in lis:
        if i.isupper():
            countu+=1
        elif i.islower():
            countl+=1
    print("No of uppercase charecters :",countu)
    print("No of lowercase charecters :",countl)
    

string="The quick Brow Fox"
list1=(string)
count_letters(list1)