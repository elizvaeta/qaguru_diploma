import pytest
from models.pages.career_fast_offers_page import career_fast_offers_page
from models.pages.career_it_page import career_it_page
from models.pages.career_page import career_page
from models.pages.menu import menu


@pytest.mark.ui_test
class TestMenu:
    def test_career_page_have_menu(self):
        career_page.open()

        menu.should_have_items()

    def test_career_it_page_have_menu(self):
        career_it_page.open()

        menu.should_have_items()

    def test_career_fast_offers_page_have_menu(self):
        career_fast_offers_page.open()

        menu.should_have_items()
