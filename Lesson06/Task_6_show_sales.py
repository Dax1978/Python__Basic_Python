import sys


class Bakery_Show():
    def __init__(self) -> None:
        self.f_bakery = open("bakery.csv", 'r', encoding='utf-8')
        self.g_bakery = (line for line in self.f_bakery)

    def show_all(self):
        for line in self.g_bakery:
            print(line.rstrip('\n'))

    def show_start(self, start):
        for i, line in enumerate(self.g_bakery):
            if i >= start - 1:
                print(line.rstrip('\n'))

    def show_start_end(self, start, end):
        for i, line in enumerate(self.g_bakery):
            if i >= start - 1 and i < end:
                print(line.rstrip('\n'))
            if i == end:
                break

    def __del__(self):
        self.f_bakery.close()


if __name__ == '__main__':
    # Если имена файлов пользователей, их хобби и выходного файла не заданы
    bakery = Bakery_Show()
    if len(sys.argv) == 1:
        bakery.show_all()
    if len(sys.argv) == 2:
        bakery.show_start(int(sys.argv[1]))
    if len(sys.argv) > 2:
        bakery.show_start_end(int(sys.argv[1]), int(sys.argv[2]))
