import datetime
import os
import time

from selenium import webdriver


def main():
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get('https://www.kucoin.com/#/trade.pro/TEL-BTC')
    output_dir = os.path.expanduser('~/Desktop/TEL_screenshots/')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        output_filename = os.path.join(output_dir, f'{now}.png')
        print(f'Wrote a screen shot to f{output_filename}')
        driver.save_screenshot(output_filename)
        time.sleep(5)


if __name__ == '__main__':
    main()
