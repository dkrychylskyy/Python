from selenium import webdriver
import unittest
import requests

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_mini_server_home(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8081')

        # She notices the page title and header mention to-do lists
        self.assertIn('Mini-Serveur', self.browser.title)

        r = requests.get("http://localhost:8081")
        status_code = r.status_code
        self.assertEqual(status_code, 200)

        #print(self.browser.find_elements_by_tag_name('a'))


        # She is invited to enter a to-do item straight away

#        print(browser.find_elements_by_tag_name('a'))

    def test_mini_server_not_found(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8081/not-found')

        # She notices the page title and header mention to-do lists
        r = requests.get("http://localhost:8081/not-found")
        status_code = r.status_code
        self.assertEqual(status_code, 404)



# # Instance de Firefox contrôlée par webdriver
# browser = webdriver.Firefox()

# # On pointe ce browser vers l'URL de notre mini-serveur
# browser.get('http://localhost:8081')

# # En toute logique, on voudrait que le HTML généré par notre serveur ait un titre
# assert 'Mini-Serveur' in browser.title

# r = requests.get("http://localhost:8081")
# # print(r.status_code)

# print(browser.find_elements_by_tag_name('a'))

# browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')