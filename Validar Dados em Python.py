#Faça um programa que leia e valide as seguintes informações:

#    Nome: maior que 3 caracteres;
#    Idade: entre 0 e 150;
#    Salário: maior que zero;
#    Sexo: 'f' ou 'm';
#    Estado Civil: 's', 'c', 'v', 'd';


name = input("Type your Name [At least 4 Characters]: ")
while len(name) <= 4:
    name = input("Your name needs to have at least 4 characters, please type your name again: ")

age = int(input("Type here your age: "))
while age < 0 or age > 150:
    age = int(input("Your age needs to be between 0 and 150 years: "))

salary = float(input("Type here the value of your salary in USD: "))
while salary <= 0:
    salary = int(input("Your salary needs to be higher than 0: "))

sex = input("Type here your Sex: [M for Male and F for Female]: ")
while (sex != 'M') and (sex != "F"):
    sex = input("Error! You can only choose between F or M, please type your option again: ")

marital_status = input("Type here your Marital Status [Single, Married, Divorced and Widowed]: ")
while marital_status != 'Single' and marital_status != 'Married' and marital_status!='Divorced' and marital_status!='Widowed':
    marital_status = input(f'{marital_status} is not a valid option, you can only choose between: Single, Married, Divorced and Widowed.\nPlease type again your option: ')

print(f'Thank you! Here is the information we saved in our system:\nYour name: {name}\nYour age: {age} years old.\nYou recieve {salary} USD per month.\nYour sex: {sex}.\nYour current marital status: {marital_status}. ')

