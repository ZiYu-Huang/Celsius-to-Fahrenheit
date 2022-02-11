#while true會強迫一定要進去，所以一定要搭配break
#讓使用者一直輸入，告訴她想要什麼時候離開
#用while = True的方式，要打break中斷
#Ctrl +C鍵盤阻斷程式運行
while True:                       #True一定要T大寫
    mode = input("請輸入遊戲模式:")
    if mode == "q":                #因為input存成字串，故要==""字串模式(當然也可以把mode轉成數字)
        print("已離開遊戲")         
        break
    elif mode == "1":
        print('啟動模式一')
    elif mode == '2':
        print('啟動模式二')
    else:
        print('只能輸入q/1/2')