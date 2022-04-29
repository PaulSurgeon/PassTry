password = "a123456"
x = 0
while x < 3:
    x = x + 1
    pwd = input("請輸入密碼: ")
    if pwd == password:
        print("登入成功")
        break #逃出迴圈
    elif pwd != password:
        print("密碼錯誤，你還有", 3-x, "次機會")