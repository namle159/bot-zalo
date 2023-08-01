# -*- coding: utf-8 -*-
import random
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from Base.base import Base
from message import *
from contact_zalo import *
class Testcase(unittest.TestCase):
    def testAutoSendmsg(self):
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = Chrome(options=options)
        self.driver.get('https://chat.zalo.me/')
        self.driver.maximize_window()
        time.sleep(10)
        # Nhập tên cột và số lượng muốn chạy bot:
        urls= file_mau['SĐT 10 SỐ'][681:701]
        for i in urls:
            Base(self.driver).click_element(('xpath','//div[@data-translate-title="STR_CONTACT_ADD_FRIEND"]'))

            try:
                Base(self.driver).send_keys_to_element(('xpath','//input[@placeholder="Số điện thoại "]'),i)
                Base(self.driver).click_element(('xpath','//div[@data-translate-inner="STR_SEARCH"]'))
                Base(self.driver).click_element(('xpath','//div[@data-id="btn_UserProfile_SendMsg"]'))
                print(i)
                messageZalo(self)
                ten_nguoi_nhan= Base(self.driver).getElement(('xpath','//div-b18[@class="header-title flx flx-al-c flex-1"]'))
                ten_nguoi_nhan_text = ten_nguoi_nhan.text
                print(f'Đã gửi tin nhắn cho {ten_nguoi_nhan_text}')
                time.sleep((random.randint(30,90)))
            except:
                Base(self.driver).click_element(('xpath','//div[@data-translate-inner="STR_CANCEL"]'))
                print(f'{i} không tìm được thông tin')
        input('Nhấn Enter để đóng trình duyệt...')

if __name__ == '__main__':
    unittest.main()


