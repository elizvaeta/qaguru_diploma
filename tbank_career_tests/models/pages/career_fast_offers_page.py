import allure
from selene import browser, have


class CareerFastOffersPage:
    def open(self):
        with allure.step('Открытие страницы'):
            browser.open('/career/fast-offers')
            return self

    @property
    def dropdown_specialization(self):
        return browser.element('[data-qa-type="uikit/select.dropdown"]')

    @property
    def input_fio(self):
        return browser.element('[data-qa-type="uikit/inputFio.inputBox"]')

    @property
    def input_city(self):
        return browser.element('[data-qa-type="uikit/inputAutocomplete"]')

    @property
    def input_city_items(self):
        return browser.element('[data-qa-type="uikit/dropdown.item.title"]')

    @property
    def input_email(self):
        return browser.element('[data-field-name="email"]')

    @property
    def input_phone(self):
        return browser.element('[data-qa-type="uikit/inputPhone.inputBox"]')

    @property
    def button_submit(self):
        return browser.element('[data-qa-type="uikit/inputPhone.inputBox"]')

    def fill_city(self, city: str):
        with allure.step('Заполнение города'):
            self.input_city.click().type(city)
            self.input_city_items.element_by(have.text(city)).click()

    def leave_form_empty(self):
        with allure.step('Прокликивание полей заявки'):
            self.dropdown_specialization.click()
            self.input_fio.click()
            self.input_city.click()
            self.input_email.click()
            self.input_phone.click()

            self.dropdown_specialization.click()

    def empty_form_should_have_validation_error(self):
        with allure.step('Проверка сообщений валидации о пустых полях'):
            browser.element('#specialization-error').should(have.exact_text('Поле обязательное'))
            browser.element('#name-error').should(have.exact_text('Поле обязательное'))
            browser.element('#city-error').should(have.exact_text('Поле обязательное'))
            browser.element('#email-error').should(have.exact_text('Введите адрес эл. почты'))
            browser.element('#phone-error').should(have.exact_text('Поле обязательное'))


career_fast_offers_page = CareerFastOffersPage()
