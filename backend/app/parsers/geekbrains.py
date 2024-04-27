import requests

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_pagse_geekbrains():
    #собираем ссылки на курсы
    response = requests.get('https://gb.ru/courses/programming')
    tree = BeautifulSoup(response.content, 'html.parser')
    links = tree.find_all( 'a' ,{'class' : 'card_full_link'})

    links_list = []
    for link in links:
        href = link.get('href')
        links_list.append(href)

    #функция парсинга

    def parse_gb(URL):
        title_text = ''
        program_text = ''
        skill_text = ''
        response = requests.get(URL, headers={'User-Agent': UserAgent().chrome})
        tree = BeautifulSoup(response.content, 'html.parser')

        name = tree.find_all( 'h1' ,{'class' : 'gkb-promo__title ui-text-heading--2 ui-text--medium'})
        for title in name:
            title_text = title.get_text(strip=True)

        skills = tree.find_all( 'div' ,{'class' : 'promo-tech__item gkb-promo__tag _large ui-text-body--5'})
        for i in range (len(skills)-10):
            text = skills[i].get_text().replace('\n', ' ').strip()+' '
            skill_text+=' '.join(text.split())

        program = tree.find_all( 'div' ,{'class' : 'training-program-card__body ui-text-body--3'})
        for i in range (len(program)-10):
            text = program[i].get_text().replace('\n', ' ').strip()
            program_text+=(' '+' '.join(text.split()))

        if program_text=='':
            program = tree.find_all( 'div' ,{'class' : 'gkb-acc__accordion'})
            for i in range (len(program)):
                text = program[i].get_text().replace('\n', ' ').strip()
                program_text+=(' '+' '.join(text.split()))

        if program_text=='':
            program = tree.find_all( 'div' ,{'class' : 'program-accordion'})
            for i in range (len(program)):
                text = program[i].get_text().replace('\n', ' ').strip()
                program_text+=(' '+' '.join(text.split()))



        return title_text, skill_text, program_text

    #прогоняем парсинг по всем ссылкам из списка
    texts = []
    titles = []
    skills = []

    for link in links_list:
        title, skill, text = parse_gb(link)
        texts.append(text)
        titles.append(title)
        skills.append(skill)


    pd.set_option('display.max_colwidth', None)

    links_list = pd.Series(links_list)
    texts = pd.Series(texts)
    titles =pd.Series(titles)
    skills = pd.Series(skills)
    df = pd.concat([links_list,titles, skills, texts], axis=1)
    df.columns = ['url', 'title', 'skills', 'program']
    return df
