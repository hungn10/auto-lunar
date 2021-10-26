
import undetected_chromedriver.v2 as uc
from webdriver_manager.chrome import ChromeDriverManager
import selenium.common.exceptions as exs
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class undetected_chrome(uc.Chrome):
    def __init__(self, profile_path) -> None:
        #thuộc tính cơ bản
        #setting để không nhận diện
        options = uc.ChromeOptions()
        options.binary_location = profile_path
        options.user_data_dir = profile_path
        super(undetected_chrome, self).__init__(ChromeDriverManager().install(),options=options)
        #self.maximize_window()
        self.implicitly_wait(5)

    #auto join group telegram
    def auto_join_telegram(self, telegram_groups):
        #mở telegram web
        self.get('https://web.telegram.org/z/')
        #mở savemessage
        #mở menu telegram
        menu_element = self.find_element_by_css_selector(
            'button[class*="Button smaller translucent"]'
        )
        menu_element.click()
        
        time.sleep(1)
        #click vào save message
        smessage_element = self.find_element_by_css_selector(
            'i[class="icon-saved-messages"]'
        )
        smessage_element.click()
        #tìm box_chat, thêm nhóm tham gia nhóm
        for link in telegram_groups:
            box_chat = self.find_element_by_id("editable-message-text")
            box_chat.send_keys(link)
            send_button = self.find_element_by_css_selector(
                'button[class*="Button send default"]'
            )
            send_button.click()
            time.sleep(1)
            #chuyển qua nhóm
            link_to_group = self.find_elements_by_css_selector(
                f'a[href="{link}"]'
            )
            #xem nhóm đã có save message chưa để bỏ qua
            if len(link_to_group) > 1:
                continue
            #không có thì click
            link_to_group[0].click()
            #tham gia nhóm
            join_button = self.find_element_by_css_selector(
                'button[class="Button tiny primary fluid has-ripple"]'
            )
            join_button.click()
            #back to save message
            time.sleep(1)
            back_button = self.find_element_by_css_selector(
                'button[title="Back"]'
            )
            back_button.click()
            time.sleep(2)


    #auto follow twitter
    def follow_twitter(self, handle):
        for username in handle:
            self.get(f'https://twitter.com/{username}')
            time.sleep(3)
            follow = self.find_element_by_css_selector(
                f'div[aria-label*="@{username}"]'
            )
            if follow.text == "Follow":
                self.execute_script(
                    f"""document.querySelector('div[aria-label="Follow @{username}"]').click()"""
                )
