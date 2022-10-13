from random import randint

problem_check_list = [0] * 6
p = ['J', 'M', 'X', 'I']


for i in p:
    aux = randint(0, 5)
    while problem_check_list[aux] != 0:
        aux = randint(1, 6)
    problem_check_list[aux] = 1
    print(i, aux+1)
