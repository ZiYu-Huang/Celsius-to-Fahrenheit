#第二次refactor
#流程:改寫read_file()function
#寫main()function

#理想的function應該"只做一件事"，所以refactor(重構程式)的核心概念，就是把程式碼不斷地改寫，寫成越來越小的function，讓function"盡量"只做一件事。
#程式最好有main()function為程式的進入點


#讀取檔案
#沒有檢查檔案在不在
import os
def read_file(filename): #參數filename沒有''
    products = []
    with open (filename, 'r', encoding= 'utf-8') as f:
            for line in f:    
                if '商品,價格' in line: 
                    continue                                  
                name, price = line.strip().split(',')          
                products.append([name, price])                
            return products   #回傳不用()                  
 
#讓使用者輸入
def user_input(products):       #要加上prodcuts這個參數，不然他要伸手去外面拿才知道
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ') 
        products.append([name, price])  
    print(products) 
    return products            #回傳


# 印出所有商品對應的價格
def print_products(products):
    for p in products:
        print(p[0], '的商品價格為: ', p[1]) 
#沒有改變東西也沒有增加什麼，只是印出東西，所以不用回傳，只需要傳遞進去(設參數)


# 寫入檔案並在檔案中加入欄位名稱
def write_file(filename, products):
    with open (filename, 'w', encoding = 'utf-8') as f:  
        f.write('商品,價格\n')                                  
        for p in products:                                    
            f.write(p[0] + ',' + str(p[1]) + '\n')
#沒有改變東西也沒有增加什麼，只是寫到檔案，所以不用回傳，只需要傳遞進去(設參數)


# if os.path.isfile下面那一區塊不會重複使用，只會檢查一次，就不用寫成function
# 只有反白的這一小段真正在執行程式，沒有這一小段，就什麼也不會印出來，因為上面都只是在定義而已
# 通常在這一種情況，我們會把這主要執行的程式碼，也會寫成function，統一稱為main function()
# 把他們都移進main function
def main():
    filename = 'products.csv' #增加上去，先把products.csv先存成一個變數
    if os.path.isfile('filename'): #檢查檔案在不在
        print ('yeah!找到檔案了!')
        products = read_file('filename')                            
    else:
        print('找不到檔案…')
        
    products = user_input(products)        #又存回products取代它原本的
    print_products(products)
    write_file('products.csv', products)  

main()     # 最下面要寫main()才會進入那一段執行的程式碼，所以呼叫那個main function變成程式執行的進入點了，不執行就什麼也不會發生 # 先進入main function，才會依次進入read_file function, user_input function等等
# 剛剛有說，寫入和讀取都會有編碼問題，即使寫入encoding = 'utf-8'，excel讀取要是沒有使用utf-8，也還是會出現亂碼
#  如何用excel正確使用utf-8編碼導入csv檔
# Ecel導入csv資料:
# 資料 -> 從文字檔 ->選取要匯入的csv檔
# 編碼:選UTF-8
# 分隔符號:選逗點comma   