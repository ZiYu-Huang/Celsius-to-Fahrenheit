# 寫一個檔案來讀取
# 介紹讀取檔案的程式碼
# 把讀到的資料裝進清單
# strip()除掉換行符號
# 解釋with
data = []                           # 此行是為了證明有換行符號用的，用個空清單
with open('food.txt', 'r') as f:    # openr是read讀取模式;w是write寫入模式;with打開並在離開with的範圍內自動cloase;as把檔案存成f
    for line in f:                  # 要讀取檔案，7、8行是必備
        print(line)                 # 當時寫檔案按了enter，他會存成換行符號\n，所以print出來會多一個空行
        # 以下證明有換行符號，加入到空清單
        data.append(line)
print(data)                         # ['french fies\n', 'fried chicken']

with open('food.txt', 'r') as f:    
    for line in f:                  
        data.append(line.strip())   # strip()只能對"字串"去掉多餘空格和換行符號，就像.append只能對"清單"做一樣
print(data)                         # ['french fies\n', 'fried chicken', 'french fies', 'fried chicken']