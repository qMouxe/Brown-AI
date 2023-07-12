unit = str(input("Input unit: minutes = m, hours = h "))
num = float(input("Any number"))
temp = 0
if unit == "h":
    temp = num
    num = num*60
    print(str(temp) +  " hours is equal to " + str(num) + " minutes")
elif unit == "m":
    temp = num
    num = num/60
    print(str(temp) + " minutes is equal to " + str(num) + " hours")

    

    
