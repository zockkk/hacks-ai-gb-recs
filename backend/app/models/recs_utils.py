import re
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def data_processing(df):

    df = df.astype('object')
    df = df.fillna(' ')
    return df


def text_processing(text):
    text = text.lower()
    pattern = r'[,!:\.;\(\)]'
    text = re.sub(pattern, '', text)
    return text


def cosine_distances_vac(df, column_name, vac_item, name_new_col):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df[column_name])
    vacancy_text_tfidf = vectorizer.transform([vac_item])

    cosine_distances = cosine_similarity(vacancy_text_tfidf, tfidf_matrix)
    cosine_distances_column = np.squeeze(cosine_distances)
    cosine_distances_series = pd.Series(cosine_distances_column, name=name_new_col)

    df_with_distances = pd.concat([df, cosine_distances_series], axis=1)
    return df_with_distances

def skills_in_text(skills_array, text):
    result_array = []
    for skill in skills_array:
        if skill.lower() in text.lower():
            result_array.append(skill)
    return result_array