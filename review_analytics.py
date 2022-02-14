# 寫程式碼來讀取留言檔reviews.txt
# 只印出第0筆看看
# 讀取檔案的過程中，每一千筆印出len(data)才知道讀取進度
# 算留言平均長度
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)              #把每一行都加到空清單data裡面
        count += 1                     # count = count + 1
        if count % 1000 == 0:          # '%'是求餘數，也就是count要跟1000去求餘數等於零者 #記得if後面加冒號
            print(len(data))           # 讀取檔案的過程中，每一千筆印出
print('第一筆留言為:', data[0])         # 要寫在for loop外面，寫在裡面的話，他會一直印          
print('檔案讀取完了，總共有', len(data), '筆資料')

# Q:要怎麼知道這一百萬筆留言平均長度?

sum_len = 0
with open('reviews.txt', 'r') as f:
    for d in data:                    # 字串可以當清單求長度
        sum_len += len(d)             # sum_len = sum_len + len(d)
print('留言平均長度為:', sum_len / len(data), '筆')    # 要寫在for loop外面，寫在裡面的話，他會一直印

# Q:要怎麼篩選長度小於一百個字的?*這裡的'字'是指'character'ex.the有三個字

new =[]
with open('reviews.txt', 'r') as f:
    for h in f:                        # 從f這個清單裡面一個一個拿出來叫h，h是一個清單 # 先從for loop一筆一筆讀取資料
        if len(h) < 100:               # 記得後面要加冒號
            new.append(h)
print('一共有', len(new), '筆資料留言') # 要寫在for loop外面，寫在裡面的話，他會一直印 # 不是len(h)
print(new[0])                          # 看看new清單中的第一筆資料


# Q:篩選出有'good'的留言有幾筆
good = []
with open('reviews.txt', 'r') as f:
    for g in f:
        if 'good' in g:               # if後面接是非題 # good是字串記得加''
            good.append(g) 
print('一共有', len(good), '筆留言提到good')
print(good[0])