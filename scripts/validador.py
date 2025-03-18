import pandas as pd
import json
import re

# Carregar dados e regras
df = pd.read_csv('data/exemplos/itens.csv')
with open('data/exemplos/regras.json') as f:
    regras = json.load(f)["0200"]

# Validar cada registro
erros = []
for index, row in df.iterrows():
    for regra in regras:
        campo = regra["campo"]
        valor = str(row[campo])
        
        # Verificar obrigatoriedade
        if regra["obrigatorio"] and pd.isna(row[campo]):
            erros.append(f"Linha {index+1}: {regra['mensagem_erro']}")
            continue
        
        # Verificar formato (regex)
        if "formato" in regra:
            if not re.match(regra["formato"], valor):
                erros.append(f"Linha {index+1}: {regra['mensagem_erro']}")
        
        # Verificar valores permitidos
        if "valores_permitidos" in regra:
            if valor not in regra["valores_permitidos"]:
                erros.append(f"Linha {index+1}: {regra['mensagem_erro']}")

# Salvar erros
with open('erros.txt', 'w') as f:
    f.write("\n".join(erros))

print("Validação concluída. Verifique 'erros.txt'.")