#讓使用者重複地輸入商品名稱(購買過的東西)及商品價格
#因為要重複輸入，所以用while loop比較合適(不知道會執行多少次用)，比起for loop(固定次數執行)
#因為要對應名稱和價格，所以是二維清單
#二維清單即大火車內有各個小小清單組成

#讀取檔案程式碼
products = []
with open ('products.csv', 'r', encoding= 'utf-8') as f: #讀取也會有亂碼問題，故加上encoding = 'utf-8'來讀取
    for line in f:
        # s = line.strip()split(',')                  # .split(',') 用逗點分割line，遇到逗點就切 # 用.strip( )來除掉換行符號\n #split切割完的結果是清單，存到清單s中
        # name = s[0]
        # price = s[1]
        name, price = line.strip().split(',')         # 切割完分成兩塊，直接把切割完左右兩塊內容分別裝到name和price中，直接簡化前面三行   
        products.append([name, price])                # 有了兩個屬性name和product，把讀到的內容裝進清單products中
print(products)                                       # 確定有讀取成功

while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ') #寫第一個break下面，才不用前面商品不輸入了還再問一次
    #p = [] 小清單        # 較直覺的寫法:先建立小清單p
    #p.append(name)       # 再把兩個屬性加到p中
    #p.append(price)
    #products.append(p)   #最後把小清單p加到大清單products中 #小清單都放到大清單裡面，完成2維清單
    products.append([name, price]) #上面四行簡潔成一行就可以了 #記得裡面要放中括號 #兩個屬性直接建立小清單，放到大清單products中

print(products)               # [['ramen', '100'], ['pasta', '200']]

#清單的索引標籤叫做index
print(products[0][0])    # 先找出大清單中的第0格，再找到小清單中的第0格 #ramen

# Q: 寫出每個商品對應的價格
for p in products:
    print(p[0], '的商品價格為: ', p[1])
    print(p)     #是把每一個小清單拿出來
    print(p[0])  #是把每一個小清單中的第0格拿出來

# Q: 如何把商品和價格儲存到電腦中?

#加法可以做字串的合併，'我的年齡是' + '23' = 我的年齡是23
with open ('products.csv', 'w')  as f:              #有沒有products.csv這個檔案不重要，有的話會覆蓋掉，沒有會自動建立(因為現在是寫入模式) #每一種商品有很多種不同屬性的時候，多會用.csv儲存資料
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') #用.write()寫到檔案內，沒有這行的話還是沒有寫入檔案 # \n是換行符號，寫入多會在最後做換行 #csv檔多是以逗點做區隔，所以要在每個屬性中間用逗點做合併 
#若上面price = int(price) 被寫成整數而非字串時，p[1]要用str()轉成字串，因為p[1]在上面已經改成int(price)了 ，而加法只能字串跟字串或整數跟整數

# Q: 如何在檔案中加入欄位名稱?
#add header #加入程式碼來寫header欄位
with open ('products.csv', 'w', encoding = 'utf-8') as f:  #解決亂碼問題:用encoding編碼轉換 #utf-8 是最廣泛使用的編碼 #寫入和讀取檔案時，都會有編碼問題，可以用encoding= 'utf-8'解決中文字變亂碼的問題
    f.write('商品,價格\n')                                 #在for loop前面先寫入欄位名稱   
    for p in products:                                    #之後再一個一個各寫入一行
        f.write(p[0] + ',' + str(p[1]) + '\n')            #用.write()寫到檔案內  # 加法只能字串跟字串，但p[0],p[1]要用str()轉成字串 #改存成.csv格式 # \n就是換行符號
# 剛剛有說，寫入和讀取都會有編碼問題，即使寫入encoding = 'utf-8'，excel讀取要是沒有使用utf-8，也還是會出現亂碼
#  如何用excel正確使用utf-8編碼導入csv檔
# Ecel導入csv資料:
# 資料 -> 從文字檔 ->選取要匯入的csv檔
# 編碼:選UTF-8
# 分隔符號:選逗點comma   