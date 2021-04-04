import random
from time import sleep
from selenium import webdriver

# Creando el objeto 
driver = webdriver.Chrome('./chromedriver.exe')

# Iniciando el navegador
driver.get('https://www.olx.com.co/republica-de-venezuela_g5304712/carros_c378')

# Ampliando los resultados para tener más infromación
button = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

for i in range(3):
    try:
        button.click()
        sleep(random.uniform(8.0, 10.0))
        button = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        break
    
# Todos los articulos listados
cars = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

# Mostrando la infromación
for car in cars:
    price = car.find_elements_by_xpath('.//span[@data-aut-id="itemPrice"]')
    title = car.find_elements_by_xpath('.//span[@data-aut-id="itemTitle"]')
    
    print()
    print(title[0].text)
    print(price[0].text)

