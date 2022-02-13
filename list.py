# list清單，符號是中括號
# 清單就是用來裝東西的，且可以混裝int, float, bool, str不同資料型別
# 清單List可以想像成火車，每節車廂是index索引，編號從0開始
# 用.append()可以加東西到清單裡
# 用len()來取長度
# 用in 來檢查東西在不在裡面
a = ['Toyota', 'Honda'] #空清單
print(a)
print(a[0])
print(a[1])
a.append('Audi')        # 增加Audi到清單內
print(a[2])
print(len(a))           #取長度length
print ('Audi' in a)     # 是非題 True, False


# 字串也可以當清單string can also be a list
# Python把字串內的每個字母和符號當成是清單中的各個東西
car = 'Audi'    #['A', 'u', 'd', 'i']
for c in car:
    print(car)

print(len(car))
print('A' in car)
print(car[1])
