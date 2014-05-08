# coding: utf-8

"""
    Desafio 01:
    Mostrar o nome do autor do post.
"""

from selenium import webdriver


firefox = webdriver.Firefox()
firefox.get('http://pythonclub.com.br/')

posts = firefox.find_elements_by_class_name('post')

for post in posts:

    post_title = post.find_element_by_class_name('post-title')
    post_link = post_title.get_attribute('href')

    avatar_img = post.find_element_by_class_name('avatar')
    author_name = avatar_img.get_attribute('alt')

    print u"Títutlo: {titulo}, \nLink: {link} \nAutor: {autor} \n".format(
        titulo=post_title.text,
        link=post_link,
        autor=author_name
    )

firefox.quit()
