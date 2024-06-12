import allure
from selene import browser, have, be


class Menu:
    @property
    def navigation_menu(self):
        return browser.element('[data-qa-type="uikit/navigation.menu"]')

    @property
    def navigation_menu_items(self):
        return browser.element('[data-qa-type="uikit/navigation.menu"]').all('a')

    def should_have_items(self):
        with allure.step("Проверка наличия пунктов меню"):
            self.navigation_menu.should(be.visible)

            self.navigation_menu_items[0].should(have.text('Работа в ИТ'))
            self.navigation_menu_items[1].should(have.text('Бизнес и процессы'))
            self.navigation_menu_items[2].should(have.text('Работа с клиентами'))


menu = Menu()
