# 假設有一些整數裝在data清單中，你想要一行一行把這些數字寫到test.txt檔案裡，請寫出這樣的程式碼
data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
# 請開始寫"寫入檔案"的程式碼
with open ('test.txt', 'w') as f:
    for d in data:
        f.write(str(d) + '\n')  #記得要用'+'合併