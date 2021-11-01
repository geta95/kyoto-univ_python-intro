class MyClass:
    a = "マイクラス"
    __b = 0

    def __init__(self, data):
        self.__number = MyClass.__b
        self.mydata = data
        print("MyClass is created, number: ", self.__number)
        MyClass.__b += 1

    def show_number(self):
        print(self.__number)

if __name__ == "__main__":
    print("MyClassのクラス変数 a:", MyClass.a)

    instance1 = MyClass(1)
    instance2 = MyClass(10)

    instance1.show_number()
    instance2.show_number()

    print("mydata of instance1: ", instance1.mydata)
    print("mydata of instance2: ", instance2.mydata)
    instance1.mydata += 1
    instance2.mydata += 2
    print("mydata of instance1: ", instance1.mydata)
    print("mydata of instance2: ", instance2.mydata)

    # クラス外からはアクセス不可のためエラー発生
    print(instance1.__number)
