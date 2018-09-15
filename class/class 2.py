'''isinstance(3, int) #проверяет принажлежность классаы
s = 'mDA'
print(s.count('a')) #считать элемент в последовательности
print(s.upper(), s.lower())
s = "{} mda"
h = s.format('heh')
print(h)
x = '{}k{}t{}b{}'
print(x.format('','u','taa',''))
n = list(range(65))
n.sort()
print(n)
n.reverse()
print(n)
y = (11,23,65) #class 'tuple' (кортеж)
print(len(y), y[1])
z = list(y)
z1 = tuple(z)
d = ('1':'odin', '2':'dva')
del(d['2'])
k = list(d.keys())
v = list(d.values())
i = list(d.items())
m = {'one', 'two'}'''

#5.1
cons = 'ptk'
vow = 'ao'
s = '{}{}'
for i in cons:
    for j in vow:
        print(s.format(i,j))

#5.2
nouns = ['An apple', 'A ball', 'A knife', 'A cup', 'A pillow', 'A flag', 'A goose', 'A linguist']
verbs = ['finds', 'bites', 'sings', 'draws', 'hunts']
sentence = '{} {} {}.'
for S in nouns:
    for V in verbs:
        for O in nouns:
            print(sentence.format(S,V,O.lower()))

