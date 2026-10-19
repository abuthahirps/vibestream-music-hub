import streamlit as st

st.set_page_config(
    page_title="VibeStream | User Dashboard",
    page_icon="🎧",
    layout="wide"
)

# Custom UI Styling
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

if "songs" not in st.session_state:
    st.info("Loading music database... Please return to Home if not loaded.")
    st.stop()

st.title("🎧 Stream & Discover Tracks")
st.markdown("Browse tailored recommendations by genre and mood vibe.")
st.write("---")

# Sidebar Filters
with st.sidebar:
    st.header("🎛️ Filter Feed")
    genres = ["All"] + sorted(list(set(s["genre"] for s in st.session_state.songs)))
    selected_genre = st.selectbox("Genre", genres)
    
    moods = ["All"] + sorted(list(set(s["mood"] for s in st.session_state.songs)))
    selected_mood = st.selectbox("Mood", moods)

# Filter Logic
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
                <div class="artist-name">🎙️ {song['artist']}</div>
                <div style="margin-bottom: 12px;">
                    <span class="badge badge-genre">{song['genre']}</span>
                    <span class="badge badge-mood">{song['mood']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.image(song["cover"], use_container_width=True)
        st.audio(song["audio"], format="audio/mp3")
        st.write("")