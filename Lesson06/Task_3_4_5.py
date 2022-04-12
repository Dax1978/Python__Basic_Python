import sys


class Users_Hobby():
    # Конструктор,в  котором получаем названия фалов: пользователей, хобби, имя выходного файла для результатов
    def __init__(self, file_user, file_hobby, file_output='users_hobby.txt') -> None:

        self.f_user = open(file_user, 'r', encoding='utf-8')
        self.f_hobby = open(file_hobby, 'r', encoding='utf-8')
        self.f_output = open(file_output, 'w', encoding='utf-8')

        self.g_user = (line for line in self.f_user)
        self.g_hobby = (line for line in self.f_hobby)

        self.output_data()

    # Чтение данные о users
    def read_users(self):
        try:
            line_user = next(self.g_user)
            return line_user
        except StopIteration:
            return "end_users"

    # Чтение данные о hobby
    def read_hobby(self):
        try:
            line_hobby = next(self.g_hobby)
            return line_hobby
        except StopIteration:
            return "None"

    # Метод чтения данных о пользователях и их хобби, с записью этих данных в указанный выходной файл
    def output_data(self):
        # обход всех данных в файлах генераторами
        while True:
            line_user = self.read_users()
            line_hobby = self.read_hobby()
            if line_user != "end_users":
                self.f_output.write(line_user.rstrip(
                    '\n') + ': ' + line_hobby.rstrip('\n') + '\n')
            elif line_user == "end_users" and line_hobby == "None":
                break
            else:
                print("Выход из программы с завершающим кодом 1 (sys.exit(1))")
                # raise SystemExit(1) - что то не понял как работает
                sys.exit(1)

    # Деструктор, в котором закрываем открытые в конструкторе файлы
    def __del__(self):
        self.f_user.close()
        self.f_hobby.close()
        self.f_output.close()
        print("Файлы закрыты ...")


if __name__ == '__main__':
    # Если имена файлов пользователей, их хобби и выходного файла не заданы
    if len(sys.argv) == 1:
        users_hobby = Users_Hobby('users.csv', 'hobby.csv')
    # Если имена файлов хобби и выходного файла не заданы
    elif len(sys.argv) == 2:
        users_hobby = Users_Hobby(sys.argv[1], 'hobby.csv')
    # Если имя выходного файла не задано
    elif len(sys.argv) == 3:
        users_hobby = Users_Hobby(sys.argv[1], sys.argv[2])
    # Если заданы все имена файлов
    elif len(sys.argv) > 3:
        users_hobby = Users_Hobby(sys.argv[1], sys.argv[2], sys.argv[3])
