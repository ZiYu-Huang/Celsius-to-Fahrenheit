# for loop
# for loop就是把清單中的東西一個一個拿出來
# 因為for loop會把清單中的東西一個一個拿出來，所以清單中有幾個東西，就會走幾遍迴圈

cars = ['Toyota', 'Honda']

for car in cars:             # 從cars這個清單中每一次拿出來就稱其為car。
    print(car)               # 所以這個car只是暫時的變數，用來稱呼清單中的每個東西
                             # 只會用在for loop裡面，外面就不會使用這個變數
students = ['Allen', 'Tom', 'Mayday', 'JJ', 'Jolin', 'Jay', 'Jam']
for student in students:
    print('Hi', student)  