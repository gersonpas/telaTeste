def notas(valor, ced):
  totalced = valor // ced
  resto = valor % ced
  ret = (f'Total de {totalced:2} Cédulas de R${ced:2},00')
  return ret,resto, totalced, ced
print('\033[33m='*55)
print('{:^55}'.format('BANCO GPAS'))
print('='*55)
print('\033[33mNOTAS DISPONÍVEIS: R$1,00 / R$10,00/ R$20,00 e R$50,00\033[31m')
print('\033[33m='*55)
saque = int(input('\033[31mQuanto deseja sacar? '))
tipoNotas = 50
retorno = notas(saque,tipoNotas)
if retorno[2] > 0:
  print(retorno[0])

cedulas = 20
while retorno[1] > 0:
    valnotas = (retorno[1])
    tipoNotas = cedulas
    retorno = notas(valnotas, tipoNotas)
    if retorno[2] > 0 and valnotas > 0:
      print(retorno[0])
    cedulas = 10
    if retorno[3] == 10 and retorno[1]:
      tipoNotas = 1
      valnotas = retorno[1]
      retorno = notas(valnotas, tipoNotas)
      print(retorno[0])
      break
print('\033[33m='*55)
print('Volte sempre. O banco GPAS agradece. Tenha um Bom Dia!')
print('='*55)
