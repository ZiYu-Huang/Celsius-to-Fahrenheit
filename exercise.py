# 假設有一些整數裝在data清單中，你想要一行一行把這些數字寫到test.txt檔案裡，請寫出這樣的程式碼
data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
# 請開始寫"寫入檔案"的程式碼
with open ('test.txt', 'w') as f:
    for d in data:
        f.write(str(d) + '\n')  #記得要用'+'合併

#Quiz

def add(x, y):
    print(1, 6)
# 不會印
#因為這只是function的定義，沒有去呼叫（執行）它，寫上 add(1, 6)才去執行它


def add(x, y)
    print(x + y)
add(1, 1) 
# 不會印
# 第一行最後面少了一個冒號，正確的話應該印出2


def hello(x=1, y):
    print(x, y)
 
hello(3, 4)
# 不會印
#這個比較特殊，特別注意，不會印的原因是因為程式會出錯，python規定參數的部分，"沒預設值的" 一定要在"有預設值的" 的前面，所以上面這個程式不行運作，請看下一題


def hello(x, y=1):
    print(x + y)
 
hello(3, 4)
# 印出7
# 現在這樣就沒錯了，有預設值的必須放在最後，先把全部沒有預設值的參數都寫完，才可以寫有預設值的。（x沒有預設值, y有預設值)
# 雖然有預設值，但有投東西給它，所以不管預設值

def crazy(x, y=3, z=2):
    return x * 2 + y * 3 + z
 
crazy(2)
crazy(3, 1)
crazy(3, 2, 0)

#  不會印出東西
# 程式碼中完全沒有print ，function只有把算完的結果return出來而已，我們看下一題，我把print補上…



def crazy(x, y=3, z=2):
    return x * 2 + y * 3 + z
 
print(crazy(2))
print(crazy(3, 1))
print(crazy(3, 2, 0))

# 第一個印出15因為 x=2, y=3, z=2；第二個印出11因為x=3, y=1, z=2(z沒有投東西，所以用預設值)；第三個x=3, y= 2, z=3 (這個很簡單，三個都有投東西)



def can_vote(age):
    if age >= 18:
        return True
    else:
        return False
 
a = can_vote(20)
print(a)
# 印出20
#其實這題只是讓你們看看這種function的寫法，這種也很常見。

def check_mood(color='紅'):
    mood = '好心情'
    if color == '藍':
        mood = '心情不好'
    return mood
 
print(check_mood())
print(check_mood('藍'))
# 印出好心情和心情不好
# 主要讓你們見識function的各種寫法
# 第一個印好心情因為沒有投東西，所以color用預設值，所以mood就維持好心情，沒有進去if的裡面去改變。
