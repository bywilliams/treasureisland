# ----------------------- Day 3 --------------------------------
# conditional statements, logical operators, Code blocks and Scope
"""
# Operdores comparativos
Operator    Meaning
    >         Greater than
    <         Less than
    >=        Greater than or equal to
    <=        Less than or equal to
    ==        Equal to
    !=        Not equal to
"""
# exercise Odd or Even
"""
number = int(input("Wich number to you want to check? "))
if number % 2 == 0:
    print("This is a even number.")
else:
    print("\033[1m" + "This is an odd number.")
"""

# Nested condition / Aninhamento de condicionais
"""
if condition:
   if another condition:
     do this
   elif confition:
     do this
   else:
     do this
else:
  do this
  
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride in the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill += 5
        print("child tickets are $5")
    elif age <= 18:
        bill += 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        bill =+ 0
        print("Ok, everything is fine, you can ride for free in the rollercoaster.")
    else:
        bill += 12
        print("Adult tickets are $12")
else:
    print("Grow up litle rabbit!")

wants_photo = input("Do you want a photo taken? Y or N.")
if wants_photo == "Y":
    bill += 3
print(f"Your Final Bill is ${bill}")
  
"""
# ---------------- day 3.2 -------------------------------------------
# comando para printar negrito em python "\033[1m"

# exercise BMI 2.0
"""
print("BMI Calculator 2.0")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are " + "\033[1m" + "underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a " + "\033[1m" + "normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are " + "\033[1m" + "slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are " + "\033[1m" + "obese.")
else:
    print(f"Your BMI is {bmi}, you are " + "\033[1m" + "clinically obese.")
"""

# day 3 aula 6 calculo do ano bissexto
"""
Regra
- o ano é divisivel por 4
- se for divisivel por 100 não é bissexto 
- porém ignore a regra anterior se o ano for divisivel pro 400
"""

"""
year = int(input("Which year do want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else: 
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
"""

# ------------------------ Day 3.4 ------------------------------
# Pizza exercise

"""
Etapa 1
Small 15
Medium 20
Large 25

etapa 2
Add peperoni? Y or N    $2

etapa 3
extra cheese? Y or N    $3
"""
# ------------------------- Python Pizza ------------------------
"""
bill = 0

print("Welcome Python Pizza Deliveries ")
size = input("What size Pizza do you want? S, M, or L ")
add_peperoni = input("Do you want peperoni? Y or N ")
add_cheese = input("Do you want extra cheese? Y or N ")

# Conditional Pizza size choice
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Conditional Add Peperoni or no?
if add_peperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Conditional Add Extra cheese or no
if add_cheese == "Y":
    bill += 1

print(f"Your final bill is: {bill}")
"""

# ------------------- Love Score Exercise -----------------
"""
Etapa 1:
próprio_name input 
people_name input

etapa 2:
mudar os nomes para lowercaser() <- função usada para isso

etapa 3:
contar quantas vezes a letras de TRUE tem em cada nome usando a função count()

etapa 4:
contar quantas vezes as letras de LOVE tem em cada nome usando a função count()

etapa 5:
Tendo o total de score usar if statement para printar qual msg deve aparecer
* se for abaixo de 10 or acima de 90  "Your score is **x**, you go together like coke and mentos."
* se for entre 40 e 50 "Your score is **y**, you are alright together."
* para qualquer outro valor a msg deve ser "Your score is **z**.
"""
print("Welcome to the Love Calculator!")

name1 = input("What is your name? ")
name2 = input("Whats is their name? ")

# combinando os nomes para facilitar a chegagem
combined_name = name1 + name2
# deixando tudo em minusculo para ter certeza que a checagem será correta
lower_case_string = combined_name.lower()

# colocando cada quantidade das letras verificadas em uma variável para facilitar a soma aṕos
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e

# juntando a quatindade q tem em true com a qtde q tem em love dentro de uma váriavel inteira
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
