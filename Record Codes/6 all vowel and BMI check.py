def vowel(t):
    for words in t:
        c=0
        for letters in 'aeiou':
            if letters in words.lower():
                c+=1
        if c >= 5:
            print(words,end=', ')
    print()

def BMI(tup):
    bmi = t[0] / ((t[1])*10**2) # m to cm
    if bmi >= 30:
        print('Obese')
    elif bmi >= 25:
        print('Overweight')
    elif bmi >= 18.5 and bmi < 25:
        print('Normal')
    else:
        print('Underweight')

while True:
    m = int(input("     Menu Driven Code\n1) Display words with vowels\n2) Check BMI\n3) Exit\nChoose your dezired option: "))
    if m == 1:
        t = eval(input('Enter Tuple with words :'))
        print('Words with Vowels are ',end='')
        vowel(t)

    if m == 2:
        t = eval(input('Enter Tuple with weight(in kg) and height(in cm) :'))
        BMI(t)

    if m == 3:
        print('Closed successfully.')
        break
