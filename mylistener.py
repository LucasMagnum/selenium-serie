# coding: utf-8

from selenium import webdriver
from selenium.webdriver.support.events import (
    EventFiringWebDriver, AbstractEventListener
)


class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print "Antes de abrir a url %s" % url

    def after_navigate_to(self, url, driver):
        print "Depois de abrir a url %s" % url

    def before_click(self, element, driver):
        print "Antes de clicar no elemento"

    def after_click(self, element, driver):
        print "Depois de clicar no elemento"

    def before_close(self, driver):
        print "Antes de fechar a pagina"

    def after_close(self, driver):
        print "Depois de fechar a pagina"

    def on_exception(self, exeception, driver):
        print "Ocorreu um erro"


if __name__ == '__main__':
    # instancia do navegador
    firefox = webdriver.Firefox()

    # instancia do listener
    listener = MyListener()

    # instancia do navegador com os eventos monitorados
    ef_firefox = EventFiringWebDriver(firefox, listener)

    # abrir página da python club
    ef_firefox.get('http://pythonclub.com.br/')

    try:
        """
            Propositalmente irá gerar uma exception pois a classe não existe.
            O evento "on_exception" deve ser chamado
        """
        post = ef_firefox.find_element_by_class_name('post-tile')
    except:
        pass

    # localizamos o primeiro post
    post = ef_firefox.find_element_by_class_name('post-title')

    # clicar no elemento
    post.click()

    # fechar a página
    ef_firefox.close()
