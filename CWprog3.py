#WAP implementing 2 default arguments and 3 default arguments for 2 UDF si() and ci() and show the function calls with 1,2,3 arguments for si() and 1,2 for cs()
'''SI= prt/100
   CI=p+(1+(r/100))^t'''

def si(p=1000,r=10,t=2):
    print((p*r*t)/100)

def ci(p=1000,r=10,t=2):
    print(p+(1+(r/100))**t)

si()
si(3500,5)
ci()
ci(2000,50,1)
