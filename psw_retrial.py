#password = '123456789'
#讓使用者重複輸入密碼，最多輸入三次
#若正確就印出'登入成功!'，反之則印出'密碼錯誤!還有__次機會!'
password = '123456789'
x = 3
while x > 0 :                    #w記得要小寫
    psw = input('請輸入密碼: ') #這個不能放在while True外面，否則迴圈不會重複要使用者輸入密碼
    if psw == password:
        print('登入成功!')
        break                  #記得對的話要逃出迴圈
    else:
        print('密碼錯誤!')
        x = x - 1              #這行也可以放在while x>0底下那行(即第7行)
        if x > 0:              #這行要放在print前面，不然錯誤機會會顯示錯誤(因為會先print)
            print('還有',x,'次機會!')
        else:
            print('你沒有機會啦!被鎖定了!拜拜~')

        
