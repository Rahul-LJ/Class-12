'''MENU DRIVEN CODE – DICTIONARY
AIM: to create a dictionary to store details of ‘n’ subscribers and perform the menu
operations.
METHODOLOGY: The details of ‘n’ subscribers namely name and phone number are read and
stored in a dictionary. Using a menu and user’s choice, the operations like Add a subscriber
detail, View all subscribers, Modify name of a given subscriber, Delete an existing subscriber
are done using user defined functions.
Note: The menu to be display should be:
MENU
1. ADD
2. VIEW
3. MODIFY NAME
4. DELETE
5. EXIT
Creating the dictionary should be done only by calling option 1)ADD repeatedly.
In Modify and Delete, the input taken is the phone number. If the number does not exist in the
list, appropriate message should be shown'''

def add(dd,d):
    d.update(dd)

def view(d):
    for subscribers in d.items():
        print(subscribers)

def modify(d):
    nam = input('Enter Name of the subscriber to be changed :')
    newnam = input('Enter new the name :')
    d[newnam] = d[nam]
    del d[nam]

def delete(nam,d):
    del d[nam]

d={}
for i in range(1,int(input('Enter number of subscribers: '))+1):
    name = input('Enter name of subscriber '+str(i)+':')
    num = int(input('Enter number of subscriber '+str(i)+':'))
    d[name] = num

while True:
    m = int(input('\tMenu Driven\n1) ADD\n2) VIEW\n3) MODIFY NAME\n4) DELETE\n5) Exit\nChoose your desired option :'))
    if m == 1:
        new = eval(input('Enter the keys and values to be added in a dict'))
        add(new,d)
        print('Updated the dict successfully')
        print('')

    if m == 2:
        view(d)
        print('')

    if m == 3:
        modify(d)
        print('')

    if m == 4:
        nam = input('Enter the name of subscriber to be deleted :')
        delete(nam,d)
        print('')

    if m == 5:
        break
