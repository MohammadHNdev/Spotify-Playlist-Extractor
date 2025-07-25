#!/usr/bin/env python3
"""
Advanced Spotify Playlist Extractor Examples
Demonstrates various usage patterns and features
"""

import os
import sys
from pathlib import Path

# Add the parent directory to sys.path to import spotify_extractor
sys.path.insert(0, str(Path(__file__).parent.parent))

from spotify_extractor import SpotifyExtractor, get_info

def setup_credentials():
    """Setup Spotify API credentials from environment or user input"""
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    
    if not client_id or not client_secret:
        print("Spotify API credentials not found in environment variables.")
        print("Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET")
        print("Or provide them below:")
        
        if not client_id:
            client_id = input("Enter Spotify Client ID: ").strip()
        if not client_secret:
            client_secret = input("Enter Spotify Client Secret: ").strip()
    
    return client_id, client_secret

def example_basic_extraction():
    """Example 1: Basic playlist extraction"""
    print("\n=== Example 1: Basic Playlist Extraction ===")
    
    try:
        client_id, client_secret = setup_credentials()
        extractor = SpotifyExtractor(client_id, client_secret)
        
        # Test playlist URL
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"
        
        print(f"Extracting playlist: {playlist_url}")
        tracks = extractor.extract_tracks(playlist_url)
        
        if tracks:
            print(f"✅ Successfully extracted {len(tracks)} tracks!")
            
            # Show first few tracks
            for i, track in enumerate(tracks[:3]):
                print(f"{i+1}. {track['name']} - {track['artist']}")
        else:
            print("❌ No tracks found or extraction failed")
            
    except Exception as e:
        print(f"❌ Error in basic extraction: {e}")

def example_save_formats():
    """Example 2: Save in different formats"""
    print("\n=== Example 2: Save in Multiple Formats ===")
    
    try:
        client_id, client_secret = setup_credentials()
        extractor = SpotifyExtractor(client_id, client_secret)
        
        # Sample tracks for demo
        sample_tracks = [
            {
                'name': 'Sample Song 1',
                'artist': 'Artist One',
                'album': 'Album One',
                'url': 'https://open.spotify.com/track/example1',
                'album_image': 'https://example.com/image1.jpg'
            },
            {
                'name': 'Sample Song 2', 
                'artist': 'Artist Two',
                'album': 'Album Two',
                'url': 'https://open.spotify.com/track/example2',
                'album_image': 'https://example.com/image2.jpg'
            }
        ]
        
        # Save in different formats
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        
        # TXT format
        txt_file = output_dir / "playlist.txt"
        extractor.save_to_txt(sample_tracks, str(txt_file))
        print(f"✅ Saved as TXT: {txt_file}")
        
        # CSV format
        csv_file = output_dir / "playlist.csv"
        extractor.save_to_csv(sample_tracks, str(csv_file))
        print(f"✅ Saved as CSV: {csv_file}")
        
        # JSON format
        json_file = output_dir / "playlist.json"
        extractor.save_to_json(sample_tracks, str(json_file))
        print(f"✅ Saved as JSON: {json_file}")
        
    except Exception as e:
        print(f"❌ Error in save formats: {e}")

def example_helper_functions():
    """Example 3: Using helper functions"""
    print("\n=== Example 3: Helper Functions ===")
    
    from spotify_extractor import extract_playlist_id, format_duration, clean_filename
    
    # Test URLs
    test_urls = [
        "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd",
        "https://open.spotify.com/playlist/1A2B3C4D5E6F7G8H9I0J?si=abc123",
        "spotify:playlist:37i9dQZF1DX0XUsuxWHRQd"
    ]
    
    print("Testing playlist ID extraction:")
    for url in test_urls:
        playlist_id = extract_playlist_id(url)
        print(f"  {url} -> {playlist_id}")
    
    # Test duration formatting
    print("\nTesting duration formatting:")
    durations = [30000, 180000, 245000, 3600000]  # milliseconds
    for ms in durations:
        formatted = format_duration(ms)
        print(f"  {ms}ms -> {formatted}")
    
    # Test filename cleaning
    print("\nTesting filename cleaning:")
    filenames = [
        "Song Name (feat. Artist)",
        "Track/with\\bad*chars?",
        "Normal Song Title",
        "Song: The \"Best\" Version"
    ]
    for filename in filenames:
        cleaned = clean_filename(filename)
        print(f"  '{filename}' -> '{cleaned}'")

def example_error_handling():
    """Example 4: Error handling and edge cases"""
    print("\n=== Example 4: Error Handling ===")
    
    try:
        # Try with invalid credentials
        extractor = SpotifyExtractor("invalid_id", "invalid_secret")
        
        # This should fail gracefully
        tracks = extractor.extract_tracks("https://open.spotify.com/playlist/invalid")
        print(f"Result with invalid credentials: {tracks}")
        
    except Exception as e:
        print(f"✅ Properly caught error: {e}")
    
    # Test with invalid URLs
    from spotify_extractor import extract_playlist_id
    
    invalid_urls = [
        "not_a_url",
        "https://youtube.com/watch?v=abc123",
        "https://open.spotify.com/track/abc123",  # track instead of playlist
        ""
    ]
    
    print("Testing invalid URLs:")
    for url in invalid_urls:
        try:
            result = extract_playlist_id(url)
            print(f"  '{url}' -> {result}")
        except Exception as e:
            print(f"  '{url}' -> Error: {e}")

def main():
    """Run all examples"""
    print("🎵 Spotify Playlist Extractor - Advanced Examples")
    print("=" * 50)
    
    # Show package info
    info = get_info()
    print(f"Package: {info['name']} v{info['version']}")
    print(f"Author: {info['author']}")
    print(f"Description: {info['description']}")
    
    # Run examples
    example_basic_extraction()
    example_save_formats()
    example_helper_functions() 
    example_error_handling()
    
    print("\n🎯 All examples completed!")
    print("Check the 'output' directory for generated files.")

if __name__ == "__main__":
    main()