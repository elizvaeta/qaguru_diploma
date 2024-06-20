import allure
from selene import browser, be, have, command


class Footer:
    @property
    def footer(self):
        return browser.element('[data-module-type="advertFooter"]')

    @property
    def social_medias(self):
        self.footer.perform(command.js.scroll_into_view)

        return browser.element('[data-qa-type="uikit/footer.socMedia"]')

    def should_have_social_medias(self):
        with allure.step("Проверка наличия ссылок на социальные сети в футере"):
            self.footer.should(be.visible)

            self.social_medias.element('[title=VK]').should(have.attribute('href', 'https://vk.com/tbank/'))
            self.social_medias.element('[title=Одноклассники]').should(
                have.attribute('href', 'https://ok.ru/tbank/'))
            self.social_medias.element('[title=Telegram]').should(have.attribute('href', 'https://t.me/tbank/'))


footer = Footer()
