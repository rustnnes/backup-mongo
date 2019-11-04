# Backup Mongo

## Formato dos arquivos .env

É esperada a existência de uma pasta, de nome _.env_, contendo arquivos de configuração, como segue:

-   **.env**: arquivo padrão de configuração. Aqui vão todas as variáveis de ambiente comuns para o projeto;
-   **.env.development**: arquivo de configuração para ambiente de desenvolvimento;
-   **.env.test**: arquivo de configuração para ambiente de teste;
-   **.env.staging**: arquivo de configuração para ambiente de homologação;
-   **.env.production**: arquivo de configuração para ambiente de produção.

O arquivo _.env_ segue o seguinte formato:

```
BKP_MONGO_ENV=ambiente
BKP_MONGO_DATABASE=database
BKP_MONGO_COLLECTIONS=collections para backup separadas por espaço
```

Os arquivos _.env.\*_ seguem o seguinte formato:

```
BKP_MONGO_URL=endereço do servidor mongo
BKP_MONGO_PORT=porta do servidor mongo
BKP_MONGO_USR=usuário do servidor mongo
BKP_MONGO_PWD=senha do servidor mongo

BKP_MONGO_SECRET_KEY=para o caso de varáveis adicionais, que devem ser configuradas no arquivo `settings.py`
```
