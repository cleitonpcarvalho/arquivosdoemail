# Email Attachments Organizer

## Descrição

Este projeto automatiza o salvamento e organização de arquivos anexados enviados por e-mail. Ele foi criado para resolver problemas comuns enfrentados por contadores e outros profissionais que precisam organizar documentos enviados para seus clientes. O script salva os anexos em uma estrutura de pastas organizada, separando os arquivos por remetente e data. 

Com este script, o cliente terá todos os arquivos recebidos de um remetente específico salvos automaticamente em pastas nomeadas de forma intuitiva. Ele também pode ser configurado para rodar diariamente em um servidor VPS.

---

## Funcionalidades

- **Busca por remetente específico**: Salva apenas os anexos enviados pelo remetente fornecido.
- **Organização por data**: Cria pastas com base na data do dia atual.
- **Nomes amigáveis para pastas**: Pastas nomeadas com o formato `Arquivos do dia DD-MM-AAAA` e `Remetente - Nome do Remetente`.
- **Automatização**: Pode ser configurado para rodar automaticamente em um VPS diariamente às 23:59.
- **Substituição de caracteres inválidos**: Os nomes dos arquivos são ajustados para evitar problemas no sistema de arquivos.

---

## Tecnologias Utilizadas

- **Python**
- Biblioteca [imbox](https://github.com/martinrusev/imbox)

---

## Como Usar

### Pré-requisitos

1. Python 3.8+
2. Instalar as dependências do projeto:

   ```bash
   pip install imbox
   ```

3. Um arquivo JSON chamado `credenciais.json` com as informações do e-mail de onde os anexos serão baixados. O formato do arquivo é o seguinte:

   ```json
   {
       "e-mail": "seu-email@example.com",
       "password": "sua-senha",
       "host": "imap.seu-servidor.com"
   }
   ```

### Passo a Passo

1. Clone o repositório do projeto:

   ```bash
   git clone https://github.com/seu-usuario/email-attachments-organizer.git
   ```

2. Navegue até a pasta do projeto:

   ```bash
   cd email-attachments-organizer
   ```

3. Configure o arquivo `credenciais.json` conforme o exemplo fornecido acima.

4. Execute o script:

   ```bash
   python script.py
   ```

5. Insira o e-mail do remetente quando solicitado. O script salvará os anexos na estrutura de pastas organizada.

---

## Estrutura das Pastas Geradas

- **Pasta principal**: `Arquivos do dia DD-MM-AAAA`
- **Subpasta**: `Remetente - Nome do Remetente`
- **Arquivos**: Todos os anexos enviados pelo remetente no dia especificado.

Exemplo:
```
Arquivos do dia 27-12-2024
├── Remetente - Fulano de Tal
│   ├── documento1.pdf
│   ├── planilha.xlsx
└── Remetente - Ciclano
    ├── imagem.png
```

---

## Configuração Automática em VPS

Para configurar o script para rodar automaticamente todos os dias às 23:59 em uma VPS, siga os passos abaixo:

1. Edite o `crontab` do servidor:

   ```bash
   crontab -e
   ```

2. Adicione a seguinte linha ao arquivo para agendar a execução diária:

   ```bash
   59 23 * * * /usr/bin/python3 /caminho/para/o/script.py
   ```

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
