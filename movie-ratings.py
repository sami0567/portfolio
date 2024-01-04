import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import requests

st.sidebar.title("Genres") #NEW - Sidebar menue with buttons
genre_choice = st.sidebar.radio("Select a Genre", ["Comedy", "Thriller", "Horror"])

if genre_choice == "Thriller":
    st.title("Personal ratings: Thriller")
    check_loved = st.checkbox("Loved Movies") #NEW - checkbox
    movies = (["- The Hunger Games: The Ballads of Songbirds and Snakes", "- Oppenheimer"])
    images = (["hungergames.jpg", "oppenheimer.jpg"])
    links = (["https://youtu.be/NxW_X4kzeus?si=_WJxsU0HO_eqco93", "https://youtu.be/uYPbbksJxIg?si=aW42iKXT9CSgM0YE"])
    if check_loved:
        for movie, image,link in zip(movies, images,links):
            movielist = movie.split()
            if len(movielist) > 0:
                fullurl = "https://www.omdbapi.com/?t=" + "+".join(movielist[:3]) + "&y=2023&apikey=929a2841"
                r = requests.get(fullurl) #API included
                data = r.json()
                plot = data.get("Plot")
                st.write(movie)
                st.header("Plot")
                expander = st.expander("Plot")
                expander.write(plot)
            st.link_button("Trailer", link) #NEW - button
            st.write(movie)
            st.image(image, caption=movie[1:])
            st.write("--")
    check_liked = st.checkbox("Liked Movies") 
    movies = (["- Cocaine Bear", "- Spider-Man: Across the Spider-Verse"])
    images = (["bear.jpeg", "spider.jpg"])
    links = (["https://youtu.be/DuWEEKeJLMI?si=PfBrmNFFB0M5zvOF", "https://youtu.be/shW9i6k8cB0?si=qdJER9iFTybFWK-s"])
    if check_liked:
        for movie, image,link in zip(movies, images,links):
            movielist = movie.split()
            if len(movielist) > 0:
                fullurl = "https://www.omdbapi.com/?t=" + "+".join(movielist) + "&y=2023&apikey=929a2841"
                r = requests.get(fullurl)
                data = r.json()
                plot = data.get("Plot")
                st.write(movie)
                st.header("Plot")
                expander = st.expander("Plot")
                expander.write(plot)
            st.link_button("Trailer", link) 
            st.write(movie)
            st.image(image, caption=movie[1:])
            st.write("--")
    check_dislike = st.checkbox("Disliked Movies") 
    movies = (["- John Wick: Chapter 4", "- Creed III"])
    images = (["4.jpg", "3.jpg"])
    links = (["https://youtu.be/qEVUtrk8_B4?si=LQYhB-KCiukc7anh", "https://youtu.be/AHmCH7iB_IM?si=mqr82EeojX-oLqRQ"])
    if check_dislike:
        for movie, image,link in zip(movies, images,links):
            movielist = movie.split()
            if len(movielist) > 0:
                fullurl = "https://www.omdbapi.com/?t=" + "+".join(movielist) + "&y=2023&apikey=929a2841"
                r = requests.get(fullurl)
                data = r.json()
                plot = data.get("Plot")
                st.write(movie)
                st.header("Plot")
                expander = st.expander("Plot")
                expander.write(plot)
            st.link_button("Trailer", link) 
            st.write(movie)
            st.image(image, caption=movie[1:])
            st.write("--")

if genre_choice == "Comedy":
    st.title("Personal ratings: Comedy")
    check_loved = st.checkbox("Loved Movies") 
    movies = (["- Barbie"])
    images = (["barbie.jpg"])
    links = (["https://youtu.be/pBk4NYhWNMM?si=rJDQKOPabPqoz46t"])
    if check_loved:
        for movie, image,link in zip(movies, images,links):
            movielist = movie.split()
            if len(movielist) > 0:
                fullurl = "https://www.omdbapi.com/?t=" + "+".join(movielist) + "&y=2023&apikey=929a2841"
                r = requests.get(fullurl)
                data = r.json()
                plot = data.get("Plot")
                st.write(movie)
                st.header("Plot")
                expander = st.expander("Plot")
                expander.write(plot)
            st.link_button("Trailer", link) 
            st.write(movie)
            st.image(image, caption=movie[1:])
            st.write("--")
    check_liked = st.checkbox("Liked Movies") 
    movies = (["- Renfield"])
    images = (["vamp.jpg"])
    links = (["https://youtu.be/6LmO6rmDW08?si=l6WTI5-MCZPRUuhl"])
    if check_liked:
        for movie, image,link in zip(movies, images,links):
            movielist = movie.split()
            if len(movielist) > 0:
                fullurl = "https://www.omdbapi.com/?t=" + "+".join(movielist) + "&y=2023&apikey=929a2841"
                r = requests.get(fullurl)
                data = r.json()
                plot = data.get("Plot")
                st.write(movie)
                st.header("Plot")
                expander = st.expander("Plot")
                expander.write(plot)
            st.link_button("Trailer", link) 
            st.write(movie)
            st.image(image, caption=movie[1:])
            st.write("--")
    check_disliked = st.checkbox("Disliked Movies") 
    movies = (["Theater Camp"])
    images = (["camp.jpg"])
    links = (["https://www.youtube.com/watch?v=puVDIUk0kM8"])
    if check_disliked:
        for movie, image,link in zip(movies, images,links):
            movielist = movie.split()
            if len(movielist) > 0:
                fullurl = "https://www.omdbapi.com/?t=" + "+".join(movielist) + "&y=2023&apikey=929a2841"
                r = requests.get(fullurl)
                data = r.json()
                plot = data.get("Plot")
                st.write(movie)
                st.header("Plot")
                expander = st.expander("Plot")
                expander.write(plot)
            st.link_button("Trailer", link) 
            st.write(movie)
            st.image(image, caption=movie[1:])
            st.write("--")
   
if genre_choice == "Horror":
    st.title("Personal ratings: Horror")
    check_loved = st.checkbox("Loved Movies") 
    movies = (["- Scream VI"])
    images = (["scream.jpg"])
    links = (["https://youtu.be/h74AXqw4Opc?si=TtCwxzoGTjIn3GlM"])
    if check_loved:
        for movie, image,link in zip(movies, images,links):
            movielist = movie.split()
            if len(movielist) > 0:
                fullurl = "https://www.omdbapi.com/?t=" + "+".join(movielist) + "&y=2023&apikey=929a2841"
                r = requests.get(fullurl)
                data = r.json()
                plot = data.get("Plot")
                st.write(movie)
                st.header("Plot")
                expander = st.expander("Plot")
                expander.write(plot)
            st.link_button("Trailer", link) 
            st.write(movie)
            st.image(image, caption=movie[1:])
            st.write("--")
    check_liked = st.checkbox("Liked Movies") 
    movies = (["- Five Nights at Freddy's"])
    images = (["five.jpg"])
    links = (["https://youtu.be/0VH9WCFV6XQ?si=6S95LK8hmrEaw-6v"])
    if check_liked:
        for movie, image,link in zip(movies, images,links):
            movielist = movie.split()
            if len(movielist) > 0:
                fullurl = "https://www.omdbapi.com/?t=" + "+".join(movielist) + "&y=2023&apikey=929a2841"
                r = requests.get(fullurl)
                data = r.json()
                plot = data.get("Plot")
                st.write(movie)
                st.header("Plot")
                expander = st.expander("Plot")
                expander.write(plot)
            st.link_button("Trailer", link) 
            st.write(movie)
            st.image(image, caption=movie[1:])
            st.write("--")
    check_disliked = st.checkbox("Disliked Movies") 
    movies = ([" - The Tutor"])
    images = (["tutor.jpg"])
    links = (["https://www.youtube.com/watch?v=E-x3u1rsu1M"])
    if check_disliked:
        for movie, image,link in zip(movies, images,links):
            movielist = movie.split()
            if len(movielist) > 0:
                fullurl = "https://www.omdbapi.com/?t=" + "+".join(movielist) + "&y=2023&apikey=929a2841"
                r = requests.get(fullurl)
                data = r.json()
                plot = data.get("Plot")
                st.write(movie)
                st.header("Plot")
                expander = st.expander("Plot")
                expander.write(plot)
            st.link_button("Trailer", link) 
            st.write(movie)
            st.image(image, caption=movie[1:])
            st.write("--")


        
   
