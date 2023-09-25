import json

# Словарь: уникальное имя контакта - ключ -> вложенный словарь
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле 
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи 
# (Например имя или фамилию человека) 
# 4. Использование функций. Ваша программа не должна быть линейной
# Телефонный справочник с внешним хранилищем информации, 
# и чтоб был реализован основной функционал - 
# просмотр, сохранение, импорт, поиск, удаление, изменение данных.


def Search(phonebook, contact):
    lllist = []
    for i in phonebook.keys:
        if contact in i:
            lllist.append(phonebook[i])
    return lllist


def Remove(phonebook, contact):
    moreThanOnce = False
    for i in phonebook.keys:
        if contact in i:
            if moreThanOnce:
                print("More than 1 contact matching your query. Specify detailed contact name")
                return removed
            removed = phonebook.pop(i)
            moreThanOnce = True
    return removed
    

def Change(phonebook, f):
    amount = int(input('How many numbers do you wish to input: '))
    d = 0
    numbers = []
    while amount != 0:
        d += 1
        amount -= 1
        numbers.append(input(f"Input {f}'s {d}th number: "))
    birthday = input("Input birthday in format: DD.MM.YYYY: ")
    email = input("Input email in format: email@someservice.com: ")
    city = input("Input city: ")
    status = input("Input marital status: ")
    phonebook[f] = {"phones":numbers,"birthday":birthday,"email":email,"city":city,"Status":status}
    print('Entry added to collection')
    return phonebook


def Import(phonebook, f):
    amount = int(input('How many numbers do you wish to input: '))
    d = 0
    numbers = []
    while amount != 0:
        d += 1
        amount -= 1
        numbers.append(input(f"Input {f}'s {d}th number: "))
    birthday = input("Input birthday in format: DD.MM.YYYY: ")
    email = input("Input email in format: email@someservice.com: ")
    city = input("Input city: ")
    status = input("Input marital status: ")
    phonebook[f] = {"phones":numbers,"birthday":birthday,"email":email,"city":city,"Status":status}
    print('Entry added to collection')
    return phonebook


def Export(phonebook):
    phonebook_json = open("phone.txt", "a", encoding='utf-8')
    json.dump(phonebook, phonebook_json, sort_keys=True)

phonebook = {
                "Varvara Sergeevna":{"phones":["+79862544955", "+74413874053"],"birthday":"12.11.1988","email":"varvarp6@mail.ru","city":"Kirov","Status":"married"},
                "Ianina Vasilevna":{"phones":["+79484583321", "+79008742342"],"birthday":"18.06.1973","email":"ianina@protonmail.com","city":"Moscow","Status":"divorced"}
}
while True:
    key = input("Enter choices:")
    if key == '/all':
       print("Here is phone list")
       print(phonebook)
    elif key == '/add.contact':
        f = input("Print new contact name: ")
        if f in phonebook:
            print("Contact exists")
            continue
        else:
            phonebook = Import(phonebook, f)
    elif key == '/export.contact':
        Export(phonebook)
    elif key == '/search.contact':
        f = input("Print contact name you wish to search: ")
        result = Search(phonebook, contact=f)
        print("All contacts matching your query: ")
        print(result)
    elif key == '/remove.contact':
        f = input("Print contact name you wish to remove: ")
        phonebook = Remove(phonebook, contact=f)
        print(f"Contact {f} successfully removed")
    elif key == '/change.contact':
        f = input("Print contact name you wish to change: ")
        if not f in phonebook:
            print("Contact does not exist")
            continue
        else:
            phonebook.pop(f)
            phonebook = Change(phonebook, f)
    elif key == '/help':
        print("/all - to print currently existing entries in the dictionary")
        print("/add.contact - to add new contact to phones")
        print("/export.contact - to write all contacts to text file '.txt'")
        print("/search.contact - to search contacts by name")
        print("/remove.contact - to remove specific contact")
        print("/change.contact - to change specific contact")
    elif key == '/quit':
        phonebook_txt = open("phone.txt", "a", encoding='utf-8')
        final = input("Aborting work with contact list, save changes to file? [Y/N] ")
        if final == 'Y':
            json.dump(phonebook, phonebook_txt)
            break
        elif final == 'N':
            break
        else:
            final_ = input("Please, choose yes or no: ")
            if final_ == 'yes':
                json.dump(phonebook, phonebook_txt, sort_keys=True)
                break
            elif final_ == 'no':
                break
            else:
                print('no option chosen - aborting without any changes')
                break
    else:
        print("Unknown command, try /help for help manual")

# Пример входных данных:
# /add.contact   
# Uliana Karaulova
# 2
# +79548405757     
# +78904563984 
# 08.08.1997
# uliana55@mail.ru
# Moscow
# Married
# /all
# /help
# /quit
# some
# yes