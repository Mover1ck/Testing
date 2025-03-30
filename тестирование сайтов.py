from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"  # complete




class WowlolTest(unittest.TestCase):

    #browser = webdriver.Chrome()
    browser = webdriver.Edge()


    def test_page_title(self):

        self.browser.get('https://wowlol.ru/')
        # Явное ожидание загрузки элемента заголовка
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
        except TimeoutException:
            print("Заголовок не был найден за 10 секунд")

        self.assertIn('Вовлол - сборник юмора World of Warcraft: шутки, цитаты и прочие wow приколы',
                      self.browser.title)
        self.browser.quit()

    def test_search(self):
        self.browser.get('https://wowlol.ru/find')

        # Находим элемент для ввода текста по имени 'q' и вводим запрос "Гаррош"
        search_input = self.browser.find_element(By.NAME, 'q')
        search_input.send_keys('Гаррош')

        # Находим кнопку по id 'button' и кликаем на нее
        search_button = self.browser.find_element(By.NAME, 'sa')
        search_button.click()

        # Проверяем, что на странице есть слово "Гаррош" в любом регистре
        time.sleep(10)
        page_source = self.browser.page_source
        self.assertIn('Гаррош'.lower(), page_source.lower(), "Слово 'Гаррош' не найдено на странице")

    def test_create_achievement(self):
        self.browser.get('https://wowlol.ru/achiv/')

        # Вводим текст "Свирепый воин" в поле с name='title' и id='title'
        title_input = self.browser.find_element(By.NAME, 'title')
        title_input.send_keys('Свирепый воин')

        # Кликаем по картинке с id='gift8'
        gift_image = self.browser.find_element(By.ID, 'gift8')
        gift_image.click()

        # Вводим текст "Убить 50 игроков голыми руками" в поле с id='dost'
        dost_input = self.browser.find_element(By.ID, 'dost')
        dost_input.send_keys('Убить 50 игроков голыми руками')

        # Кликаем по кнопке с name='go'
        go_button = self.browser.find_element(By.NAME, 'go')
        go_button.click()

        # Проверяем, что на новой странице есть надпись "Ваше достижение:" в тегах h3
        h3_elements = self.browser.find_elements(By.TAG_NAME, 'h3')
        achievement_text_found = False
        for h3_element in h3_elements:
            if h3_element.text == 'Ваше достижение:':
                achievement_text_found = True
                break
        self.assertTrue(achievement_text_found, "Надпись 'Ваше достижение:' не найдена на странице")

    def test_submit_joke(self):
        self.browser.get('https://wowlol.ru/add')
        time.sleep(3)

        # Вводим текст "Андектот про Гарроша" в поле с class='inputadd' и name='title z'
        title_input = self.browser.find_element(By.CSS_SELECTOR, 'input.inputadd[name="titlez"]')
        title_input.send_keys('Андектот про Гарроша')
        time.sleep(3)

        # Вводим текст "Гаррош, бургер, анекдот" в поле с class='inputadd' и name='key z'
        key_input = self.browser.find_element(By.CSS_SELECTOR, 'input.inputadd[name="keyz"]')
        key_input.send_keys('Гаррош, бургер, анекдот')
        time.sleep(3)

        # Вводим текст про Гарроша в поле с name='text'
        text_input = self.browser.find_element(By.NAME,'text')
        text_input.send_keys(
            'Гаррош Адский Крик решил открыть свой ресторан. Он назвал его "Адский Бургер". Посетители были в восторге от его бургеров, потому что каждый кусок мяса был прожарен адским огнем, а каждая порция картошки фри была подана с долей ада. Но самое интересное начиналось, когда Гаррош выходил в зал и кричал: "Этот бургер для Орды! Этот бургер для Альянса!" и бросал бургеры в гости. Такой сервис можно найти только в ресторане Гарроша Адского Крика!')
        time.sleep(3)

        # Поставляем галочку, кликнув по элементу с id='box'
        checkbox = self.browser.find_element(By.ID, 'box')
        checkbox.click()
        time.sleep(3)

        # Нажимаем кнопку с type='submit'
        submit_button = self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        submit_button.click()
        time.sleep(3)

        # Проверяем, что на открывшейся странице есть надпись "Спасибо, ваш материал отправлен на модерацию"
        success_message = self.browser.find_element(By.XPATH,
            "//*[contains(text(), 'Спасибо, ваш материал отправлен на модерацию')]")
        self.assertTrue(success_message.is_displayed())

if __name__ == '__main__':
    unittest.main(verbosity=2)