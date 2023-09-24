def MAX_SCORE(d):
    for i in d:
        highest = 0
        for scores in d[i].items():  # here scores are tuple of house,score
            if scores[1] > highest:
                highest = scores[1]
                house = scores[0]
        print('Highest score in '+i+' is '+house+' of score ',highest,'points.')


d = {}
m = ['SENIORS', 'JUNIORS', 'SUBJUNIORS']
n = ['BHARATHI', 'TAGORE', 'SHIVAJI', 'PRATAP']
for grades in m:
    nestedd = {}
    print('\nFor',grades,'catogery',sep=' ')
    for house in n:
        x = int(input('Enter score of '+house+':'))
        nestedd[house] = x
    d[grades] = nestedd
MAX_SCORE(d)
