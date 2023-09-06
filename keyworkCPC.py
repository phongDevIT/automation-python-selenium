from seleniumbase import SB
import time
import json
from selenium.webdriver.common.keys import Keys
import re
import html
import requests

class KeywordCPC:
    def __init__(self, sb, email_google):
        self.sb = sb
        self.email_google = email_google

    def keyword_cpc(self):
        url = "https://click.mmolovers.com/administrator/api/get_keyword"
        response = requests.get(url)
        data = response.json()
        final = []

        for id, keyword in data.items():
            print(keyword)
            input_xpath = (
                "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/"
                "awsm-child-content/div[1]/div[2]/kp-root/div/div/view-loader[2]/"
                "splash-view/div/div/div[1]/splash-cards/div/div[1]/div[2]/focus-trap/"
                "div[2]/div[1]/div/div/split-ideas-input-panel/div/div[1]/div[1]/search-"
                "chips-selector/div/multi-suggest-input/div/div[1]/material-chips/div/div/input"
            )
            input_element = self.sb.wait_for_element_present(input_xpath, timeout=10)
            input_element.click()
            input_element.send_keys(Keys.CONTROL + "a")
            input_element.send_keys(Keys.DELETE)
            input_element.send_keys(keyword)
            input_element.send_keys(Keys.RETURN)
            print("search input success")
            self.sb.click(
                "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div[2]/kp-root/div/div/"
                "view-loader[2]/splash-view/div/div/div[1]/splash-cards/div/div[1]/div[2]/focus-trap/div[2]/div[1]/div/div/"
                "split-ideas-input-panel/div/div[3]/material-button/material-ripple",
                timeout=5,
                delay=1,
            )
            time.sleep(5)
            try:
                self.sb.click(
                    "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div/kp-root/div/div/"
                    "view-loader[2]/combined-ideas-view/ideas-view/div/div/tableview/div[6]/ess-table/ess-particle-table/div[1]/"
                    "div/div[2]/div[3]",
                    timeout=5,
                    delay=1,
                )

                try:
                    full_xpath = (
                        "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div[2]/kp-root/div/"
                        "div/view-loader[2]/combined-ideas-view/ideas-view/div/div/tableview/div[6]/ess-table/ess-particle-table/div[1]/"
                        "div/div[2]/div[3]"
                    )
                    row_element = self.sb.wait_for_element_present(full_xpath, timeout=10)

                    bid_min_element = row_element.find_element(
                        "xpath", ".//*[contains(@essfield, 'bid_min')]/text-field"
                    )
                    bid_max_element = row_element.find_element(
                        "xpath", ".//*[contains(@essfield, 'bid_max')]/text-field"
                    )

                    bid_min_value = bid_min_element.get_attribute("innerHTML").strip()
                    bid_max_value = bid_max_element.get_attribute("innerHTML").strip()
                    bid_min_value = self.clean_html_tags(bid_min_value)
                    bid_max_value = self.clean_html_tags(bid_max_value)

                    bid_min_value = html.unescape(bid_min_value)
                    bid_max_value = html.unescape(bid_max_value)

                    bid_min_value = bid_min_value.replace("₫", "").strip()
                    bid_max_value = bid_max_value.replace("₫", "").strip()
                    price = {"GC": bid_min_value, "GT": bid_max_value}
                    value = {"id": id, "keyword": keyword, "Price": price}
                    final.append(value)
                    print(str(final))

                    self.sb.go_back()
                    time.sleep(10)
                    self.sb.click('//*[@id="navigation.tools"]/div/a/rail-item', timeout=15, delay=1)
                    print("click success 3 next")
                    self.sb.click(
                        "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div[2]/kp-root/div/div/"
                        "view-loader[2]/splash-view/div/div/div[1]/splash-cards/div/div[1]",
                        timeout=15,
                        delay=1,
                    )
                    print("click success 4 next image")

                except Exception as e:
                    print(str(e))
                    print("không tìm thấy từ khóa và giá trị đó", keyword)
                    time.sleep(10)
                    continue
            except:
                self.sb.go_back()
                time.sleep(10)
                self.sb.click('//*[@id="navigation.tools"]/div/a/rail-item', timeout=15, delay=1)
                print("click success 3 next")
                self.sb.click(
                    "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div[2]/kp-root/div/div/"
                    "view-loader[2]/splash-view/div/div/div[1]/splash-cards/div/div[1]",
                    timeout=15,
                    delay=1,
                )
                print("click success 4 next image")

        return final

    @staticmethod
    def clean_html_tags(text):
        cleaned_text = re.sub(r"<.*?>", "", text)
        cleaned_text = cleaned_text.replace("\n", "").strip()
        return cleaned_text
