import streamlit as st

st.set_page_config(
    page_title="VibeStream | Admin Portal",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #171026 50%, #0d1527 100%);
        color: #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if "songs" not in st.session_state:
    st.session_state.songs = []

st.title("Administrator Control Center")

# Admin Login Check
if not st.session_state.admin_logged_in:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.subheader("Admin Verification")
        admin_pass = st.text_input("Enter Admin Password", type="password")
        if st.button("Unlock Admin Panel", use_container_width=True):
            if admin_pass == "admin123":
                st.session_state.admin_logged_in = True
                st.success("Authorized successfully!")
                st.rerun()
            else:
                st.error("Invalid Password! Use: admin123")
    st.stop()

col_h1, col_h2 = st.columns([4, 1])
with col_h1:
    st.caption("Status: Logged in as Administrator")
with col_h2:
    if st.button("Log Out Admin"):
        st.session_state.admin_logged_in = False
        st.rerun()

st.write("---")

# Add Track Form
with st.expander("Upload / Add New Track to Catalog", expanded=True):
    with st.form("admin_add_form"):
        title = st.text_input("Track Title")
        artist = st.text_input("Artist Names")
        genre = st.text_input("Genre (e.g., Synthwave, Indie)")
        mood = st.text_input("Mood (e.g., Chill, Euphoric)")
        cover = st.text_input("Album Cover Image URL", value="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=600")
        audio = st.text_input("Audio URL (MP3 format)", value="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        
        submitted = st.form_submit_button("Publish Track")
        if submitted:
            if title and artist:
                new_track = {
                    "id": len(st.session_state.songs) + 1,
                    "title": title,
                    "artist": artist,
                    "genre": genre,
                    "mood": mood,
                    "cover": cover,
                    "audio": audio
                }
                st.session_state.songs.append(new_track)
                st.success(f"Track '{title}' added to the live catalog!")
                st.rerun()
            else:
                st.error("Title and Artist are mandatory.")

# Manage Catalog
st.subheader("Live Catalog Management")
if not st.session_state.songs:
    st.info("No tracks currently stored in library.")
else:
    for song in st.session_state.songs:
        row1, row2, row3 = st.columns([3, 2, 1])
        with row1:
            st.write(f"{song['title']} - {song['artist']}")
        with row2:
            st.caption(f"{song['genre']} | {song['mood']}")
        with row3:
            if st.button("Delete", key=f"del_{song['id']}"):
                st.session_state.songs = [s for s in st.session_state.songs if s["id"] != song["id"]]
                st.rerun()