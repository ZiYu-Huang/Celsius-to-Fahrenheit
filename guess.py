# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他比答案大/小

import random 
r = random.randint(1, 100)               # 有包含1和100

while True:                              # while要記得小寫
    num = input('請輸入1至100內的數字: ') # 要放在while True底下!放在上面的話回圈會跑不到，不會重複詢問
    num = int(num)                        
    if num == r:                         #記得，要一樣(即等於)時，要用==
        print("終於猜對了!")
        break
    elif num > r:
        print('要再小一點唷~')
    elif num < r:
        print('要再大一點唷~')
