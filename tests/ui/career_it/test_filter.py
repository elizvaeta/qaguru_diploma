import pytest
from models.pages.career_it_page import career_it_page


@pytest.mark.ui_test
class TestFilter:
    def setup_method(self):
        career_it_page.open()

    @pytest.mark.parametrize(
        'specialty',
        [
            'Backend',
            'DWH',
            'Frontend',
            'ML'
        ],
        ids=repr
    )
    def test_filter_specialty(self, specialty):
        career_it_page.filter_specialty_choose(specialty)

        career_it_page.filter_specialty_should_have_value(specialty)
        career_it_page.specialty_title_should_have_value(specialty)

    @pytest.mark.parametrize(
        'experience',
        [
            'Junior',
            'Middle',
            'Senior',
            'Head',
        ],
        ids=repr
    )
    def test_filter_experiences(self, experience):
        career_it_page.filter_experiences_choose(experience)

        career_it_page.filter_experiences_should_have_value(experience)

    @pytest.mark.parametrize(
        'city',
        [
            'Любой город',
            'Удаленная работа',
            'Екатеринбург',
        ],
        ids=repr
    )
    def test_filter_cities(self, city):
        career_it_page.filter_cities_choose(city)

        career_it_page.filter_cities_should_have_value(city)
