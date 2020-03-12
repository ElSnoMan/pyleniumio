""" Make an instance of Pylenium and automate the world! """


from selenium.webdriver.common.keys import Keys
from pylenium import Pylenium


search_field = "[name='q']"
images_link = "[href*='tbm=isch']"


def main():
    py = Pylenium()
    py.visit('https://google.com')
    py.get(search_field).type('puppies', Keys.ENTER)
    py.get(images_link).click()
    print(py.title)
    py.quit()


if __name__ == '__main__':
    main()
