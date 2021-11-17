# This will require you to input your curent age since the beginning of 2021. 
IlangTaonKaNa = int(input("How old are you?:"))


# Then with this if-elif statements, my program will present you what stage in life you're currently in.
if IlangTaonKaNa >= 0 and  IlangTaonKaNa <= 12:
    print("Kid")
elif IlangTaonKaNa >= 13 and IlangTaonKaNa <= 17:
    print("Teen")
elif IlangTaonKaNa == 18:
    print("Debut")    
elif IlangTaonKaNa >= 19:
    print("Adult")
    