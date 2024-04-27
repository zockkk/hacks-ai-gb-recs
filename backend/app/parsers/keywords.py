import pandas as pd

df_courses = pd.read_json('static/courses.json', orient='index')


def json_parse_skills():
    tmp_array = []
    for i in df_courses['Технологии, инструменты'].unique():
        tmp_array.append(i.split(','))
    skills_array = []
    for i in tmp_array:
        for j in i:
            skills_array.append(j)

    for i in range(len(skills_array)):
        skills_array[i] = skills_array[i].strip()
    skills_array = list(set(skills_array))
    return skills_array