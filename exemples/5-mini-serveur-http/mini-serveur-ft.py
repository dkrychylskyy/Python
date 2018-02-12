from selenium import webdriver

# Instance de Firefox contrôlée par webdriver
browser = webdriver.Firefox()

# On pointe ce browser vers l'URL de notre mini-serveur
browser.get('http://localhost:8081')

# En toute logique, on voudrait que le HTML généré par notre serveur ait un titre
assert 'Mini-Serveur' in browser.title

browser.quit()