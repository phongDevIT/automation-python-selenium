from seleniumbase import SB
import time

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
        self.sb.type('input[type="password"]', email["pass_login"], timeout=5)
        self.sb.click('button:contains("Next")', timeout=20, delay=1)
        self.sb.wait_for_element_absent('button:contains("Next")', timeout=5)
        print("successfully access google ads")
        time.sleep(20)
        self.sb.click('//*[@id="navigation.tools"]/div/a/rail-item', timeout=15, delay=1)
        self.sb.click(
            "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div[2]/kp-root/div/div/"
            "view-loader[2]/splash-view/div/div/div[1]/splash-cards/div/div[1]",
            timeout=15,
            delay=1,
        )
        print("click success 2")
