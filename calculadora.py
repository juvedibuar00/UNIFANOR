while True:
    print("\nCalculadora Python")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair para o menu inicial")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '5':
        print("Saindo para o menu inicial...")
        break
    
    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida. Tente novamente.")
        continue
    
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    
    if not (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()):
        print("Entrada inválida! Digite apenas números.")
        continue
    
    num1 = float(num1)
    num2 = float(num2)
    
    if escolha == '1':
        print(f"Resultado: {num1 + num2}")
    elif escolha == '2':
        print(f"Resultado: {num1 - num2}")
    elif escolha == '3':
        print(f"Resultado: {num1 * num2}")
    elif escolha == '4':
        if num2 == 0:
            print("Erro! Divisão por zero não é permitida.")
        else:
            print(f"Resultado: {num1 / num2}")
print('----------------------FIM -------------------------')