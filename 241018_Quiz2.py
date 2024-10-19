class 구구단:
    def __init__(self, num):
        self.num = num

    def output(self):
        for a in range(1, 10):
            print(f"{self.num} X {a} = {self.num * a}")

num = int(input("숫자를 입력하세요: "))
multiplication = 구구단(num)
multiplication.output()