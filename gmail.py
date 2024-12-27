from imbox import Imbox
import json
from datetime import date
import os
import re 

with open ("credenciais.json","r") as file:
    credenciais = json.loads(file.read())
    
email = credenciais["e-mail"]
senha = credenciais["password"]
servidor = credenciais["host"]

with Imbox(
    hostname=servidor,
    username=email,
    password=senha) as imb:
    
    remetente = input ("Digite o email do remetente: ")
    data_atual = date.today()
    
    # Acessando ano, mês e dia
    y = data_atual.year  # Ano
    m = data_atual.month  # Mês
    d = data_atual.day  # Dia
       
    
    mensagens = imb.messages(sent_from=remetente, date__on=date(y,m, d))
    
    if not mensagens:
        print("Ocorreu um erro!")
        
    for uid, msg in mensagens:
        
        
        print (f"Email: {msg.sent_from[0]['email']}")
        print (f"Assunto: {msg.subject}")
        
        
        
        for anexo in msg.attachments:
            nome_arquivo = anexo['filename']
            # Substitui caracteres inválidos no nome do arquivo
            nome_arquivo = re.sub(r'[<>:"/\\|?*]', '_', nome_arquivo)  # Substitui caracteres inválidos por '_'
            conteudo = anexo['content']
            
            # Obtendo a data do dia atual no formato 'DIA-MES-ANO'
            data_atual = date.today().strftime("%d-%m-%Y")  # Formato da data: DD-MM-YYYY
           
            # Criando o diretório com o nome da data
            diretorio = f"Arquivos do dia {data_atual}"
            os.makedirs(diretorio, exist_ok=True)  # Cria a pasta, se não existir
            
            nome_remetente = f"Remetente - {msg.sent_from[0]['name']}"
            
            # Criando a pasta 'nome_remetente' dentro de 'diretorio'
            caminho_remetente = os.path.join(diretorio, nome_remetente)
            
            os.makedirs(caminho_remetente, exist_ok=True)  # Cria a pasta, se não existir
            
            # Salva o anexo no diretório 'anexos'
            with open(f"{caminho_remetente}/{nome_arquivo}", "wb") as file:
                file.write(conteudo.read())
                
            print(f"Anexo salvo: {nome_arquivo}")        
            
           
            
            
            
        
    
    

    
    
