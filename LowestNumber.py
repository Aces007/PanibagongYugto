# So, the program will ask you first to input 3 numbers ranging from 0-∞ input three numbers below.
def MgaNumero():
    UnangNumero = input("Provide your first number: ")
    PangalawangNumero = input("Providenow your second number: ")
    PangatloNaman = input("Lastly, your third number: ")
    return UnangNumero, PangalawangNumero, PangatloNaman

# Then, this  
def PangalawangList():
    MgaNumero2 = [FirstNum, SecondNum, ThirdNum] 
    for numbers in MgaNumero2:
        if FirstNum < SecondNum and FirstNum < ThirdNum:
            print("The lowest number is Number 1") 
        elif SecondNum < FirstNum and SecondNum < ThirdNum:
            print("The lowest number is Number 2")
        else:
            print("The lowest number is Number 3") 

FirstNum, SecondNum, ThirdNum = MgaNumero()
PangalawangList()