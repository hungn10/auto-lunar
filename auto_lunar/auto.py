from time import sleep
import undetected_chromedriver.v2 as uc
from undetected_chromedriver import ChromeDriverManager


class auto(uc.Chrome):
    def __init__(self):
        #self.user_agent = user_agent
        #self.proxy_sever = proxy_sever
        options = uc.ChromeOptions()
        #options.add_argument(f'--proxy-server={proxy_sever}')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-gpu')

        #options.add_argument(f'--user-agent={user_agent}')

        super(auto, self).__init__(ChromeDriverManager().install(), options=options)
        self.set_window_size(650, 750)
        self.implicitly_wait(10)
    #click vao link
    def create_acccount(self, email):
        login_button = self.find_element_by_css_selector(
            'a[href="/login"]'
        )
        login_button.click()

        sleep(3)

        email_input = self.find_element_by_css_selector(
            'input[placeholder="Enter Email address"]'
        )
        email_input.send_keys(email)

        sleep(3)

        next_button = self.find_element_by_css_selector(
            'span[class="css-901oao css-16my406 r-fpv9pr r-1inkyih"]'
        )
        next_button.click()

    def get_verify_code(self, account):
