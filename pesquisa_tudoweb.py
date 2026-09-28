# Pesquisa de opinião - TudoWeb
# Objetivo: coletar a opinião de clientes sobre o atendimento prestado

total_entrevistados = 50   # para os testes, troque para 10

# Contadores (começam em zero)
qtd_excelente = 0
qtd_ruim = 0

print("=== PESQUISA DE SATISFAÇÃO - TUDOWEB ===")
print("Opinião: 1 = EXCELENTE | 2 = BOM | 3 = RUIM")

# Estrutura de repetição: repete uma vez para cada entrevistado
for i in range(total_entrevistados):
    print()
    print("Entrevistado", i + 1, "de", total_entrevistados)

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    opiniao = int(input("Digite a opinião (1, 2 ou 3): "))

    # Validação: repete enquanto a opinião for inválida
    while opiniao < 1 or opiniao > 3:
        print("Opinião inválida! Digite 1, 2 ou 3.")
        opiniao = int(input("Digite a opinião (1, 2 ou 3): "))

    # Estrutura de decisão: verifica a opinião do entrevistado
    if opiniao == 1:
        print("Opinião registrada: EXCELENTE")
        qtd_excelente += 1
    elif opiniao == 2:
        print("Opinião registrada: BOM")
    else:
        print("Opinião registrada: RUIM")
        qtd_ruim += 1

# Resultado final
print()
print("=== RESULTADO DA PESQUISA ===")
print("Quantidade de respostas EXCELENTE:", qtd_excelente)
print("Quantidade de respostas RUIM:", qtd_ruim)