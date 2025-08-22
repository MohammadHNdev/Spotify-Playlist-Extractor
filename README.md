Simple Spotify Playlist Extractor
==================================

This is a simple command line tool to extract tracks from Spotify playlists.

Requirements:
- Python 3.6 or higher
- requests library

Installation:
1. Install Python from python.org
2. Open command prompt (cmd)
3. Navigate to this folder
4. Run: pip install -r requirements.txt

Usage:
python main.py [playlist_url]

Options:
-f, --format    Output format: txt, json, or csv (default: txt)
-o, --output    Output filename (optional)

Examples:
python main.py https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd
python main.py -f json https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd
python main.py -o my_playlist.txt https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd

Note: The Spotify API credentials are already included in the code.