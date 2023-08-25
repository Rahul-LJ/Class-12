'''NESTED DICTIONARY
AIM: To create a nested dictionary and manipulate the same.
METHODOLOGY: A nested dictionary is created having the main keys to be 3 categories
namely SENIORS, JUNIORS, SUBJUNIORS. For each of these keys, an inner dictionary is
created with keys as BHARATHI, TAGORE, SHIVAJI, PRATAP and values as the score for that
house. The code makes use of an user defined function MAX_SCORE() that takes the
dictionary as parameter and displays the house having maximum score for each category.
Note: Strictly follow the uppercase for all the keys as mentioned above.'''

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
