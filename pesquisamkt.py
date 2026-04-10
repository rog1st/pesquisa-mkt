excelente = 0
bom = 0
ruim = 0
soma_idade_ruim = 0
total_entrevistados = 50

print("--- Iniciando Pesquisa de Satisfação ---")

with open("resultado_completo_pesquisa.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("=== LOG DE RESPOSTAS INDIVIDUAIS ===\n")
    arquivo.write(f"{'Nº':<3} | {'NOME':<20} | {'IDADE':<6} | {'OPINIÃO'}\n")
    arquivo.write("-" * 50 + "\n")

    for i in range(1, total_entrevistados + 1):
        print(f"\nEntrevistado nº {i}")
        nome = input("Digite seu nome: ")
        
        while True:
            try:
                idade = int(input("Digite sua idade: "))
                break
            except ValueError:
                print("Erro! Digite um número inteiro para a idade.")
        
        while True:
            print("Opinião: 1: EXCELENTE | 2: BOM | 3: RUIM")
            opiniao = input("Sua resposta: ")
            if opiniao in ["1", "2", "3"]:
                break
            else:
                print("Resposta inválida! Digite 1, 2 ou 3.")

        status = "EXCELENTE" if opiniao == "1" else "BOM" if opiniao == "2" else "RUIM"
        arquivo.write(f"{i:02d}  | {nome[:20]:<20} | {idade:<6} | {status}\n")

        if opiniao == "1":
            excelente += 1
        elif opiniao == "2":
            bom += 1
        elif opiniao == "3":
            ruim += 1
            soma_idade_ruim += idade

    perc_excelente = (excelente / total_entrevistados) * 100
    perc_bom = (bom / total_entrevistados) * 100
    perc_ruim = (ruim / total_entrevistados) * 100
    media_idade_ruim = soma_idade_ruim / ruim if ruim > 0 else 0

    # Gerando as barras do gráfico (1 caractere para cada 2%)
    barra_exc = "█" * int(perc_excelente / 2)
    barra_bom = "█" * int(perc_bom / 2)
    barra_ruim = "█" * int(perc_ruim / 2)

    resumo = f"""
========================================
        RESUMO ESTATÍSTICO FINAL
========================================
EXCELENTE: {excelente:02d} {barra_exc} ({perc_excelente:.1f}%)
BOM:       {bom:02d} {barra_bom} ({perc_bom:.1f}%)
RUIM:      {ruim:02d} {barra_ruim} ({perc_ruim:.1f}%)

Média de idade (Perfil RUIM): {media_idade_ruim:.1f} anos
========================================
"""
    arquivo.write(resumo)

print("\n" + resumo)
print("Pesquisa finalizada! Dados salvos em 'resultado_completo_pesquisa.txt'.")
