def number(num1,num2):
    if num1%2 == 0 and num2%2 == 0:
        if num1 < num2:
            return num1
        else:
            return num2
    else:
        if num1 > num2:
            return num1
        else:
            return num2
    
print (number(2,5))