import streamlit as st
import joblib
import pandas as pd
import requests
import requests
import os
from dotenv import load_dotenv,dotenv_values
from pathlib import Path
load_dotenv()
key=(os.getenv("API"))
def fetch_poster(selected_movie_name):
    url = f"https://moviesdatabase.p.rapidapi.com/titles/search/title/{selected_movie_name}"
    querystring = {"exact":"true","titleType":"movie"}
    headers = {
	"X-RapidAPI-Key": f"{key}",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
            }
    response = requests.get(url, headers=headers, params=querystring)
    if(len(response.json()['results']) >0):
        return(response.json()['results'][0]['primaryImage']['url'])
    else:
        return 1


movies=joblib.load('movies')
similarity=joblib.load('similarity')
# print(movies.head())
# print(similarity[0])
st.title('Movie Recommender System')
selected_movie_name=st.selectbox('Select A Movie',movies['title'].values)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    posters=[]
    for i in distances[1:6]:
        # fetch the movie poster
        posters.append(fetch_poster(movies.iloc[i[0]].title))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        

    return recommended_movie_names,posters

if st.button('Show Recommendation'):
    recommended_movie_names ,posters= recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        if(posters[0]!=1):
            st.image(posters[0])
        else:
            st.image('/Users/yogeshgoyal/Desktop/Projects/ML/Projects/Flick_Picks/not_found.png')
    with col2:
        st.text(recommended_movie_names[1])
        if(posters[0]!=1):
            st.image(posters[1])
        else:
            st.image('/Users/yogeshgoyal/Desktop/Projects/ML/Projects/Flick_Picks/not_found.png')
    with col3:
        st.text(recommended_movie_names[2])
        if(posters[0]!=1):
            st.image(posters[2])
        else:
            st.image('/Users/yogeshgoyal/Desktop/Projects/ML/Projects/Flick_Picks/not_found.png')
    with col4:
        st.text(recommended_movie_names[3])
        if(posters[0]!=1):
            st.image(posters[3])
        else:
            st.image('/Users/yogeshgoyal/Desktop/Projects/ML/Projects/Flick_Picks/not_found.png')
    with col5:
        st.text(recommended_movie_names[4])
        if(posters[0]!=1):
            st.image(posters[3])
        else:
            st.image('/Users/yogeshgoyal/Desktop/Projects/ML/Projects/Flick_Picks/not_found.png')
        