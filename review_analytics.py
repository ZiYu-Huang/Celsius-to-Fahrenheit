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
print('第一筆留言為:', data[0])
print('檔案讀取完了，總共有', len(data), '筆資料')

# Q:要怎麼知道這一百萬筆留言平均長度?

sum_len = 0
with open('reviews.txt', 'r') as f:
    for d in data:                    # 字串可以當清單求長度
        sum_len += len(d)             # sum_len = sum_len + len(d)
avg = sum_len / len(data)
print('留言平均長度為:', avg, '筆')