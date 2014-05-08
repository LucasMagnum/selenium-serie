# coding: utf-8

"""
    Desafio 02:
    Salvar os dados(titulo, link, autor) do post em um arquivo.
"""

import os
import json

from selenium import webdriver


BASE_DIR = os.path.dirname(__file__)

firefox = webdriver.Firefox()
firefox.get('http://pythonclub.com.br/')

posts = firefox.find_elements_by_class_name('post')

with open(os.path.join(BASE_DIR, 'posts.json'), 'w') as json_file:
    posts_list = []

    for post in posts:
        post_title = post.find_element_by_class_name('post-title')
        post_link = post_title.get_attribute('href')

        avatar_img = post.find_element_by_class_name('avatar')
        author_name = avatar_img.get_attribute('alt')

        post_dict = {
            'titulo': post_title.text,
            'link': post_link,
            'autor': author_name
        }

        posts_list.append(post_dict)

    json_posts = json.dumps(posts_list, indent=4)
    json_file.write(json_posts)

firefox.quit()
