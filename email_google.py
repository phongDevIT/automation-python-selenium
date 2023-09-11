import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumbase import SB


class EmailGoogleAccess:
    def __init__(self, sb):
        self.sb = sb

    def access_google_ads(self):
        email = {
            "email": "nguyendiphong159@gmail.com",
            "pass_login": "nguyenngocphong3121999",
        }
        self.sb.open("https://ads.google.com/")
        self.sb.click('//*[@id="header-topbar"]/div/div[3]/div/div[4]/a', timeout=5)
        self.sb.type('input[type="email"]', email["email"], timeout=5)

        self.sb.click('button:contains("Next")', timeout=15, delay=1)
        WebDriverWait(self.sb.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        self.sb.type('input[type="password"]', email["pass_login"], timeout=5)
        self.sb.click('button:contains("Next")', timeout=20, delay=1)
        try:
            WebDriverWait(self.sb.driver, 15).until(
                EC.invisibility_of_element_located(
                    (By.CSS_SELECTOR, 'button:contains("Next")')
                )
            )
        except Exception as e:
            print(f"Error: {e}")
        self.sb.wait_for_element_absent('button:contains("Next")', timeout=5)
        time.sleep(5)
        self.sb.click('//*[@id="navigation.tools"]/div/a/rail-item', timeout=5, delay=1)
        self.sb.click(
            "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div[2]/kp-root/div/div/"
            "view-loader[2]/splash-view/div/div/div[1]/splash-cards/div/div[1]",
            timeout=5,
            delay=1,
        )
