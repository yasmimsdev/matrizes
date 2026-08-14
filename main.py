# Matriz base: vendas[vendedor][mes]
vendas = [
    [1200, 1500, 1100],
    [1000, 1300, 1400],
    [900, 1700, 1600]
]

# (Opcional) nomes para deixar a saída mais clara
nomes_vendedores = ["Vendedor 0", "Vendedor 1", "Vendedor 2"]
nomes_meses = ["Mês 0", "Mês 1", "Mês 2"]

# ----------------------------
# Etapa 1 — Exibição organizada
# ----------------------------
print("=== PLANILHA DE VENDAS ===")
# Cabeçalho
print(" " * 12 + " | " + " | ".join([f"{m:>6}" for m in nomes_meses]))
print("-" * (12 + 3 + (len(nomes_meses) * 9)))
# Linhas (cada vendedor)
for i in range(len(vendas)):
    linha = vendas[i]
    valores_formatados = " | ".join([f"{valor:>6}" for valor in linha])
    print(f"{nomes_vendedores[i]:<12} | {valores_formatados}")
print()

# ----------------------------
# Etapa 2 — Total por vendedor
# ----------------------------
print("=== TOTAL POR VENDEDOR ===")
totais_por_vendedor = []
for i in range(len(vendas)):
    soma_linha = 0
    for j in range(len(vendas[i])):
        soma_linha += vendas[i][j]
    totais_por_vendedor.append(soma_linha)
    print(f"Total {nomes_vendedores[i]}: {soma_linha}")
print()

# ----------------------------
# Etapa 3 — Total por mês
# ----------------------------
print("=== TOTAL POR MÊS ===")
totais_por_mes = []
# Número de colunas assumindo matriz retangular (todas linhas com mesmo tamanho)
num_meses = len(vendas[0])
for j in range(num_meses):
    soma_coluna = 0
    for i in range(len(vendas)):
        soma_coluna += vendas[i][j]
    totais_por_mes.append(soma_coluna)
    print(f"Total {nomes_meses[j]}: {soma_coluna}")
print()

# ----------------------------
# Etapa 4 — Total geral
# ----------------------------
total_geral = 0
for i in range(len(vendas)):
    for j in range(len(vendas[i])):
        total_geral += vendas[i][j]
print("=== TOTAL GERAL ===")
print(f"Total geral da empresa: {total_geral}")
print()

# ----------------------------
# Etapa 5 — Melhor vendedor
# ----------------------------
melhor_indice = 0
maior_total = totais_por_vendedor[0]
for i in range(1, len(totais_por_vendedor)):
    if totais_por_vendedor[i] > maior_total:
        maior_total = totais_por_vendedor[i]
        melhor_indice = i
print("=== MELHOR VENDEDOR ===")
print(f"Melhor vendedor: {nomes_vendedores[melhor_indice]} (Total: {maior_total})")