import sys

if __name__ == '__main__':
    # Если имена файлов пользователей, их хобби и выходного файла не заданы
    if len(sys.argv) == 1:
        print("Вы не указали сумму продаж для их записи...")
    if len(sys.argv) > 1:
        f_bakery = open("bakery.csv", 'a', encoding='utf-8')
        f_bakery.write(sys.argv[1] + '\n')
        f_bakery.close()
