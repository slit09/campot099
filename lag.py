#lag
print('Отправляем в лагерь детей и взрослых на автобусах')
N=int('колличество детей')
M=int('колличество взрослых')
K= input('Введите колличество детей и колличество взрослых')
buses = (N+M)/K
if buses != int(buses):
    buses = int (buses)+1
if buses <=M/2:
   print (buses)
else:
    print(0)