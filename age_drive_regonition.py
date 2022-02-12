age = input("請問你今年幾歲?")
age = int(age)                    #記得要Casting才能=
drive = input("請問你開過車嗎?")
if drive != "有" and drive != "沒有":
    print("只能回答有或沒有喔")     #記得縮排 #被觸發錯誤用
    raise SystemExit              #直接讓程式終止
    #思考:要問到他回答有或沒有的loop要怎麼寫?hint:while loop
if drive == "有":                 #雙層if #記得要冒號
    if age >= 18:                 #記得要冒號
        print("那你應該是合法駕駛") #記得要縮排
    else:  
        print("你違法開車耶")
elif drive == "沒有" or drive == "無":
    if age >= 18:
        print("那你可以去考駕照囉~")