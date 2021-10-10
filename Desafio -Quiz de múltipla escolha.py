print('''
Q1 - Quem é o maior campeão brasileiro?
a - Palmeiras
b - Flamengo
c - Atlético Mineiro
''')
resposta = input().lower()

if resposta == "a":
    print ("Correto!")
elif resposta == "b":
    print("Incorreto")
elif resposta == "c":
    print("Incorreto")
else:
    print(" Você não escolheu a, b ou c :( ")

if resposta == "a":
    score = 1
    print(f'score={score}')
else:
    score = 0
    print(f'score={score}')


print('''
Q2 - Quem é o maior campeão da Copa do Brasil?
a - Palmeiras
b - Flamengo
c - Cruzeiro
''')
resposta = input().lower()

if resposta == "a":
    print ("Incorreto")
elif resposta == "b":
    print("Incorreto")
elif resposta == "c":
    print("Correto!")
else:
    print(" Você não escolheu a, b ou c :( ")

if resposta == "c":
    score2 = score + 1
    print(f'score={score2}')
else:
    score2 =  score
    print(f'score={score2}')


print('''
Q3 - Quem é o maior campeão da libertadores?
a - Peñarol - URG
b - Flamengo - BRA
c - Independiente - ARG
d - São Paulo - BRA
e - River Plate - ARG
''')
resposta = input().lower()

if resposta == "a":
    print ("Incorreto")
elif resposta == "b":
    print("Incorreto")
elif resposta == "c":
    print("Correto!")
elif resposta == "d":
    print("Incorreto")
elif resposta == "e":
    print("Incorreto")
else:
    print(" Você não escolheu a, b, c, d ou e :( ")

if resposta == "c":
    score3 = score2 + 1
    print(f'score={score3}')
else:
    score3 =  score2
    print(f'score={score3}')

print('''
Q4 - Qual seleção tem mais Copas do Mundo?
a - Brasil
b - França
c - Italia
d - Argentina
e - Alemanha
''')
resposta = input().lower()

if resposta == "a":
    print ("Correto!")
elif resposta == "b":
    print("Incorreto")
elif resposta == "c":
    print("Incorreto")
elif resposta == "d":
    print("Incorreto")
elif resposta == "e":
    print("Incorreto")
else:
    print(" Você não escolheu a, b, c, d ou e :( ")

if resposta == "a":
    score4 = score3 + 1
    print(f'Final score={score4}')
else:
    score4 =  score3
    print(f'score={score3}')


if score4 == 4:
    print('Muito bem!')
else:
    score4 != 4
    print('Tente novamente')

print('Obrigado por participar do Quiz!!')


    
