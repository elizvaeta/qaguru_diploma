import allure
from selene import browser, have


class CareerItPage:
    def open(self):
        with allure.step('Открытие страницы'):
            browser.open('/career/it')
            return self

    # Фильтрация по направлению
    @property
    def filter_specialty(self):
        return browser.element('[data-qa-type="listFilter/specialtyUrl.dropdown"]')

    @property
    def filter_specialty_items(self):
        return browser.all('[data-qa-type="listFilter/specialtyUrl.dropdown.item.title"]')

    @property
    def specialty_title(self):
        return browser.element('[data-qa-type="vacancy-list-section-0-title"]')

    def filter_specialty_choose(self, specialty: str):
        with allure.step('Выбор направления'):
            self.filter_specialty.click()
            self.filter_specialty_items.element_by(have.exact_text(specialty)).click()

    def filter_specialty_should_have_value(self, value: str):
        with allure.step('Проверка значения в поле фильтра'):
            self.filter_specialty.should(have.exact_text(value))

    def specialty_title_should_have_value(self, value: str):
        with allure.step('Проверка значения в заголовке'):
            self.specialty_title.should(have.exact_text(value))

    # Фильтрация по уровню
    @property
    def filter_experiences(self):
        return browser.element('[data-qa-type="listFilter/experiencesUrl.dropdown"]')

    @property
    def filter_experiences_value(self):
        return browser.element('[data-qa-type="listFilter/experiencesUrl.value"]')

    @property
    def filter_experiences_items(self):
        return browser.all('[data-qa-type="listFilter/experiencesUrl.dropdown.item.title"]')

    def filter_experiences_choose(self, experience: str):
        with allure.step('Выбор уровня'):
            self.filter_experiences.click()
            self.filter_experiences_items.element_by(have.exact_text(experience)).click()

    def filter_experiences_should_have_value(self, value: str):
        with allure.step('Проверка значения в поле фильтра'):
            self.filter_experiences_value.should(have.exact_text(value))

    # Фильтрация по городу
    @property
    def filter_cities(self):
        return browser.element('[data-qa-type="listFilter/citiesUrl.dropdown"]')

    @property
    def filter_cities_items(self):
        return browser.all('[data-qa-type="listFilter/citiesUrl.dropdown.item.title"]')

    def filter_cities_choose(self, city: str):
        with allure.step('Выбор города'):
            self.filter_cities.click()
            self.filter_cities_items.element_by(have.exact_text(city)).click()

    def filter_cities_should_have_value(self, value: str):
        with allure.step('Проверка значения в поле фильтра'):
            self.filter_cities.should(have.exact_text(value))


career_it_page = CareerItPage()
