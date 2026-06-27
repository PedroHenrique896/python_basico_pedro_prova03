print("\n--------------------------------")
print(" CABEÇALHO GERAL")
print("-------------------------------")
#Usuando as F-Strings e acessando as chaves do dicionário
#
print(f" Aluno(a): {aluno["nome"]}")
print(f" Disciplina:{aluno["disciplina"]}")

from datetime import datetime
data_formatada= datetime.now().strftime("%d/%m/%Y")
#Usando f-string para juntar o texto com a variável
print(f" Data {data_formatada}")
#Saída: Data 16/06/2026
print("-------------------------------")

#SISTEMA ACADEMIA FITNESS
#Autor: Gabarito do Professor
#Conteúdos:
print/input
variáveis
listas e dicionários
if/elif/else
for/while/break
funçoes
parâmetros e return
import random
#

import random

#
#ESTRUTURAS DE DADOS
#

alunos=[]
planos={}
treinos[]

#
#FUNÇOES DE ALUNOS
#

def cadastrar aluno():
nome= input("NOME DO ALUNO:")
idade= int(input("Idade:"))

aluno={
    "nome":nome,
    "idade":idade
    }

aluno.append(aluno)

print("Aluno cadastrado com sucesso!")


def listar_alunos():
    if len(aluno)==0:
print("Nenhum aluno cadastrado.")
else:
print("\nLIsta DE ALUNOS")
print("-" * 30)

for aluno in alunos:
print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"],"anos")
print("-" * 30)

print("Total de alunos :", len(alunos))


def sortear aluno():
if len(aluno) == 0:
print("Cadastre alunos primeiro.")
else:
 escolhido = random.choice (alunos)
 print("Alunos sorteado:", escolhido["nome"])


def buscar aluno():
nome = input("Nome para buscar:")
encontrado = False

for aluno in alunos:
if aluno["nome"]. lower() == nome.lower():
print("\nAluno encontrado!")
print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
encotrado = true
break

if not encontrado:
print("Aluno não encontrado.")

#
#FUNÇÕES DE PLANOS
#===========================

def cadastrarnplano():
nome = input("Nome do aluno:")

print("Aluno não encontrado.")

print("\nPlanos disponíveis:")
print("1-"básico" -> R$ 89,90")
print("2-Intermediário -> R$ 129,90")
print("3-Premium -> R$ 199,90")

 opcao = input("Escolha o plano (1/2/3/):")

 if opcao = "1":
 plano = "Básico"
 valor = 89,90
elif opcao == "2":
plano = "Premium"
valor = 199,90
 else:
print("Opção inválida.")
return
planos[nome] = {
 "plano": plano,
"valor": valor
                                                                }

print("Plano cadastrado com sucesso!")


def consultar plano():
nome = input("Nome do aluno:")

if nome in planos:
dados = planos[nome]
print("\nAluno:", nome)
print("plano:", dados["plano"])
print("Mesalidade: R$", dados["valor"])
else;
print("plano não encontrado para este aluno.")


def listar planos():
    if len(planos)==0:
        print("\nPLANOS ATIVOS")
        print("-" * 30)

        for nome, dados in planos.item():
            print("Aluno:", nome)
            print("Plano:", dados ["plano"])
            print("Valor: R$", dados ["valor"])
            print("-" * 30)

#==============================
# FUNÇÔES DE TREINOS
#==============================

def registrar treino():
    nome = input("Nome do aluno: ")

    print("\Tipos de treino:")
    print("A - peito e Tríceps")
    print("B - Costas e Bíceps

                                              
                                        

                        

                


              
