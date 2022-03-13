#Made by Ruben Bartelet in 3-2022

def get_symbol_list():#adds symbols to numbers with value above 9 (F in base 16 is 15). In the text file that I made I justed the nationally accepted (in base 16) uppercase letters from A to Z from 10 to 35; for 36 to 61 lowercase letters (a to z); for 62 to 75 lowercase greek letters (with Sampi and no Alpha, Bèta, Epsilon, Zèta, Èta, Jota, Kappa, Mu, Nu, Omikron, Rho, Tau, Ypsilon and Chi because they looked to similair to some latin letters) and for 76 to 100 the lowercase greek letters (with Sampi and without Nu and Omikron).   
    symbols_file = open("symbols_number_systems.txt", "r", encoding="utf8")
    symbols_list = symbols_file.read().split("\n")
    symbols_file.close()
    symbols_list2 = []
    for d in range(0, len(symbols_list)-2):#the -2 is for the spaces add the end of the file
        temp = symbols_list[d]
        symbols_list2.append(temp[-1])
    return symbols_list2

def check_range(Input_number, BaseOutputNumber):#checks how many times the loop in the convert function must be used
    a = 0 
    while True:
        if Input_number < BaseOutputNumber**(a):
            return(a-1) 
        else: a += 1

def convert(Input_number, Output, BaseOutputNumber,symbols_list):#converts the base 10 number into the base number that is chosen
    range_ = check_range(Input_number, BaseOutputNumber)
    for b in range(0,range_+1):#how this method of converting works is as following: (I'll demonstrate it with base 10 to base 2) if we have the number 40 and we wanted to make it base 2 we first need to subtract 32 (2^5) (this frist number determined bij the range) and at a 1 in the sixth (5+1) place of the base 2 number. Then we need to check if 16 (2^4) can be removed from it (without making a negative number), it cant so we add a 0 (at the fifth (4+1) position of the number). Then we check 8 (2^3), it can be removed so we add a 1 (at the fourth (3+1) position of the number). Than 4,2,1. And the number we get is 101000. This is the base 2 number of 40.  
        bigNumber = BaseOutputNumber**(abs(b-range_))
        num = 0
        if Input_number >= bigNumber:
            for c in range(BaseOutputNumber):
                if Input_number >= bigNumber:
                        Input_number -= bigNumber
                        num += 1
            Output += str(symbols_list[num])
        else: Output += '0'
    return Output

def base_number(number, BaseInputNumber, symbols_list):#makes the number base 10 because python uses base 10
    range_2 = len(number)
    base_10_number = 0
    for e in range(0,range_2):
        value = symbols_list.index(number[-1])
        base_10_number += value*(BaseInputNumber**e)
        number = number[:-1]
    return base_10_number

def check_base_range(base, symbols_list):
    if base > len(symbols_list):# if a higher base is chosen that is supported by the text file. (-2 is for the spaces at the end)
        print("The text file doesn't support this number base. Chose a lower number base.") 
        main(symbols_list)

def main(symbols_list): # the main function, it handles the input and output. 
    BaseInputNumber = int(input('Input number based system: '))
    check_base_range(BaseInputNumber, symbols_list)
    BaseOutputNumber = int(input('Output number based system: '))
    check_base_range(BaseOutputNumber, symbols_list)
    Input_number = input('Base ' + str(BaseInputNumber) + ' Number: ' )
    
    for f in range(BaseInputNumber,len(symbols_list)):#checks if the symbol used is supported by the number system
        if symbols_list[f] in str(Input_number):
            print('You used the wrong symbol for this number system.')
            main(symbols_list)
        else: pass
    
    Input_number = base_number(Input_number, BaseInputNumber, symbols_list)#makes it base 10
    Output = ''
    
    print('Base ' + str(BaseOutputNumber) +  ' Number: '+ str(convert(Input_number,Output, BaseOutputNumber,symbols_list)))
    main(symbols_list)

main(get_symbol_list())

#69