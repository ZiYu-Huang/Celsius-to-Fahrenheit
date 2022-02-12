age = input("請問你今年幾歲?")
age = int(age)                    
while True:                         #True記得要大寫#強迫一定會進入迴圈
    drive = input("請問你開過車嗎?") #記得要indention縮排
    if drive == "有":                 
        if age >= 18:                 
            print("那你應該是合法駕駛") 
            break                      #逃出迴圈
        else:  
            print("你違法開車耶")
            break
    elif drive == "沒有" or drive == "無":
        if age >= 18:
            print("那你可以去考駕照囉~")
            break
        else:
            print("再等等就能去考駕照囉~")
            break
    else:
        print("只能回答有或沒有喔") 
