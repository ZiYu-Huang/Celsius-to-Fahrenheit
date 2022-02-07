weight = input("請輸入您的體重(kg)")
height = input("請輸入您的身高(cm)")
weight = float(weight)
height = float(height)
height = height/ 100               #要記得把公分轉成公尺
BMI = weight/height/height
print("您的BMI為", BMI)
if BMI < 18.5 :                    #要記得if最後要加上冒號
    print("體重過輕 Underweight.")  # print前記得要空四格
elif BMI >= 18.5 and BMI < 24 :             
    print("正常範圍 Healthy Weight") #and 後面的BMI還是要加
elif BMI >= 24 and BMI < 27 :       #elif最後面還是要加上冒號
    print("過重 Overweight.")
elif BMI >= 27 and BMI < 30 :
    print("輕度肥胖 Slightly Obesity.")
elif BMI >=30 and BMI <35 :
    print("中度肥胖 Obesity")
else :                             #else最後面還是要加上冒號，print一樣要打在下一行 
    print("重度肥胖 Severe Obesity")    