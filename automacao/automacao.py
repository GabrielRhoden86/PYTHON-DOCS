from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Cria uma nova instância do Google Chrome
driver = webdriver.Chrome(service=Service(r'C:\chromedriver-win64\chromedriver.exe'))

# Vai para a página do Python
driver.get("http://www.python.org")

# Verifica se o título da página contém a palavra "Python"
assert "Python" in driver.title
