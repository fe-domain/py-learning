
num = 10


def func():
    # 使用 global 声明全局变量
    global num
    print(num)
    num = 50
    print(num)


func()
