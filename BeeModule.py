from selenium import webdriver
import requests
import time
import random


class BeeHelper:

    def push_everything (self, url ,data ):
        try:
            payload={ 'data': str(data) }
            response = requests.request("POST", url, data=payload)
            return response 
        except Exception as e:
            print(str(e))
            


def test_module():
    print('Hello World')

test_module()