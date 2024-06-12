from models.pages.career_fast_offers_page import career_fast_offers_page


class TestForm:
    def setup_method(self):
        career_fast_offers_page.open()

    def test_leave_form_empty(self):
        career_fast_offers_page.leave_form_empty()

        career_fast_offers_page.empty_form_should_have_validation_error()
