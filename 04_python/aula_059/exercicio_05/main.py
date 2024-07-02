print("\n\n")

print("=== Clinica de Nutrição ===\n")

nome = input("-Digite o nome do paciente: ")
peso = float(input("-Digite o peso do paciente (kg): "))
alt = float(input("-Digite a altura do paciente (m): "))
imc = peso / (alt ** 2)

print(f" O paciente {nome} esta com um IMC de ({imc:.1f})")






print("\n\n")