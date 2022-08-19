import json

users = []


def get_users():
    try:
        with open("Guseyn", "r") as file:
            for line in file:
                users.append(json.loads(line))
            file.close()
    except FileNotFoundError:
        print("File not found!")


def add_user():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    age = input("Enter age: ")
    user = {"name": name, "surname": surname, "age": age}
    users.append(user)


def save_users():
    try:
        with open("Guseyn", "w") as file:
            for user in users:
                file.write(json.dumps(user) + '\n')
            file.close()
    except FileNotFoundError:
        print("File not found!")

def change_user():
    opt1 = input("1)Change name\n2)Change surname\n3)Change age\nChoose: ")
    word1 = input("Enter your word: ")
    word2 = input("Enter your word: ")
    if opt1 == "1":
        for i in users:
            if i["name"] == word1:
                i["name"] = word2
    if opt1 == "2":
        for i in users:
            if i["surname"] == word1:
                i["surname"] = word2
    if opt1 == "3":
        for i in users:
            if i["age"] == word1:
                i["age"] = word2

def delete_user():
    word1 = input("Enter your name: ")
    for i in users:
        if i["name"] == word1:
            users.remove(i)

def search_by_surname():
    search1 = input("Enter surname to search: ")
    found = False
    for i in users:
        if search1 in i["surname"]:
            print("Exists")
            found = True
    else:
        if not found:
            print("Not found!")



def search_by_age():
    search2 = input("Enter age to search: ")
    found1 = False
    for i in users:
        if search2 in i["age"]:
            print(i)
            found1 = True
    else:
        if not found1:
            print("No users of this age")


get_users()
while True:
    opt = int(input("1) Show users\n2) Add user\n3) Change user\n4) Delete user by name\n5) Search by surname\n6) Search by age\n7) Exit\nChoose: "))
    if opt == 1:
        for user in users:
            print(user)
    elif opt == 2:
        add_user()
        print("User added!")
    elif opt == 3:
        change_user()
    elif opt == 4:
        delete_user()
    elif opt == 5:
        search_by_surname()
    elif opt == 6:
        search_by_age()
    elif opt == 7:
        break
    else:
        print("Wrong option!")
save_users()