
# EXERCÍCIO DE LISTAS - 5 A 11
# 1 questão 
Livros = ["O pequeno príncipe - Antoine de Saint-Exupéry", "Dom Casmurro - Machado de Assis", "A hora da estrela - Clarice Lispector"]
print(Livros)
# 2 questão
print(Livros[0]) #primeiro
print(Livros[-1]) #último
# 3 questão
Livros.append("O extraordinário - R. J. Palacio")
Livros.append("O auto da compadecida - Machado de Assis")
print(Livros)
# 4 questão
Livros.insert(1, "Duna") #insere na posição
print(Livros)
# 5 questão 
if "Silencio dos inocentes" in Livros:
    Livros.remove("Silencio dos inocentes")
else:
     print('Livro não encontrado')
     # 6 questão 
Numeros = [1, 2, 3, 2, 4, 2, 5]
print(Numeros.count(2),"vezes.")
# 7 questão
for livro in Livros:
    print(f"o livro {"A hora da estrela - Clarice Lispector"} é interessante")
    print(f"o livro {"O pequeno príncipe - Antoine de Saint-Exupéry"} é interessante")
    print(f"o livro {"Dom Casmurro - Machado de Assis"} é interessante") 
    print(f"o livro {"Duna"} é interessante")
    print(f"o livro {"O extraordinário - R. J. Palacio"} é interessante")
    print(f"o livro {"O auto da compadecida - Machado de Assis"} é interessante")
    # 8 questão
    idades = [12, 18, 25, 14, 30]
    for idade in idades:
        if idade >= 18: 
            print(idade)
           # 9 questão
        Valores = [10, 20, 30, 40]
        soma = 0 
        for valor in Valores:
         soma += valor 
         print("soma:", soma)
# 10 questão
notas = []
for i in range(2):
    aluno_notas = []
    j = 0
    for j in range(3):
        nota = float(input(f"digite a nota {j+1} do aluno {i+1}:"))
        aluno_notas.append(nota)
        notas.append(aluno_notas)
        for k, aluno_notas in enumerate(notas, start=1):
            media = sum(aluno_notas) / len(aluno_notas)
            print(f"media do aluno {k}: {media:2f}")
      # 11 questão 

tabuleiro = [['[ ]' for _ in range(8)] for _ in range(8)]
peças_brancas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
peças_pretas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
for i, piece in enumerate(peças_brancas):
    tabuleiro[0][i] = piece
    tabuleiro[7][i] = piece
for i in range(8):
    tabuleiro[1][i] = "pea"
    tabuleiro[6][i] = "pea" 
for row in tabuleiro:
    print(row)
