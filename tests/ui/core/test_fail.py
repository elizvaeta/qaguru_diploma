import allure
import pytest


@allure.tag('ui')
@allure.epic('Общие компоненты')
@pytest.mark.ui_test
class TestFail:
    @allure.title('Это пример упавшего теста')
    def test_fail(self):
        assert 1 == 0
