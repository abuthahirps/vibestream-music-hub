import streamlit as st

st.set_page_config(
    page_title="VibeStream | User Dashboard",
    page_icon="🎧",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #171026 50%, #0d1527 100%);
        color: #FFFFFF;
    }
    .song-card {
        background: rgba(23, 25, 48, 0.7);
        border: 1px solid rgba(138, 75, 255, 0.3);
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(12px);
    }
    .song-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #00f2fe;
        margin-bottom: 4px;
    }
    .artist-name {
        font-size: 1rem;
        color: #f1f5f9;
        margin-bottom: 12px;
    }
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 6px;
    }
    .badge-genre {
        background: rgba(147, 51, 234, 0.25);
        color: #c084fc;
        border: 1px solid rgba(147, 51, 234, 0.4);
    }
    .badge-mood {
        background: rgba(14, 165, 233, 0.25);
        color: #38bdf8;
        border: 1px solid rgba(14, 165, 233, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# Shared Database initialization
if "songs" not in st.session_state or not st.session_state.songs:
    st.session_state.songs = [
        {
            "id": 1,
            "title": "Neela Nilave",
            "artist": "Kapil Kapilan, Sam C.S.",
            "genre": "Malayalam Pop / Melody",
            "mood": "Romantic / Euphoric",
            "cover": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=600&auto=format&fit=crop&q=80",
            "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        },
        {
            "id": 2,
            "title": "Illuminati",
            "artist": "Sushin Shyam, Dabzee",
            "genre": "Hip-Hop / Electronic",
            "mood": "High Energy / Party",
            "cover": "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=600&auto=format&fit=crop&q=80",
            "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
        },
        {
            "id": 3,
            "title": "Katchi Sera",
            "artist": "Sai Abhyankkar",
            "genre": "Indie Pop",
            "mood": "Catchy / Happy",
            "cover": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=600&auto=format&fit=crop&q=80",
            "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
        },
        {
            "id": 4,
            "title": "Aalaporaan Thamizhan",
            "artist": "A.R. Rahman, Kailash Kher",
            "genre": "Folk / Anthem",
            "mood": "Motivational / Power",
            "cover": "https://images.unsplash.com/photo-1459749411175-04bf5292ceea?w=600&auto=format&fit=crop&q=80",
            "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
        }
    ]

st.title("User Dashboard")
st.markdown("Browse tailored recommendations by genre and mood vibe.")
st.write("---")

# Sidebar Filters
with st.sidebar:
    st.header("Filter Feed")
    genres = ["All"] + sorted(list(set(s["genre"] for s in st.session_state.songs)))
    selected_genre = st.selectbox("Genre", genres)
    
    moods = ["All"] + sorted(list(set(s["mood"] for s in st.session_state.songs)))
    selected_mood = st.selectbox("Mood", moods)

filtered = [
    s for s in st.session_state.songs
    if (selected_genre == "All" or s["genre"] == selected_genre) and
       (selected_mood == "All" or s["mood"] == selected_mood)
]

st.markdown(f"**Showing {len(filtered)} Tracks**")

cols = st.columns(2)
for idx, song in enumerate(filtered):
    with cols[idx % 2]:
        st.markdown(f"""
            <div class="song-card">
                <div class="song-title">{song['title']}</div>
                <div class="artist-name">Artist: {song['artist']}</div>
                <div style="margin-bottom: 12px;">
                    <span class="badge badge-genre">{song['genre']}</span>
                    <span class="badge badge-mood">{song['mood']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.image(song["cover"], use_container_width=True)
        st.audio(song["audio"], format="audio/mp3")
        st.write("")