import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options ;


def main():
    print("Converting Please Wait")
    try:
        if(not sys.argv[1] or not sys.argv[2] or not sys.argv[3]):
            raise;
    except:
        print("Usage : python html_to_png.py <html_file_in_current_dir> resolution(e.g 1366,800) save_location/name_of_file");
        exit(1);
    chrome_options = Options();
    chrome_options.add_argument("--headless");
    chrome_options.add_argument("--no-sandbox");
    chrome_options.add_argument("--disable-dev-shm-usage");
    chrome_options.add_argument(f"--window-size={sys.argv[2]}");

    driver = webdriver.Chrome(options=chrome_options);

    abs_path = 'file://' + os.path.abspath(sys.argv[1]);
    file_uri = abs_path.replace('\\', '/');
    driver.get(file_uri)

    driver.save_screenshot(sys.argv[3]);

    driver.quit();
    print("Converted Successfully");


if __name__ == "__main__":
    main();
