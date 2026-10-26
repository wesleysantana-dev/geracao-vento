from time import sleep

print("=" * 50)
print("   SISTEMA DE MONITORAMENTO - VENTOS")
print("=" * 50)
velocidade = float(input("Digite a velocidade média do vento (m/s): "))
print("\nAnalisando dados do parque eólico...")
sleep(1)
if velocidade < 3.0:
    status = "Vento muito fraco. Turbina paralisada."
    geracao_estimada = 0.0
elif 3.0 <= velocidade <= 12.0:
    status = "Vento ideal! Operação eficiente."
    geracao_estimada = velocidade * 150.5
else:
    status = "Alerta: vento muito forte! Acionar freio de segurança."
    geracao_estimada = 1800.0
print("-" * 50)
print(f" Status Operacional: {status}")
print(f" Geração Estimada: {geracao_estimada:.2f} kWh")
print("-" * 50)
print("Relatório gerado com sucesso para o banco de dados!")
