#UDF is User Defined Function
'''WAP to use User Defined Function with 4 different types (with/without return and argument) as Menu driven
1) Area of a square
2) Volume of cone
3) TSA of cuboid
4) volume of cube
5) exit             '''



while True:
    n=int(input('''Menu driven code

1) Area of a square
2) Volume of cone
3) TSA of cuboid
4) volume of cube
5) exit

Choose your desired option: '''))
    
    if n==1:
        #no return no argumemnt
        def sqrarea():
            a=s*s
            print('Area of the square is ',a,'unit sqr')
        s=int(input('Enter side of the square: '))
        sqrarea()
        print()
        continue
        
    if n==2:
        #no return with argument
        def volume(r,h):
            v=(1/3)*h*(22/7)*r**2
            print('Volume of the cone is ',v,'unit cube')
        r=int(input('Enter radius of the cone: '))
        h=int(input('Enter height of the cone: '))
        volume(r,h)
        print()
        continue

    if n==3:
        #return no argument
        def tsa():
            a=2*((l*b)+(b*h)+(h*l))
            return(a)
        l=int(input('Enter length of the cuboid: '))
        b=int(input('Enter breadth of the cuboid: '))
        h=int(input('Enter height of the cuboid: '))
        print('The total surface area of the cuboid is ',tsa(),' unit sq')
        print()
        continue

    if n==4:
        #return with argument
        def cubev(s):
            v=s**3
            return(v)
        s=int(input('Enter side of the cube: '))
        print('The volume of the cube is ',cubev(s),' unit cube')
        print()
        continue

    if n==5:
        print('The menu driven code has stopped succesfully')
        break


    else:
        print('OOPS ! wrong number, try between 1 to 5')
        print()
        continue
