import pandas as pd
from models.recs_utils import data_processing, text_processing, cosine_distances_vac, skills_in_text
from parsers.geekbrains import get_pagse_geekbrains

df_courses = pd.read_json('static/courses.json', orient='index')
df_courses_add = get_pagse_geekbrains()

df_courses.columns = df_courses.columns.str.lower()
df_courses['name'] = df_courses['уровень сложности'] + " " + df_courses['name'] + " " + df_courses['подвид']
df_courses = df_courses.drop(['уровень сложности', 'класс', 'тип устройства'], axis=1)
df_courses.columns = ['title', 'url', 'sphere', 'specialization', 'sub', 'skills']
df_courses = df_courses[df_courses['sphere'] != 'Профессии для школьников']

df_courses = pd.merge(df_courses, df_courses_add[['url', 'program']], on='url', how='left')
df_courses = df_courses.astype(str)
df_courses['more_text'] = df_courses.apply(
    lambda x: " ".join([x['sphere'], x['specialization'], x['sub'], x['program'], ]), axis=1
)
df_courses = df_courses.drop(['sphere', 'specialization', 'sub', 'program'], axis=1)
df_courses = data_processing(df_courses)


def get_recommended_courses(title, description, skills):
    # text = df_courses[['title', 'skills', 'more_text']].apply(lambda x: ' '.join(x.astype(str)), axis=1)
    # df_united = pd.DataFrame({'title': title, 'text': text})

    df1 = cosine_distances_vac(df_courses, 'more_text', description, 'cosine_dist_description')
    df2 = cosine_distances_vac(df_courses, 'title', title, 'cosine_dist_title')

    result = df1.join(df2.iloc[:, -1])
    print(1)
    skills_in_vacalsy = skills_in_text(skills, title + description)
    print(2)
    df_courses['skills_ratio'] = (df_courses['more_text'] + df_courses['skills']).apply(lambda x: skills_in_text(skills_in_vacalsy, x))
    for i in df_courses['skills_ratio'].index:
        df_courses.loc[i,'skills_ratio'] = len(df_courses.loc[i,'skills_ratio'])/ len(skills_in_vacalsy)
    print(df_courses['skills'])
    print(df_courses['skills_ratio'])
    print(skills_in_vacalsy)
    result['skills_ratio'] = df_courses['skills_ratio']

    return result.sort_values(by='cosine_dist_title', ascending=False).query('cosine_dist_title > 0')


def get_recommended_courses_pdf(description, skills):
    # text = df_courses[['title', 'skills', 'more_text']].apply(lambda x: ' '.join(x.astype(str)), axis=1)
    # df_united = pd.DataFrame({'title': title, 'text': text})

    df1 = cosine_distances_vac(df_courses, 'more_text', description, 'cosine_dist_description')
    df2 = cosine_distances_vac(df_courses, 'title', description, 'cosine_dist_title')

    result = df1.join(df2.iloc[:, -1])
    print(1)
    skills_in_vacalsy = skills_in_text(skills, description)
    print(2)
    df_courses['skills_ratio'] = (df_courses['more_text'] + df_courses['skills']).apply(lambda x: skills_in_text(skills_in_vacalsy, x))
    for i in df_courses['skills_ratio'].index:
        df_courses.loc[i,'skills_ratio'] = len(df_courses.loc[i,'skills_ratio'])/ len(skills_in_vacalsy)
    print(df_courses['skills'])
    print(df_courses['skills_ratio'])
    print(skills_in_vacalsy)
    result['skills_ratio'] = df_courses['skills_ratio']

    return result.sort_values(by='cosine_dist_title', ascending=False).query('cosine_dist_title > 0')


