# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

username=(input("Please, type here your username: "))
password=(input("Type your password: "))

while password==username:
    print(f"The password {password}, cannot be the same as your username {username} .\nPlease type it again")
    password=(input("Type your password: "))
else:
    print(f"Your password for the username: {username} was saved.")


