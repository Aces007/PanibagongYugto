# So, the program will ask you first to input 3 numbers ranging from 0-∞ input three numbers below.
def MgaNumero():
    UnangNumero = input("Provide your first number: ")
    PangalawangNumero = input("Provide now your second number: ")
    PangatloNaman = input("Lastly, your third number: ")
    return UnangNumero, PangalawangNumero, PangatloNaman


# Then, this function will evaluate your provided numbers, then it will show the smallest number.
def PangalawangList():
    MgaNumero2 = [FirstNum, SecondNum, ThirdNum] 
    for numbers in MgaNumero2:
        if FirstNum < SecondNum and FirstNum < ThirdNum:
            print("The lowest number is Number 1") 
        elif SecondNum < FirstNum and SecondNum < ThirdNum:
            print("The lowest number is Number 2")
        else:
            print("The lowest number is Number 3") 


# This variable pertains for the first function where you are required to provide three numbers in order for the program to work.
FirstNum, SecondNum, ThirdNum = MgaNumero()


# This variable then will, post-evaluation shows your smallest number out of three numbers. 
PangalawangList()