# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

class ListCube():
    def __init__(self, num):
        self.lc = []
        self.num = num

    def lcCreate(self):
        for i in range(1, 1000, 2):
            self.lc.append(i ** 3)
        print(self.lc)

    def lcSum(self, nAdd = 0):
        sumNum = 0
        for i in self.lc:
            sum = 0
            for j in str(i + nAdd):
                sum += int(j)
            if (sum % self.num) == 0:
                sumNum += i + nAdd
        print(sumNum)


if __name__ == '__main__':
    lc = ListCube(7)
    lc.lcCreate()
    lc.lcSum()
    lc.lcSum(17)
