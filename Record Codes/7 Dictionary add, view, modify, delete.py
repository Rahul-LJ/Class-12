def view(d):
    for subscribers in d.items():
        print(subscribers)

def add(dd,d):
    d.update(dd)

def modify(d):
    nam = input('Enter Name of the subscriber to be changed : ')
    newnam = input('Enter new the name :')
    d[newnam] = d[nam]
    del d[nam]

def delete(nam,d):
    del d[nam]

d={}
for i in range(1,int(input('Enter number of subscribers: '))+1):
    name = input('Enter name of subscriber '+str(i)+': ')
    num = int(input('Enter number of subscriber '+str(i)+': '))
    d[name] = num

while True:
    m = int(input('\tMenu Driven\n1) ADD\n2) VIEW\n3) MODIFY NAME\n4) DELETE\n5) Exit\nChoose your desired option : '))
    if m == 1:
        new = eval(input('Enter the keys and values to be added in a dicttionary: '))
        add(new,d)
        print('Updated the dict successfully')
        print('')

    if m == 2:
        view(d)
        print('')

    if m == 3:
        modify(d)
        print('Sucessfully modified.')
        print('')

    if m == 4:
        nam = input('Enter the name of subscriber to be deleted :')
        delete(nam,d)
        print('Deleted ',nam,' from list successfully.')
        print('')

    if m == 5:
        break
