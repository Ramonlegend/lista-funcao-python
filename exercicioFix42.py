# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 23/04/2024
# Descrição: Calcula a média de um aluno e verifica se ele foi aprovado ou não.
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

nome = input("Digite seu nome: ")
ra = input("Digite seu RA: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

# Calcula a média do aluno
media = (nota1 + nota2) / 2

# Verifica se a média é maior ou igual a sete
if media >= 7:
  print("Parabéns, você está aprovado!")
else:
  print("Você ainda tem uma chance! Estude mais para o exame")