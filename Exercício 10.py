# 10. Faça um programa que solicite ao usuário sua idade, depois disso, exiba a classificação etária de acordo com as faixas de valores:
#  Criança para 0 até 11 anos;
#  Adolescente para 12 até 18 anos;
#  Jovem para 19 até 24 anos;
#  Adulto para 25 até 40 anos;
#  Meia Idade para 41 até 60 anos;
#  Idoso acima de 60 anos.

idade = int(input("Informe sua idade "))

if idade >= 0 and idade <= 11:
  print("Você é uma CRIANÇA")
elif idade >= 12 and idade <= 12:
  print("Você é adolecente")
elif idade >= 19 and idade <= 24:
  print("Você é jovem")
elif idade >= 25 and idade <= 40:
  print("Você é adulto")
elif idade >= 41 and idade <= 60:
  print("Você tem meia idade")
elif idade >= 61 and idade <=150:
  print("Você é idoso")
else:
  print("Você digitou errado ou você é um DEUS")