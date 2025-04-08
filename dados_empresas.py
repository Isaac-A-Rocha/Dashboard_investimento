import pandas as pd
import numpy as np

np.random.seed(42)

anos = list(range(2020, 2026))
meses = list(range(1, 13))
empresas = ["Empresa A", "Empresa B", "Empresa C"]

dados = []

for ano in anos:
    for mes in meses:
        for empresa in empresas:
            investimento = np.random.uniform(50000, 200000)
            variacao = np.random.uniform(-0.2, 0.4)
            retorno = investimento * (1 + variacao)
            dados.append({
                "ano": ano,
                "mes": mes,
                "empresa": empresa,
                "investimento": round(investimento, 2),
                "retorno": round(retorno, 2),
                "lucro_prejuizo": round(retorno - investimento, 2)
            })

df = pd.DataFrame(dados)
df.to_csv("dados_investimentos.csv", index=False)
