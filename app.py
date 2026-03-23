import streamlit as st

# Заглавие
st.title("Галерия на игри")

# Списък с игри (session state)
if "games" not in st.session_state:
    st.session_state.games = []

# Добавяне на нова игра
st.header("Добави нова игра")

name = st.text_input("Име на играта")
description = st.text_area("Описание")
image_url = st.text_input("URL на изображение")
genre = st.selectbox("Жанр", ["Action", "RPG", "Shooter", "Adventure", "Open World"])

if st.button("Добави"):
    if name and description and image_url:
        st.session_state.games.append({
            "име": name,
            "описание": description,
            "картинка": image_url,
            "жанр": genre
        })
        st.success(f"{name} е добавена!")
    else:
        st.warning("Попълнете всички полета!")

# Премахване на игра
if st.session_state.games:
    st.header("Премахни игра")

    names = [g["име"] for g in st.session_state.games]
    remove_name = st.selectbox("Избери игра", names)

    if st.button("Премахни"):
        for g in st.session_state.games:
            if g["име"] == remove_name:
                st.session_state.games.remove(g)
                break
        st.success(f"{remove_name} е премахната!")

# Галерия
st.header("Галерия")

if st.session_state.games:
    for g in st.session_state.games:
        st.subheader(g["име"])
        st.image(g["картинка"], use_container_width=True)
        st.write(f"Жанр: {g['жанр']}")
        st.write(g["описание"])
        st.markdown("---")
else:
    st.info("Няма добавени игри още.")

# Примерни AAA игри (по желание)
if st.button("Добави примерни AAA игри"):
    st.session_state.games.extend([
        {
            "име": "The Witcher 3",
            "описание": "Отворен свят RPG с история за Гералт.",
            "картинка": "https://upload.wikimedia.org/wikipedia/en/0/0c/Witcher_3_cover_art.jpg",
            "жанр": "RPG"
        },
        {
            "име": "GTA V",
            "описание": "Open-world екшън игра в Лос Сантос.",
            "картинка": "https://upload.wikimedia.org/wikipedia/en/a/a5/Grand_Theft_Auto_V.png",
            "жанр": "Open World"
        },
        {
            "име": "Call of Duty",
            "описание": "Популярен FPS шутър.",
            "картинка": "https://upload.wikimedia.org/wikipedia/en/5/5f/Call_of_Duty_cover.jpg",
            "жанр": "Shooter"
        }
    ])
    st.success("Добавени са примерни игри!")
