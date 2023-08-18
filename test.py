
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def send_email(username, password, to_email, subject, body):
    url = "https://accounts.google.com/v3/signin/identifier?checkedDomains=youtube&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=AXo7B7WC0q9zU62Hiv9ARbl0FEevDvFo9DS2y7HbH7R10-AziDz4G_3vB53Gxh1ftff1JLlR68psqw&pstMsg=1&rip=1&service=mail&dsh=S-955384532%3A1692331835568287"
    
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)
    
    driver.get(url)
    driver.maximize_window()
    
    driver.find_element(By.ID, "identifierId").send_keys(username)
    driver.find_element(By.ID, "identifierNext").click()
    
    password_input = wait.until(EC.element_to_be_clickable((By.NAME, "Passwd")))
    password_input.send_keys(password)
    driver.find_element(By.ID, "passwordNext").click()
    
    print("Đăng nhập thành công")

    # gửi mail
    
    compose_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Compose']")))
    compose_button.click()

    sleep(5)  

    to_input = wait.until(EC.presence_of_element_located((By.NAME, "To")))
    to_input.send_keys(to_email)

    subject_input = driver.find_element(By.NAME, "Subject")
    subject_input.send_keys(subject)

    body_input = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Message Body']")
    body_input.send_keys(body)

    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Send']")))
    send_button.click()
    sleep(5)
    print("Email đã được gửi")

    driver.quit()

    username = "phong2193240106@bachkhoasaigon.edu.vn"
    password = "nguyenngocphong31219"
    to_email = "nguyendiphong159@gmail.com"
    subject = "Test Email"
    body = " email python test."


    send_email("phong2193240106@bachkhoasaigon.edu.vn", "nguyenngocphong31219", "nguyendiphong159@gmail.com", "Test Email", "email python test.")