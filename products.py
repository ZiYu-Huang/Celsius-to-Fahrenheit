#先逐區塊設def，再把全部function都收起來
#再依各def區塊決定function要不要設參數和回傳

#讀取檔案
import os
def read_file(filename):     #參數filename沒有'' #插入這行進去後，下面全選插入一個tab縮進去，出現了tab跟空白鍵的混用#加入參數filename
    products = []
    if os.path.isfile(filename): #參數filename沒有''
        print ('yeah!找到檔案了!')
        with open (filename, 'r', encoding= 'utf-8') as f: #參數沒有''
            for line in f:    
                if '商品,價格' in line: 
                    continue                                  
                name, price = line.strip().split(',')          
                products.append([name, price])                
        print(products)                                       
    else:
        print('找不到檔案…')
    return products         #回傳裝著我們讀完的資料 #回傳不用()

#讓使用者輸入
def user_input(products):       #要加上prodcuts這個參數，不然他要伸手去外面拿才知道
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ') 
        products.append([name, price])  
    print(products) 
    return products             #回傳不用()


# 印出所有商品對應的價格
def print_products(products):
    for p in products:
        print(p[0], '的商品價格為: ', p[1]) 
#沒有改變東西也沒有增加什麼，只是印出東西，所以不用回傳，只需要傳遞進去(設參數)


# 寫入檔案並在檔案中加入欄位名稱
def write_file(filename, products):                      #參數filename沒有''
    with open (filename, 'w', encoding = 'utf-8') as f:  #參數filename沒有''
        f.write('商品,價格\n')                                  
        for p in products:                                    
            f.write(p[0] + ',' + str(p[1]) + '\n')
#沒有改變東西也沒有增加什麼，只是寫到檔案，所以不用回傳，只需要傳遞進去(設參數)

products = read_file('products.csv')   #有return的話，function的執行結果就可以存下來開
products = user_input(products)        #又存回products取代它原本的
print_products(products)
write_file('products.csv', products)
# 剛剛有說，寫入和讀取都會有編碼問題，即使寫入encoding = 'utf-8'，excel讀取要是沒有使用utf-8，也還是會出現亂碼
#  如何用excel正確使用utf-8編碼導入csv檔
# Ecel導入csv資料:
# 資料 -> 從文字檔 ->選取要匯入的csv檔
# 編碼:選UTF-8
# 分隔符號:選逗點comma   