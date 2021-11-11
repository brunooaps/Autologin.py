from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

#Aqui seria necessário preencher seu usuário e senha do site que gostaria de fazer login.
usernameStr = 'username'
passwordStr = 'password'

#Aqui deverá colocar o site que gostaria de acessar, precisa ser na tela de login.
browser = webdriver.Chrome()
browser.get(('https://examplewebsite'))

#Para o campo "username", deve colocar o ID do html, do campo de login, assim o python consegue escrever naquele campo
username = browser.find_element_by_id('login_name')
username.send_keys(usernameStr)
#Para a parte da senha, tem a opção de esperar acabar o preenchimento do usuário para preencher a senha, senão acabam se atrapalhando.
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'password_name'))) #Mesmo processo do campo username, pegar o ID do campo da senha
password.send_keys(passwordStr)
 
#Aqui é colocado o campo do botão, para após escrever login e senha, apertar sozinho o botão de avançar.
signInButton = browser.find_element_by_class_name('submit') #Deve-se pegar o ID/Class ou oque tiver, do botão para poder acessar.
signInButton.click()

