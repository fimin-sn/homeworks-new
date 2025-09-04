''' Задача:
Написать телефонный справочник, который будет сохранять контакты в файл и иметь следующий функционал:
- открыть файл
- сохранить файл
- показать все контакты
- создать контакт
- найти контакт
- изменить контакт
- удалить контакт
- выход
Контакт минимально должен содержать имя, телефон и комментарий (по желанию можно дополнить поля)

Пояснения и рекомендации:
Данное задание можно выполнить в двух вариантах: использовать готовый файл с контактами (находится в материалах) или написать свою структуру:
1.1. В качестве "хранилища" контактов можно использовать любой формат - txt, json, csv
1.2. Контакт минимально должен содержать имя, телефон и комментарий (по желанию можно дополнить поля)
Реализацию сохранения можно выполнить двумя способами: загружать файл, создавать буферную копию для работы и в дальнейшем сохранять (или нет) внесенные изменения, или вносить изменения сразу в файл
Если выбран вариант буферизации - добавить функционал проверки изменений перед выходом (предлагать сохранить изменения) - опционально (делать необязательно)
Поиск по контактам можно делать отдельно по полям (имя, телефон, комментарий), так и общий (поисковое слово ищет сразу во всех полях контакта)
Для упрощения поиска, изменения и удаления рекомендуется добавить контактам - ID
Добавить всевозможные проверки, чтобы программа не крашилась в случае введенных неверных данных
Данное задание подразумевает отличное владение всем навыками затронутых в первом модуле
Сдавать ДЗ ссылкой на свой репозиторий
................................................................................................
Алгоритм решения:
1. Т.к. контакт - имеет структуру, поэтому необходим класс, который определяет структуру и интерфейс.
    Создаем класс Contact с атрибутами:
    family_name, name, phone, comment типа string.
    Каждый объект класса Contact -это ссылка на словарь типа:
    {'family_name':'value1','name':'value2','phone':'value3','comment':'value4'}
2. Телефонный справочник - это список, элементами которого являются словари.
    класс Phones_list, который реализует ряд операций по работе с контактами.
    Класс Phones_list имеет атрибут list_contacts, тип list и методы:
    create_contact, find_contact, change_contact, delete_contact, show_all_contacts
    и два метода работы с внешними хранилищами(файлами):
    load_contacts_from_file, save_contacts_to_file.
3.  Необходим интерфейс для взаимодействия пользователя с телефонным справочником.
    Поэтому создаем класс Manage_phones_list с атрибутами: menu_commands, который
    содержит словарь {command1: symbol1, command2: symbol2, ....}, которые необхомио выполнить,
    dict_field_names - словарь, который содержит {field1 : symbol1, field2 : symbol2,....} список полей
    контакта, file_name - название файла, в котором будет хранится информация о контактах.

Работа программы начинается с:
1. с определения словарей menu_commands, dict_field_names
2. создания объекта menu_manage = Manage_phones_list().
3. cоздания объекта list_phones = Phones_list()
4. определения имени файла, где будут храниться данные. Формат файла json, т.к.
   элемент хранения - словарь. Если файл уже сушествует, то загружаем его содержимое в list_phones.
  Если файла нет ничего не делаем, т.к. при выходе из приложения он автоматически создается и
  данные о контактах в него записываются.
5. сохраняем результат menu_manage.main_menu в переменную point_menu. В этой переменной хранится
   символ вызванной команды.
6. вызываем menu_manage.manage_commands(point_menu), который выполняет данную команду.
7. после выполнения команды снова вызывается menu_manage.main_menu и процесс повторяется до
   тех пор пока пользователь не выберет команду 'выход'. Данные объекта list_phones
   записыватся в файл заново и происходит выход из программы.
'''

import os
import json


# класс описывает атрибуты и методы контакта
class Contact:
    def __init__(self, *args):
        self.__family_name = args[0]
        self.__name = args[1]
        self.__phone = args[2]
        self.__comment = args[3]

    @property
    def family_name(self):
        return self.__family_name

    @family_name.setter
    def family_name(self, family_name):
        self.__family_name = family_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment):
        self.__comment = comment

    def delete_contact(self, **kwargs):
        pass


# класс описывает телефонный справочник - список контактов.
class Phones_list:
    def __init__(self):
        self.phones_list = []

    def add_contact_to_list(self, family_name, name, phone, comment):
        # создание и добавление нового контакта в c
        contact = Contact(family_name, name, phone, comment)
        self.phones_list.append(contact)

    def show_all_contacts(self):
        # Преобразование списка контактов: ссылки заменяются на словари с текстовыми значениями.
        dict_contacts = []
        for item in self.phones_list:
            dict_contacts = [
                {'family_name': item.family_name, 'name': item.name, 'phone': item.phone, 'comment': item.comment} for
                item in self.phones_list]
        for item in dict_contacts:
            print(item)

    def find_contact(self, field_name, field_value):
        # Преобразование списка контактов: ссылки заменяются на словари с текстовыми значениями.
        # Дополнительно в словарь добавляется ключ id cо значением ссылки из телефонного словаря
        dict_contacts = []
        for item in self.phones_list:
            dict_contacts = [{'id': item, 'family_name': item.family_name, 'name': item.name, 'phone': item.phone,
                              'comment': item.comment} for item in self.phones_list]
        # поиск в словарях поля
        field = [item for item in dict_contacts if field_value in item.values()]
        if len(field) != 0:
            return ('Контакт найден', field[0])
        else:
            return ('Контакт не найден!')

    def change_contact(self, contact_for_change, data_for_change):
        field_name = data_for_change[0]
        field_value = data_for_change[1]
        for item in self.phones_list:
            # поиск ссылки на контакт, значение поля которого необходимо заменить.
            if item == contact_for_change['id']:
                # выбор поля, в котором будет изменено значение
                match field_name:
                    case 'family_name':
                        item.family_name = field_value
                    case 'name':
                        item.name = field_value
                    case 'phone':
                        item.phone = field_value
                    case 'comment':
                        item.comment = field_value

    def delete_contact(self, contact):
        self.phones_list.remove(contact)

    def save_contacts_to_file(self, file_name):
        # self.phones_list - это список ссылок на контакты, поэтому извлекаем информацию из этих ссылок
        # и загружаем в словарь.
        # Далее набор словарей сохраняем в файле.
        dict_contacts = []
        for item in self.phones_list:
            dict_contacts = [
                {'family_name': item.family_name, 'name': item.name, 'phone': item.phone, 'comment': item.comment} for
                item in self.phones_list]
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(dict_contacts, file, ensure_ascii=False, indent=4)

    def load_contacts_from_file(self, file_name):
        # чтение данных из файла
        with open(file_name, 'r', encoding='utf-8') as file:
            dict_contacts = json.load(file)
        for item in dict_contacts:
            family_name, name, phone, comment = item.values()
            # добавляем контакты в существующий список
            self.add_contact_to_list(family_name, name, phone, comment)


# Класс описывает интерфейс между пользователем экземпляром класса Phones_list
# Его задача не запрашивать и собирать информацию, он также управляет выполнением команд.
class Manage_phones_list:
    # menu_command - словарь, содержащий список команд с соответствущими им символами
    # dict_field_names - словарь
    def __init__(self, menu_commands, dict_field_names, file_name):
        self.menu_commands = menu_commands
        self.dict_field_names = dict_field_names
        self.file_name = file_name

    def main_menu(self):
        # Вывод меню на основе словаря menu_commands и проверка выбора команды пользователем.
        condition = True
        while condition:
            print('\n  Меню')
            for key, value in self.menu_commands.items():
                print(f'{key}: {value}')
            answer = input()
            if answer in list(self.menu_commands.values()):
                condition = False
                return answer
            else:
                print('Такого пункта нет в меню!')

    def sub_menu_select_field_and_value(self):
        # вывод menu полей контакта на основе словаря dict_field_names
        # данный метод используется при поиске, замене и удалении контактов.
        condition = True
        while condition:
            print('Выберите поле для поиска:')
            for key, value in self.dict_field_names.items():
                print(f'  {key} : {value}')
            char_field = input()
            # проверка правильности выбора поля контакта
            if char_field in list(self.dict_field_names.values()):
                condition = False
                field_value = input('Введите значение поля\n')
                # Определение key по value
                field_name = ''
                for key, value in self.dict_field_names.items():
                    if value == char_field:
                        field_name = key
                return field_name, field_value
            else:
                print('Такого поля нет в меню!')

    def manage_commands(self, symbol_command):
        # метод, который определяет какую команду выполнять.
        # по выбранному символу определяет что нужно сделать
        match symbol_command:
            case 'c':
                print('создать контакт')
                self.create_contact()

            case 'f':
                print('найти контакт')
                result = self.find_contact()
                print(result)

            case 'a':
                print('показать все контакты\n')
                self.show_all_contacts()

            case 'i':
                print('изменить контакт')
                result = self.find_contact()
                if result[0] == 'Контакт найден':
                    contact_for_change = result[1]
                    print(f'Что менять в контакте?\n {contact_for_change}')
                    data_for_change = Manage_phones_list.sub_menu_select_field_and_value(self)
                    print(data_for_change)
                    self.change_contact(contact_for_change, data_for_change)
                else:
                    print('Такого контакта нет')

            case 'd':
                print('удалить контакт')
                result = self.find_contact()
                if result[0] == 'Контакт найден':
                    self.delete_contact(result[1]['id'])
                else:
                    print('Такого контакта нет')

            case 's':
                print('сохранить файл')
                list_phones.save_contacts_to_file(self.file_name)

            case 'r':
                print('открыть файл')
                self.open_file(self.file_name)

            case 'e':
                print('выход')
                # перед выходом из приложения данные о контактах сохраняются в файл
                list_phones.save_contacts_to_file(self.file_name)
                exit()

            case _:
                print('Такого пункта нет в меню.')

    def create_contact(self):
        family_name = input('Введите фамилию:\n')
        print(f'фамилия: {family_name}')
        name = input('Введите имя:\n')
        print(f'имя: {name}')
        phone = input('Введите номер телефона в формате +код страны ABC номер\n'
                      'например: +73422365521,+79024719933\n')
        print(f'номер телефона: {phone}')
        comment = input('Введите комментарий:\n')
        print(f'комментарий: {comment}')
        list_phones.add_contact_to_list(family_name, name, phone, comment)

    def find_contact(self):
        result = Manage_phones_list.sub_menu_select_field_and_value(self)
        if type(result) != str:
            result_find = list_phones.find_contact(result[0], result[1])
            return result_find
        else:
            return result

    def change_contact(self, contact_for_change, data_for_change):
        list_phones.change_contact(contact_for_change, data_for_change)

    def show_all_contacts(self):
        list_phones.show_all_contacts()

    def delete_contact(self, result_find):
        list_phones.delete_contact(result_find)

    def open_file(self, file_name):
        if os.path.isfile(file_name):
            'загрузка телефонного справочника\n'
            list_phones.load_contacts_from_file(file_name)
        else:
            print('Файл не найден.')

    def save_file(self):
        file_name = input('Введите имя файла:\n')
        file_name += '.json'
        # сохранение данных в файл
        list_phones.save_contacts_to_file()


# main_program
# словарь определяет список разрешенных команд и соответствующих им символов английского алфавита.
menu_commands = {'создать контакт': 'c', 'найти контакт': 'f', 'изменить контакт': 'i', 'удалить контакт': 'd',
                 'показать все контакты': 'a', 'загрузить данные из файла': 'r',
                 'сохранить данные в файле': 's', 'выход': 'e'}
# словарь определяет список названий полей контакта и соответствующих им символов английского алфавита.
dict_field_names = {'family_name': 'f', 'name': 'n', 'phone': 'p', 'comment': 'c'}
# вводим имя файла, в котором хранится или будет храниться телефонный справочник.
# тип файла json.
# только с этим файлом работает приложение.
file_name = input('Введите имя телефонного справочника:\n')
file_name += '.json'
menu_manage = Manage_phones_list(menu_commands, dict_field_names, file_name)
list_phones = Phones_list()
menu_manage.open_file(file_name)

# Цикл: выбор команды -> выполнение команды ... выбор команды -> выполнение команды
# до тех пор, пока не выберут команду 'выход' - 'e'
while True:
    point_menu = menu_manage.main_menu()
    menu_manage.manage_commands(point_menu)

'''
тесты:
1. запускаем программу и вводим имя файла, которого нет. 
   Например dict.
   проверяем наличие его в рабочей директории.
   Его не должно быть. Выбираем в меню команду выход - 'e'
   и выходим из приложения.
   Файл dict.json должен появиться в рабочей директории.
   Он пустой.
2. запускаем программу и вводим имя файла dict.
   Нет информации о контактах на экране.
   Нажимаем 'c' - создать контакт и заполняем все поля.
   Нажимаем 'a' - показать все контакты, на экране появится
   информация о введенном контакте. Файл dict.json - пустой.
   Выбираем в меню команду 'e' - выход, и выходим из приложения.
   В файле dict.json появилась информация о введенном контакте.
3. запускаем программу и вводим имя файла dict. На экране пояна
   экране появится информация о контакте, которая была загружена
   из файла dict.json.
   Создаем ещё несколько контактов.
   Нажимаем 'a' - показать все контакты, на экране появятся введенные
   контакты, но их нет в файле.
   Нажимаем 's' - сохранить данные в файле. Контакты появятся в файле.

   Аналогично проверяются все остальные команды.   
'''