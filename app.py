
# Autor: Cristian Balsanelli
# Linguagem: Python
# Programa que calcula a quantidade de litros de água

#entrada de dados
tipoImovel = input("Insira o tipo de imóvel, digite:rcial, casa ou apartamento: ") #tipo de imóvel digitado pelo usuário
consumoMensal = float(input("Insira o consumo mensal de água em metros cúbicos: Número decimal "))#consumo mensal digitado pelo usuário
#processamento e saída de dados
if tipoImovel == "comercial": # se o tipo de imóvel for comercial, entra neste bloco
    print("Tarifa comercial aplicada – consulte o plano corporativo.")# imprime essa linha
elif tipoImovel == "apartamento" and consumoMensal <= 10: #se tipo for apartamento e consumo mensal menor ou igual a 10, entra neste bloco
    print("Consumo econômico – excelente controle de água!")#imprime essa linha
elif tipoImovel == "apartamento" or tipoImovel == "casa" and consumoMensal <= 25:# se tipo for apartamento ou casa e consumo mensal menor ou igual a 25, entra neste bloco
    print("Consumo moderado – dentro do padrão residencial.")#imprime essa linha
else:# se nenhum caso acima for verdadeiro, entra neste bloco
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos")#imprime essa linha  
  