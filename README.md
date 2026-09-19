# 💧 Calculadora de Consumo de Água

🐍 **Projeto desenvolvido em Python** para classificar o consumo mensal de água de um imóvel de acordo com o tipo de imóvel e a quantidade de água consumida.

---

## 👨‍💻 Autor

**Cristian Balsanelli**

- 🐍 Linguagem: **Python**
- 💻 Projeto: **Classificação do consumo de água**
- 📚 Nível: **Iniciante**

---

## 🎯 Objetivo

O programa solicita ao usuário:

🏠 **Tipo do imóvel**
- Casa
- Apartamento
- Comercial

💧 **Consumo mensal de água**, informado em metros cúbicos (m³).

Depois, o programa analisa os dados utilizando estruturas condicionais `if`, `elif` e `else` e apresenta uma classificação do consumo.

---

## ⚙️ Funcionamento

O programa utiliza as seguintes regras:

| 🏠 Tipo de imóvel | 💧 Consumo | 📋 Resultado |
|---|---:|---|
| Comercial | Qualquer valor | Tarifa comercial aplicada |
| Apartamento | Até 10 m³ | Consumo econômico |
| Apartamento/Casa | Até 25 m³ | Consumo moderado |
| Outros casos | Acima dos limites | Consumo excessivo |

---

## 🧠 Conceitos de Python utilizados

Neste projeto foram utilizados conceitos importantes da linguagem:

- 📝 `input()` — entrada de dados
- 🔢 `float()` — conversão para números decimais
- 🔀 `if` — estrutura condicional
- 🔀 `elif` — condição alternativa
- 🔄 `else` — condição final
- ⚖️ Operadores de comparação (`<=`)
- 🔗 Operadores lógicos (`and` e `or`)
- 🖨️ `print()` — apresentação dos resultados

---
