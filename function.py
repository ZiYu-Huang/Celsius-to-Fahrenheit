#function函式/功能，只是在寫定義，它是不會自動執行的，它只是個功能
#def函式名稱():
#    內容
#寫程式時，盡量把程式碼都 "收納" 在function內，好處:讓程式碼有清楚架構 & 增加程式碼的"重複使用性"
# 盡量把程式碼寫成function的好處： 1. 收納，程式碼有較良好/明顯的架構 2. 增加重複使用性 3. 也因為以上的原因，寫成function其實大大的降低了debug(除錯)的時間。 程式出錯時，會依照function的執行流程印出來，告訴你哪個function中執行了哪個 function，最後在哪個function的第幾行當掉，所以我們可以依照這樣有用的資訊，到出錯的function去看為什麼出錯，又因為我們的function有依照良好的中心思想(功能單一/ 簡潔)去寫，所以一下子就可以成功除錯。 
# 寫成function，在除錯時，我們是一小段一小段的看程式碼，看看我們的function有沒有 設計錯誤。 如果程式沒有寫成function，我們會像無頭蒼蠅，一堆東西不知道是在哪裏宣告的， 哪裡改變成什麼，上下上下查找，大幅增加了除錯的時間。 這樣大家應該有所體會了! 所以function算是寫程式裡面非常重要的概念!
# 大致上可以把function視為有四種難度 
# 第一難度最簡單
def wash():           #記得後面要有冒號
    print('加水')
    print('加洗衣精')
    print('旋轉')
wash()                # 使用function，就像是按下按鈕

# 第二難度: 參數parameter 
#parameter(參數)可以想成投幣孔: 當function需要外部資料時，我們就設計投幣孔(參數)，把資料投進去function中
def add(x, y): 
    print(x + y) 
add(3, 4)        # 把3投到x這個參數，把4投到y這個參數
# 術語上，所謂的"投"，是"傳遞"。 
# 所以嚴格術語說法會是，把3傳遞到x參數，把4傳遞到y參數
# 這個"傳遞"也是從英文直翻過來的，英文上都是講"pass in" 就是把東西傳遞(pass in)到function內部的概念。

def wash(dry):            # 設計了一個參數叫做dry，可以投(傳遞)東西進去             
    print('加水')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')
wash(True)                # 使用function，且將True傳遞到dry中，變成if True，就會印出烘衣
wash(False)               # 當function需要外部資料時，我們就設計投幣孔(參數)，把資料投進去function中(讓function伸手出去外面拿東西不好，也就是說，dry = False不要放在def外面)

def say_hi():
    print('hi')
say_hi()

def add(x, y):             # 投東西的時候是自動按照參數的順序
    print(x + y)           # 如果有投幣孔(參數)，那就一定要投東西給他。不投不行，不然執行function運作的時候會當掉

def add(x=1, y=1):         # 參數可以有"預設值"，那就不一定要投給它# 寫參數的時候，等號左右不用空格
    print(x + y)
add()                      # 有預設值就可以不用傳遞給它
add (3, 4)
add (y=5)                  # 投東西給參數的時候可以"明確指定"要投到哪一個參數"