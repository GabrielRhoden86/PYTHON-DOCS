# Importando os pacotes necessários
from yahooquery import Ticker
import mysql.connector

# Criando um objeto Ticker para a ação desejada
petr = Ticker("PETR4.SA")

# Obtendo os dados históricos
historico = petr.history(period="5d")

# Conectando ao banco de dados MySQL
conn = mysql.connector.connect(host='localhost', user='root', password='', database='new_site')

# Criando um cursor
cursor = conn.cursor()

# Iterando sobre cada linha do dataframe historico
for index, row in historico.iterrows():
    # Preparando a instrução SQL
    sql = f"""INSERT INTO petrobras (symbol, date, open, high, low, close, volume, adjclose) 
              VALUES ('{index[0]}', '{index[1]}', {row['open']}, {row['high']}, {row['low']}, {row['close']}, {row['volume']}, {row['adjclose']})"""
    
    # Executando a instrução SQL
    cursor.execute(sql)

# Commitando as alterações
conn.commit()

# Fechando a conexão
conn.close()
