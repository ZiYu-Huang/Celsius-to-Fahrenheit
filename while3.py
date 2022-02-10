#password = '123456789'
#讓使用者重複輸入密碼，最多輸入三次
#若正確就印出'登入成功!'，反之則印出'密碼錯誤!還有__次機會!'
password = '123456789'
x = 3
while True :                    #w記得要小寫
    psw = input('請輸入密碼: ') #這個不能放在while True外面，否則迴圈不會重複要使用者輸入密碼
    if psw == password:
        print('登入成功')
        break                  #記得對的話要逃出迴圈
    else:
        print('密碼錯誤!還有',x,'次機會!')
        x = x - 1
        if x == 0:
            print('已被鎖定，無剩餘機會')
            break
