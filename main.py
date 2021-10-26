import undetected_chromedriver.v2 as uc
from webdriver_manager.chrome import ChromeDriverManager
from booking import auto


brave_path = r'E:/airdrop-tool/brave/#2/browser/brave-portable.exe'
driver_path = r"E:/auto-airdrop/chromedriver_win32_92/chromedriver.exe"
chrome_profile_path = r"E:/airdrop-tool/chrome/chrome/1/chrome/GoogleChromePortable.exe"
twitter_profiles = [
    'cconchimnho01',
    'LTrngQuang6'

]
telegram_groups = [
    'https://t.me/AirdropTradecoinUnderground',
    'https://t.me/airdop_coin_dau_tu'

]
with auto.undetected_chrome(chrome_profile_path) as driver:
    driver.follow_twitter(handle=twitter_profiles)