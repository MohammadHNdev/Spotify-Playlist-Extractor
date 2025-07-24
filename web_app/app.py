import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import pandas as pd
import base64
import urllib.parse
import time
import math

# --- Import functions and data from auth.py ---
from auth import check_credentials, is_admin, ADMIN_USERNAME, APPROVED_USERS
# Note: ADMIN_PASSWORD is no longer imported as it's not used for checking
# ----------------------------------------------------

# Load environment variables from .env file
load_dotenv()

# --- Get Spotify API Credentials from Environment Variables ---
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
# ------------------------------------------------------------

# --- Telegram Bot Username ---
TELEGRAM_BOT_USERNAME = "SpotTrack_Bot" # Replace with your bot's actual username
# -----------------------------

# --- Pagination Settings ---
ITEMS_PER_PAGE = 20 # Number of tracks to display per page
# ---------------------------

# --- Function to load CSS ---
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file not found: {file_name}")

# --- Removed clipboard.js injection functions ---
# def inject_clipboard_js_library(): ...
# def inject_clipboard_js_init(): ...


# --- Function to authenticate with Spotify (can be cached) ---
@st.cache_resource
def authenticate_spotify():
    """Authenticates with Spotify API using Client Credentials Flow."""
    if not CLIENT_ID or not CLIENT_SECRET:
        st.error(
            "Error: Spotify API credentials (Client ID and Secret) are not set correctly."
            "Please make sure SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET are set in your environment variables or .env file."
        )
        return None
    try:
        auth_manager = SpotifyClientCredentials(
            client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        return sp
    except Exception as e:
        st.error(f"Error authenticating with Spotify API: {e}")
        return None

# --- Function to extract playlist details and tracks (cache this data) ---
@st.cache_data(ttl=3600)
def get_playlist_data(_sp, playlist_url):
    """
    Extracts playlist details and track details from a Spotify playlist URL.

    Args:
        _sp: Authenticated Spotify API client.
        playlist_url (str): The URL of the Spotify playlist.

    Returns:
        tuple: (playlist_details_dict, list_of_track_details_dicts) or (None, None) if error.
    """
    if _sp is None:
        return None, None

    try:
        # Extract playlist ID from URL
        if "spotify.com/playlist/" in playlist_url:
            playlist_id = playlist_url.split('/')[-1].split('?')[0]
        elif "spotify:playlist:" in playlist_url:
            playlist_id = playlist_id = playlist_url.split(':')[-1]
        else:
            st.error(
                f"Error: Invalid Spotify playlist URL format: {playlist_url}")
            return None, None

        st.info(f"Fetching data for playlist ID: {playlist_id}")

        # Get Playlist Details
        playlist_data = _sp.playlist(playlist_id, fields="name,owner(display_name),images,tracks(total)")
        playlist_details = {
            "name": playlist_data.get('name'),
            "owner": playlist_data.get('owner', {}).get('display_name'),
            "image_url": playlist_data.get('images', [{}])[0].get('url') if playlist_data.get('images') else None,
            "total_tracks": playlist_data.get('tracks', {}).get('total')
        }

        # Get Track Details
        track_info_list = []
        # Use a loop to get all tracks, as playlist_items is paginated
        results = _sp.playlist_items(
            playlist_id, fields="items(track(name, artists(name), album(name, images), external_urls.spotify)),next")

        while results:
            for item in results['items']:
                track = item.get('track')
                # Ensure track and essential info exist
                if track and track.get('name') and track.get('artists') and track.get('album') and track.get('external_urls', {}).get('spotify'):
                    track_info = {
                        "name": track['name'],
                        "artist": ", ".join([artist['name'] for artist in track['artists']]),
                        "album": track['album']['name'],
                        "album_image_url": track['album']['images'][0]['url'] if track['album'].get('images') else None,
                        "url": track['external_urls']['spotify']
                    }
                    if track_info["url"]:
                         track_info_list.append(track_info)
            if results['next']:
                results = _sp.next(results)
            else:
                results = None

        return playlist_details, track_info_list

    except Exception as e:
        st.error(f"An error occurred while fetching playlist data: {e}")
        return None, None

# --- Streamlit App ---
# Set page configuration - MUST be the first Streamlit command
st.set_page_config(
    layout="wide",
    page_title="Spotify Playlist Extractor",
    page_icon="spotify_logo.png" # <-- Add the path to your Spotify logo file here
    # Example if in a subfolder: page_icon="assets/spotify_logo.png"
)

# Load custom CSS (This stays here to apply styles to both login and main pages)
load_css("styles/style.css")
# Removed clipboard.js injection calls


# --- Initialize session state variables (These are always initialized at the start) ---
if 'is_authenticated' not in st.session_state:
    st.session_state.is_authenticated = False
if 'logged_in_username' not in st.session_state:
    st.session_state.logged_in_username = None
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

if 'playlist_data' not in st.session_state:
    st.session_state.playlist_data = None
if 'track_info_list' not in st.session_state:
    st.session_state.track_info_list = None
if 'last_playlist_url' not in st.session_state:
    st.session_state.last_playlist_url = ""
if 'sort_by' not in st.session_state:
    st.session_state.sort_by = "Track Name" # Default sort option
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1 # Default page is 1
if 'selected_tracks' not in st.session_state:
    st.session_state.selected_tracks = set() # Use a set to store selected track URLs
# Add state variable to track which link to display in text input
if 'display_copy_link' not in st.session_state:
    st.session_state.display_copy_link = None
# ------------------------------------------------------------


# --- Authentication Logic and Display ---
# If the user is not authenticated, display the login form
if not st.session_state.is_authenticated:
    # You can add a title or description specific to the login page here
    st.title("🔒 Login to Spotify Playlist Extractor")
    st.write("Please enter your username to access the service.")

    # Use columns to center the form (optional, for better appearance)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2: # Display the form in the middle column
        with st.form("login_form"):
            st.subheader("Login Form")
            username = st.text_input("Username")
            # Password field is removed as requested
            login_button = st.form_submit_button("Login")

            if login_button:
                # Use the check_credentials function from auth.py (only passes username)
                if check_credentials(username):
                    st.session_state.is_authenticated = True
                    st.session_state.logged_in_username = username
                    # Use the is_admin function from auth.py
                    st.session_state.is_admin = is_admin(username)
                    st.success(f"Welcome, {username}!") # Show welcome message
                    st.rerun() # Rerun the app to show the main content
                else:
                    st.error("Invalid username. Please try again or contact support.") # More specific error message

        st.markdown("<div style='text-align: center; margin-top: 20px;'>", unsafe_allow_html=True)
        st.write("Only approved users can access this service.")
        st.markdown("</div>", unsafe_allow_html=True)


else: # If the user is authenticated, display the main application content

    # --- Main Application Content (Displayed only for authenticated users) ---

    st.title("🎶 Spotify Playlist Track Extractor") # Main application title
    st.write(f"Welcome, {st.session_state.logged_in_username}!")

    # Display Logout button (optional, in a small column at the top right)
    col_main_title, col_logout = st.columns([4, 1])
    with col_logout:
        if st.button("Logout"):
            # Clear authentication and playlist data from session state
            st.session_state.is_authenticated = False
            st.session_state.logged_in_username = None
            st.session_state.is_admin = False
            st.session_state.playlist_data = None
            st.session_state.track_info_list = None
            st.session_state.last_playlist_url = ""
            st.session_state.sort_by = "Track Name"
            st.session_state.current_page = 1
            st.session_state.selected_tracks = set()
            st.session_state.display_copy_link = None
            st.rerun() # Rerun the app to show the login form


    st.write("Enter the URL of a public Spotify playlist below to extract all track links.")
    st.write("Ready to go! Let DiamondCode.tech take care of extracting your Spotify tracks.")
    st.write(
        '📢 **[Spotify Download Bot](https://t.me/SpotTrack_Bot)** – Instantly download any Spotify track via Telegram!'
    )


    playlist_url_input = st.text_input("Spotify Playlist URL:", "")

    # Authenticate with Spotify when the app starts (cached)
    spotify_client = authenticate_spotify()

    # Check if the extract button was clicked OR if there's a URL and no data yet
    # Also re-extract if the input URL is different from the one currently in session state
    if st.button("Extract Tracks") or (st.session_state.track_info_list is None and playlist_url_input and st.session_state.last_playlist_url != playlist_url_input):

         if not spotify_client:
            st.warning("Spotify API client is not initialized. Please check your credentials.")
         elif playlist_url_input:
            with st.spinner("Extracting playlist data..."):
                # Call the cached function to get all data
                playlist_details, track_info_list = get_playlist_data(spotify_client, playlist_url_input)

                # Store data in session state
                st.session_state.playlist_data = playlist_details
                st.session_state.track_info_list = track_info_list
                st.session_state.last_playlist_url = playlist_url_input # Store the current URL
                st.session_state.sort_by = "Track Name" # Reset sort when new playlist is loaded
                st.session_state.current_page = 1 # Reset page to 1 when new playlist is loaded
                st.session_state.selected_tracks = set() # Clear selected tracks for new playlist
                st.session_state.display_copy_link = None # Clear displayed link


            # No need to re-run the script fully, session state holds the data

         elif not playlist_url_input:
             st.warning("Please enter a Spotify playlist URL.")


    # --- Display Playlist Info and Tracks if data exists in session state ---
    if st.session_state.playlist_data and st.session_state.track_info_list is not None:
        playlist_details = st.session_state.playlist_data
        track_info_list = st.session_state.track_info_list

        if playlist_details and track_info_list:
            st.subheader("Playlist Details:")

            # --- Display Playlist Info ---
            st.markdown('<div class="playlist-info-container">', unsafe_allow_html=True)
            col_img, col_details = st.columns([1, 3])

            with col_img:
                if playlist_details['image_url']:
                    st.image(playlist_details['image_url'], width=150)
                else:
                     st.image("placeholder.png", width=150, caption="No Cover")

            with col_details:
                st.markdown(f"### {playlist_details['name']}</h3>", unsafe_allow_html=True)
                st.write(f"**Owner:** {playlist_details['owner']}")
                st.write(f"**Total Tracks:** {playlist_details['total_tracks']}")

            st.markdown('</div>', unsafe_allow_html=True)
            # --- End Playlist Info ---


            st.subheader("Extracted Track Details:")

            # --- Sorting Options ---
            sort_options = ["Track Name", "Artist", "Album"]
            selected_sort = st.selectbox(
                "Sort by:",
                sort_options,
                index=sort_options.index(st.session_state.sort_by),
                key="sort_selectbox"
            )

            # Update session state if sort option changes
            if selected_sort != st.session_state.sort_by:
                st.session_state.sort_by = selected_sort
                st.session_state.current_page = 1 # Reset to page 1 when sorting changes
                st.session_state.display_copy_link = None # Clear displayed link on sort change
                st.rerun() # Rerun to apply sorting and reset page

            # --- Apply Sorting ---
            if st.session_state.sort_by == "Track Name":
                track_info_list_sorted = sorted(track_info_list, key=lambda x: x['name'])
            elif st.session_state.sort_by == "Artist":
                track_info_list_sorted = sorted(track_info_list, key=lambda x: x['artist'])
            elif st.session_state.sort_by == "Album":
                track_info_list_sorted = sorted(track_info_list, key=lambda x: x['album'])
            else:
                track_info_list_sorted = track_info_list # Default or original order


            # --- Pagination Controls ---
            total_tracks = len(track_info_list_sorted)
            total_pages = math.ceil(total_tracks / ITEMS_PER_PAGE)

            st.write(f"Total Tracks: {total_tracks}")

            if total_pages > 1:
                # Create columns for pagination controls
                col_prev, col_page_info, col_next = st.columns([1, 2, 1])

                with col_prev:
                    if st.session_state.current_page > 1:
                        if st.button("⬅️ Previous Page"):
                            st.session_state.current_page -= 1
                            st.session_state.display_copy_link = None # Clear displayed link on page change
                            st.rerun() # Rerun to show the previous page

                with col_page_info:
                     # Display current page and total pages
                     st.markdown(f"<div style='text-align: center; margin-top: 10px;'>Page <strong>{st.session_state.current_page}</strong> of <strong>{total_pages}</strong></div>", unsafe_allow_html=True)


                with col_next:
                    if st.session_state.current_page < total_pages:
                        if st.button("➡️ Next Page"):
                            st.session_state.current_page += 1
                            st.session_state.display_copy_link = None # Clear displayed link on page change
                            st.rerun() # Rerun to show the next page

                # Calculate start and end index for the current page
                start_index = (st.session_state.current_page - 1) * ITEMS_PER_PAGE
                end_index = start_index + ITEMS_PER_PAGE
                tracks_to_display = track_info_list_sorted[start_index:end_index]
            else:
                # If only one page, display all tracks
                tracks_to_display = track_info_list_sorted


            # --- Display tracks as cards for the current page ---
            num_columns = 4 # Adjust as needed
            # Ensure we don't create more columns than items on the last page
            cols_to_create = min(num_columns, len(tracks_to_display))
            if cols_to_create > 0:
                 columns = st.columns(cols_to_create)
            else:
                 columns = [] # No columns if no tracks to display on this page


            # Iterate through the tracks for the current page
            for index, track_info in enumerate(tracks_to_display):
                # Use modulo with num_columns to cycle through the created columns
                # If cols_to_create is less than num_columns (last page), this still works
                with columns[index % cols_to_create]:
                    st.markdown('<div class="track-card-container">', unsafe_allow_html=True)

                    # --- Add Checkbox for Selection ---
                    track_url = track_info['url']
                    # Check if the current track URL is in the set of selected tracks
                    is_selected = track_url in st.session_state.selected_tracks

                    # Create a checkbox for the track
                    # Use the track URL as the key for uniqueness
                    checkbox_state = st.checkbox(
                        f"Select", # Label for the checkbox (can be empty string if you prefer)
                        value=is_selected, # Set initial state based on session state
                        key=f"select_{track_url}" # Unique key for the checkbox
                    )

                    # Update the session state based on checkbox state
                    if checkbox_state:
                        st.session_state.selected_tracks.add(track_url) # Add to set if checked
                    else:
                        if track_url in st.session_state.selected_tracks:
                            st.session_state.selected_tracks.remove(track_url) # Remove from set if unchecked


                    # Display Album Cover
                    if track_info['album_image_url']:
                        st.image(track_info['album_image_url'], use_container_width=True)
                    else:
                        st.image("placeholder.png", use_container_width=True, caption="No Cover")

                    # Display Track Info
                    st.markdown(f"<h4>{track_info['name']}</h4>", unsafe_allow_html=True)
                    st.write(f"*{track_info['artist']}*")
                    st.write(f"Album: {track_info['album']}")

                    # --- Add Buttons ---
                    # Generate Telegram Bot Download Link
                    encoded_track_url = urllib.parse.quote_plus(track_url)
                    telegram_download_link = f"https://t.me/{TELEGRAM_BOT_USERNAME}?start={encoded_track_url}"

                    # Button to open Telegram link
                    st.link_button(
                        "⬇️ Download from SpotTrack",
                        url=telegram_download_link,
                        help="Click to open Telegram and download via SpotTrack bot"
                    )

                    # --- Copy Link Button (triggers displaying text input) ---
                    # Use a unique key for each button
                    if st.button("📋 Show Link to Copy", key=f"show_copy_btn_{track_url}"):
                        # Set the state variable to the URL of the track whose button was clicked
                        st.session_state.display_copy_link = track_url
                        # No rerun needed here, the text input will appear on the next rerun triggered by the button click


                    # --- Display Text Input for Copying if this track's button was clicked ---
                    # Check if the current track's URL matches the one stored in session state
                    if st.session_state.display_copy_link == track_url:
                        st.text_input(
                            "Copy this link:",
                            value=track_url,
                            key=f"copy_text_{track_url}", # Unique key for the text input
                            help="Select and copy the link manually."
                        )


                    # Close the custom container div
                    st.markdown('</div>', unsafe_allow_html=True)


            # Add a separator before the download all button
            st.markdown("---")

            # --- Download Selected Links Button ---
            # Get the list of selected track URLs
            selected_urls = list(st.session_state.selected_tracks)
            selected_file_content = "\n".join(selected_urls)

            st.subheader("Download Links:")

            # Display count of selected tracks
            st.write(f"Selected Tracks: {len(selected_urls)}")

            # Download button for selected links (only if there are selected tracks)
            if selected_urls:
                 st.download_button(
                    label=f"⬇️ Download {len(selected_urls)} Selected Track Links (.txt)",
                    data=selected_file_content,
                    file_name="selected_tracks.txt",
                    mime="text/plain"
                )
            else:
                 st.info("Select tracks above to enable download for selected.")


            # Download button for all URLs (existing functionality)
            file_content_all = "\n".join([info['url'] for info in track_info_list if info['url']])
            st.download_button(
                label=f"⬇️ Download All {total_tracks} Track Links (.txt)",
                data=file_content_all,
                file_name="all_playlist_tracks.txt", # Changed filename to avoid conflict
                mime="text/plain"
            )


        elif playlist_details and track_info_list is None:
             st.warning("Could not retrieve tracks for this playlist.")
        elif playlist_details is None:
             st.warning("Could not retrieve playlist details.")


    st.markdown("---")
    st.write("Built with ❤️ by Diamond Code · © 2025")

    # --- End of Main Application Content ---

# --- End of Streamlit App ---