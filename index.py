import os
file = open('bd.txt', '+')
key_id = {
    'login': ['andrey', 'admin'],
    'password': ['qwertyuiop', 'root'],
    'role': ['user', 'admin'],
}
login_authorize = ""

os.system('clear') 

def registration(login_authorize):
    print("Hello, enter  login:")
    login = input()
    while 1:
        if (checkDuplicate(login, 'login') == 1):
            print("Login busy, plesase try again")
            login = input()
        elif (checkDuplicate(login, 'login') == 0):
            break

    print("Enter password:")
    password = input()
    choosingRole()
    key_id['login'].append(login)
    key_id['password'].append(password)
    if login_authorize == "":
        main()
    else:
        menuAdmin(login_authorize)


def choosingRole():
    print("Choose your role: 1 - user; 2 - admin")
    value = int(input())
    if (value == 1):
        key_id['role'].append('user')
    elif (value == 2):
        print("Enter code:")
        code = int(input())
        if (code == 1234):
            key_id['role'].append('admin')
        else:
            print("Sorry, code inccorect, you're user")
            key_id['role'].append('user')




def authorize():
    print("Hello, enter your login:")
    login = input()
    
    while 1:
        if (checkDuplicate(login, 'login') == 1):
            print("Ok, enter password:")
            indexOfLogin = key_id['login'].index(login)
            break
        elif (checkDuplicate(login, 'login') == 0):
            print("Enter login again")
            login = input()

    password = input()
    while 1:
        if (checkDuplicate(password, 'password') == 1) and (indexOfLogin == key_id['password'].index(password)):
            print("Authorize OK!!")
            login_authorize = login
            indexOfUser = key_id['login'].index(login)
            checkRole(login_authorize)
            break
        elif (checkDuplicate(password, 'password') == 0):
            print("inccorect password, try again")
            password = input()
    

def changePasswordUser(login_authorize):
    indexOfLogin = key_id['login'].index(login_authorize)
    old_password = key_id['password'][indexOfLogin]
    print("Input old password")
    password = input()
    while password != old_password:
        print("Try again enter old password")
        password = input()
        if password == '0':
            checkRole()
    print("Ok, now enter new password")
    password = input()
    key_id['password'][indexOfLogin] = password
    checkRole(login_authorize)

def resetPassword(login_authorize):
    print("Enter login of user to reset password:")
    login = input()
    i = 0
    while 1:
        if (login == key_id['login'][i]):
            break
        else:
            print("Try again enter login")
            i = 0
            login = input()
        i = i + 1
    indexOfLogin = key_id['login'].index(login)
    key_id['password'][i] = 1234;
    menuAdmin(login_authorize)


def changeLoginUser(login_authorize):
    print("Enter new login for your account:")
    new_login = input()
    indexOfLogin = key_id['login'].index(login_authorize)
    key_id['login'][indexOfLogin] = new_login
    checkRole(new_login)

def changeRole(login_authorize):
    print("Enter new login for account change role:")
    login = input()
    i = 0
    while 1:
        if (login == key_id['login'][i]) and i < len(key_id['login']):
            break
        elif (i > len(key_id['login'])):
            print("Try again enter login")
            i = 0
            login = input()
        i = i + 1
    print("Choose role for changing: 1 - admin, 2 - user")
    value = int(input())
    if value == 1:
        key_id['role'][i] = 'admin'
    elif value == 2:
        key_id['role'][i] = 'user'
    else:
        key_id['role'][i] = 'user'
    menuAdmin(login_authorize)

def checkDuplicate(login, key):
    n = 0
    for lists_log in key_id[key]:
        if (lists_log == login):
            n = n + 1
    if n > 0:
        return 1
    else:
        return 0

def checkRole(login_authorize):
    index = key_id['login'].index(login_authorize)
    if (key_id['role'][index] == 'admin'):
        menuAdmin(login_authorize)
    else:
        menuUser(login_authorize)

def menuUser(login_authorize):
    print("\n\n Hello, ", login_authorize, " - user")
    print("1 - change login \n2 - change password \n3 - go out \n4 - close programm")
    value = int(input())
    if (value == 1):
        print("change login")
        changeLoginUser(login_authorize)
    elif (value == 2):
        print("change password")
        changePasswordUser(login_authorize)
    elif (value == 3):
        login_authorize = ""
        print("You go out")
        main()
    elif (value == 4):
        print("Thank you for using programm")
        exit(0)

def menuAdmin(login_authorize):
    print("\n\n Hello, ", login_authorize, " - admin")
    print("1 - create user,\n2 - change my login,\n3 - change my password,\n4 - reset the password of user,\n5 - print list of user,\n 6 - change user role,\n7 - go out\n8 - exit\n")
    value = int(input())
    if value == 1:
        registration(login_authorize)
    elif value == 2:
        changeLoginUser(login_authorize)
    elif value == 3:
        changePasswordUser(login_authorize)
    elif value == 4:
        print("reset the password of user to 1234")
        resetPassword(login_authorize)
    elif value == 5:
        print(key_id)
        menuAdmin(login_authorize)
    elif value == 6:
        print("change user role")
        changeRole(login_authorize)
    elif value == 7:
        login_authorize = ""
        main()
    elif value == 8:
        exit(0)

def main():
    while (1):
        print("\n\n1 - login;\n2 - registration, 3 - print, 4 - exit")
        value = int(input())
        if (value == 1):
            authorize()
        elif (value == 2):
            registration(login_authorize)
        elif (value == 3):
            print(key_id)
        elif (value == 4):
            exit(0)

main()