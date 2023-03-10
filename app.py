import streamlit as st
from pickle import load
import pandas as pd

st.title("Which song should I :blue[Listen Next]? 🎵")

data = load(open("songs.pkl", 'rb'))
similarity = load(open("similarity.pkl", 'rb'))
data = pd.DataFrame(data)

path = "files/poster.jpg"

def recommended_song(song):
    idx = data[data["Song-Name"] == song].index[0]
    corr = similarity[idx]
    rec = sorted(list(enumerate(corr)), reverse=True, key=lambda x: x[1])[1:11]

    name, artist, movie = [], [], []

    for i in rec:
        inx = i[0]
        name.append(data['Song-Name'].iloc[inx])
        artist.append(data['Singer/Artists'].iloc[inx])
        movie.append(data['Album/Movie'].iloc[inx])

    return name, artist, movie

# song, artist, genre, movie = recommended_song("Ghoomar")
# print(song[0],
#       movie[0],
#       artist[0])

choice= st.selectbox(label="Song I liked :", options=data['Song-Name'])
st.write("You Like: ", choice)

if st.button("Search"):
    st.header(":blue[You Might Like: ]")
    song, artist, movie = recommended_song(choice)

    col1, col2,col3, col4, col5= st.columns(5)

    with col1:
        st.image(path)
        st.subheader(song[0])
        st.write(f":blue[{movie[0]}]")
        st.write(f":blue[{artist[0]}]")
        st.image(path)
        st.subheader(song[5])
        st.write(f":blue[{movie[5]}]")
        st.write(f":blue[{artist[5]}]")

    with col2:
        st.image(path)
        st.subheader(song[1])
        st.write(f":blue[{movie[1]}]")
        st.write(f":blue[{artist[1]}]")
        st.image(path)
        st.subheader(song[6])
        st.write(f":blue[{movie[6]}]")
        st.write(f":blue[{artist[6]}]")

    with col3:
        st.image(path)
        st.subheader(song[2])
        st.write(f":blue[{movie[2]}]")
        st.write(f":blue[{artist[2]}]")
        st.image(path)
        st.subheader(song[7])
        st.write(f":blue[{movie[7]}]")
        st.write(f":blue[{artist[7]}]")

    with col4:
        st.image(path)
        st.subheader(song[3])
        st.write(f":blue[{movie[3]}]")
        st.write(f":blue[{artist[3]}]")
        st.image(path)
        st.subheader(song[8])
        st.write(f":blue[{movie[8]}]")
        st.write(f":blue[{artist[8]}]")

    with col5:
        st.image(path)
        st.subheader(song[4])
        st.write(f":blue[{movie[4]}]")
        st.write(f":blue[{artist[4]}]")
        st.image(path)
        st.subheader(song[9])
        st.write(f":blue[{movie[9]}]")
        st.write(f":blue[{artist[9]}]")

    