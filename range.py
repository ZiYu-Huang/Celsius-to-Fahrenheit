# python內建清單產生器:range
# range(結尾值):自動從0開始產生，所以結尾值不包含
# 通常只是為了拿來重複執行固定次數
# 可以把i在for loop內容中印出來，就知道執行到第幾回

range(3)   #[0, 1, 2] #自動從0開始，結尾值不包含，所以只到2

for i in range(3):             #把清單range(3)中的東西一個一個拿出來，每一個稱呼為i
    print(i)
for i in range(3):
    print('hi')                #hi會出現三次# 大部分寫這種for i in range的for loop只是為了拿來重複執行固定次數

import random   
for i in range(3):
    r = random.randint(1, 1000)
    print(r)                           

for i in range(5):
    r = random.randint(1, 1000)
    print('這是第', i + 1, '次產生隨機變數: ', r) #為了從1開始，所以要i+1

# 所以要把東西執行x次，就用for i in range(x)

# range 的另外兩種不常見寫法
# range(開始值，結尾值)
# range(開始值，結尾值，遞增值)
# 開始值有包含，結束值不包含

range(2, 5)      # [2, 3, 4]
range(3, 8, 2)   # [3, 5, 7]
range(10, 3, -2) # [10, 8, 6, 4]