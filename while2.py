while True:
    name = input('請輸入名字: ') #while True下面都縮排
    if name == 'q':             #因為input存成字串，故要==""字串模式
        break
    else:                       #這行沒寫也沒關係
        print('想離開請回答q')
