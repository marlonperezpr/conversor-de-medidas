#CONVERSOR DE MEDIDAS EM PYTHON

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def metros_para_pes(metros):
    return metros * 3.28084

def pes_para_metros(pes):
    return pes / 3.28084

def quilogramas_para_libras(quilogramas):
    return quilogramas * 2.20462

def libras_para_quilogramas(libras):
    return libras / 2.20462

def menu():
    print("Conversor de Unidades de Medida")
    print("-------------------------------")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Metros para Pés")
    print("4. Pés para Metros")
    print("5. Quilogramas para Libras")
    print("6. Libras para Quilogramas")
    print("7. Sair")

    escolha = input("Escolha uma opção: ")
    return escolha

def main():
    while True:
        escolha = menu()
        if escolha == "1":
            celsius = float(input("Digite o valor em Celsius: "))
            print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius)}°F")
        elif escolha == "2":
            fahrenheit = float(input("Digite um valor em Fahrenheit: "))
            print(f"{fahrenheit}°F é igual a {fahrenheit_para_celsius(fahrenheit)}°C")
        elif escolha == "3":
            metros = float(input("Digite o valor em Metros: "))
            print(f"{metros} metros é igual a {metros_para_pes(metros)} pés")
        elif escolha == "4":
            pes = float(input("Digite o valor em Pés: "))
            print(f"{pes} pés é igual a {pes_para_metros(pes)} metros")
        elif escolha == "5":
            quilogramas = float(input("Digite o valor em Quilogramas: "))
            print(f"{quilogramas} quilogramas é igual a {quilogramas_para_libras(quilogramas)}libras")
        elif escolha == "6":
            libras = float(input("Digite o valor em Libras: "))
            print(f"{libras} libras é igual a {libras_para_quilogramas} quilogramas")
        elif escolha == "7":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente")

main()
 