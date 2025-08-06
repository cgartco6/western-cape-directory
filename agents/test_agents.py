import pytest
import requests

class TestAgent:
    def run_tests(self):
        pytest.main(["-x", "tests/"])

    def check_links(self):
        links = self.get_all_website_links()
        for link in links:
            if requests.get(link).status_code != 200:
                AutoGPT(task=f"Fix broken link: {link}").execute()

if __name__ == "__main__":
    TestAgent().run_tests()
