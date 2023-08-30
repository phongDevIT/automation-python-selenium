from seleniumbase import SB
import time
import json
from selenium.webdriver.common.keys import Keys
import re
import html
import requests

def clean_html_tags(text):
    cleaned_text = re.sub(r"<.*?>", "", text)
    cleaned_text = cleaned_text.replace("\n", "").strip()
    return cleaned_text

try:
    sb_config = {"uc": True, "device_metrics": None, "is_mobile": None, "agent": None}

    with SB(
        uc=sb_config["uc"],
        maximize=True,
        device_metrics=sb_config["device_metrics"],
        is_mobile=sb_config["is_mobile"],
        agent=sb_config["agent"],
    ) as sb:
        email = {
            "email": "nguyendiphong159@gmail.com",
            "pass_login": "nguyenngocphong31219",
        }
        sb.open("https://ads.google.com/")
        sb.click('//*[@id="header-topbar"]/div/div[3]/div/div[4]/a', timeout=5)
        sb.type('input[type="email"]', email["email"], timeout=5)
        sb.click('button:contains("Next")', timeout=15, delay=1)
        sb.type('input[type="password"]', email["pass_login"], timeout=5)
        sb.click('button:contains("Next")', timeout=20, delay=1)
        sb.wait_for_element_absent('button:contains("Next")', timeout=5)
        print("successfully access google ads")
        time.sleep(10)
        sb.click('//*[@id="navigation.tools"]/div/a/rail-item', timeout=15, delay=1)
        print("click success 1")
        sb.click(
            "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div[2]/kp-root/div/div/view-loader[2]/splash-view/div/div/div[1]/splash-cards/div/div[1]",
            timeout=15,
            delay=1,
        )
        print("click success 2")
        url = "https://click.mmolovers.com/administrator/api/get_keyword"
        response = requests.get(url)
        data = response.json()
        keywords = list(data.values())

        for keyword in keywords:
            print(keyword)
            input_xpath = "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div[2]/kp-root/div/div/view-loader[2]/splash-view/div/div/div[1]/splash-cards/div/div[1]/div[2]/focus-trap/div[2]/div[1]/div/div/split-ideas-input-panel/div/div[1]/div[1]/search-chips-selector/div/multi-suggest-input/div/div[1]/material-chips/div/div/input"
            input_element = sb.wait_for_element_present(input_xpath, timeout=10)
            input_element.click()
            input_element.send_keys(Keys.CONTROL + "a")
            input_element.send_keys(Keys.DELETE)
            input_element.send_keys(keyword)
            input_element.send_keys(Keys.RETURN)
            print("search input success")
            sb.click(
                "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div[2]/kp-root/div/div/view-loader[2]/splash-view/div/div/div[1]/splash-cards/div/div[1]/div[2]/focus-trap/div[2]/div[1]/div/div/split-ideas-input-panel/div/div[3]/material-button/material-ripple",
                timeout=5,
                delay=1,
            )
            print("input success")
            time.sleep(5)

            sb.click(
                "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div/kp-root/div/div/view-loader[2]/combined-ideas-view/ideas-view/div/div/tableview/div[6]/ess-table/ess-particle-table/div[1]/div/div[2]/div[3]",
                timeout=5,
                delay=1,
            )
            time.sleep(5)
            try:
                # sb.click(
                #     "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div/kp-root/div/div/view-loader[2]/combined-ideas-view/ideas-view/div/div/tableview/div[6]/ess-table/ess-particle-table/div[1]/div/div[2]/div[3]/tools-cell",
                #     timeout=5,
                #     delay=1,
                # )
                print("input success")
                full_xpath = "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div[2]/kp-root/div/div/view-loader[2]/combined-ideas-view/ideas-view/div/div/tableview/div[6]/ess-table/ess-particle-table/div[1]/div/div[2]/div[3]"
                row_element = sb.wait_for_element_present(full_xpath, timeout=10)

                bid_min_element = row_element.find_element(
                    "xpath", ".//*[contains(@essfield, 'bid_min')]/text-field"
                )
                bid_max_element = row_element.find_element(
                    "xpath", ".//*[contains(@essfield, 'bid_max')]/text-field"
                )

                bid_min_value = bid_min_element.get_attribute("innerHTML").strip()
                bid_max_value = bid_max_element.get_attribute("innerHTML").strip()
                bid_min_value = clean_html_tags(bid_min_value)
                bid_max_value = clean_html_tags(bid_max_value)

                bid_min_value = html.unescape(bid_min_value)
                bid_max_value = html.unescape(bid_max_value)
                bid_min_value = bid_min_value.replace("₫", "đ")
                bid_max_value = bid_max_value.replace("₫", "đ")
                data = {"bid_min": bid_min_value, "bid_max": bid_max_value}
                json_data = json.dumps(data, ensure_ascii=False, indent=4)
                print(f"Chuỗi json:\n{json_data}")
                
                
                input_element = sb.wait_for_element_present(input_xpath, timeout=10)
                input_element.click()
                input_element.send_keys(Keys.CONTROL + "a")
                input_element.send_keys(Keys.DELETE)
                
                time.sleep(60)
            except Exception as e:
                print(str(e))
                time.sleep(60)
except Exception as e:
    print(str(e))
