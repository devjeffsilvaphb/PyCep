print("def pycep():
  # INTERFACE

  print("          PYCEP")
  print(" ")

  print("Criador: JS STUDIOS")
  print("github: @devjeffsilvaphb")
  print("Obrigado por usa nosso repositório!! ;)")
  print(" ")
  print("  ")
  print("///////////////////////")
  print(" ")
  print("1 --> Busca por Cep")
  print("2 --> Busca por endereço")
  print(" ")
  print("Escolha uma das opções acima")
  print(" ")
  # CODIGOS
  esco = input("--> ")
  if esco == "1":
    print("")
    print("") 
    print("")
    print("OK.....DIGITE O CEP DE 8 DIGITOS ABAIXO, SEM PONTOS, ESPAÇOS OU TRAÇOS (TUDO JUNTO)")
    print("")
    cep = input("--> ")
    import requests
    link = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    
    print("Carregando......")
    print("Obtendo dados........")
    print("Finalizando......")
    print(link.json())   
    print("")
    print("Obrigado por usar!!!")                
  else:
    if esco == "2":
        import requests
        print("")
        print("")
        print("")
        print("OK..........INFORME OQUE VAMOS PEDIR LOGO ABAIXO")
        print("")
        uf = input("UF: ")
        city = input("Cidade: ")
        rua = input("Rua: ")
        link = requests.get(f'https://viacep.com.br/ws/{uf}/{city}/{rua}/json/')
        print("Carregando......")
        print("Obtendo dados........")
        print("Finalizando......")
        print("Pronto!!!")
        
        print(link.json())
        print("")
        print("Obrigado por usar!!!")
        
    

 
    
    
  
 
  
  
  
  
print(pycep())
  
  

")
