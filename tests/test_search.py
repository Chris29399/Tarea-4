# coding=utf-8
import os
import pytest
from pages.search_page import SearchPage
from tests.base_test import BaseTest
from dotenv import load_dotenv

load_dotenv()

class TestSearch(BaseTest):

    @pytest.fixture
    def load_pages(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")

        self.page = SearchPage(self.driver, self.wait)
        self.page.go_to_search_page()
        return username, password

    def test_login_pass(self, load_pages):
        username, password = load_pages
        self.page.make_a_login_pass(username, password)

