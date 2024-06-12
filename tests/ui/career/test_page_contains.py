from models.pages.career_page import career_page


class TestPageContains:
    def setup_method(self):
        career_page.open()

    def test_have_info_blocks(self):
        career_page.should_have_info_blocks()

    def test_go_to_vacancies(self):
        career_page.should_go_to_vacancies()

    def test_go_to_blog(self):
        career_page.should_go_to_blog()
