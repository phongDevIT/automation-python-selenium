from seleniumbase import SB
import time
import json
from selenium.webdriver.common.keys import Keys
import re
import html
import requests

from email_google import access_google_ads
from keyworkCPC import keywordCPC
from BeeModule import BeeHelper

def clean_html_tags(text):
    cleaned_text = re.sub(r"<.*?>", "", text)
    cleaned_text = cleaned_text.replace("\n", "").strip()
    return cleaned_text

if __name__ == "__main__":
        try:
            sb_config = {
                "uc": True,
                "device_metrics": None,
                "is_mobile": None,
                "agent": None,
            }
            with SB(
                uc=sb_config["uc"],
                maximize=True,
                device_metrics=sb_config["device_metrics"],
                is_mobile=sb_config["is_mobile"],
                agent=sb_config["agent"],
            ) as sb:
                

                email_google = access_google_ads(sb)
                final = []
                while True:
                    final = keywordCPC(sb, email_google, final)

                    helper = BeeHelper()  
                    url = 'https://dev92.beetech.one/test_post'
                    response = helper.push_everything(url, json.dumps(final))
                    print(response)
                    print(response.json())
                    time.sleep(60)

        except Exception as e:
            print(str(e))
