import pytest
from models.pages.career_fast_offers_page import career_fast_offers_page


@pytest.mark.ui_test
class TestForm:
    def setup_method(self):
        career_fast_offers_page.open()

    def test_leave_form_empty(self):
        career_fast_offers_page.leave_form_empty()

        career_fast_offers_page.empty_form_should_have_validation_error()
