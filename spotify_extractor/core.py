# core.py - اصل کتابخونه

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json
import csv
from typing import List, Dict, Optional
from .helpers import extract_playlist_id, clean_filename

class SpotifyExtractor:
    """کلاس اصلی برای کار با پلی‌لیست‌های اسپاتیفای"""
    
    def __init__(self, client_id=None, client_secret=None):
        # اگه نداشت از env میگیره
        self.client_id = client_id or os.getenv("SPOTIFY_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("SPOTIFY_CLIENT_SECRET") 
        self.sp = None
        self.setup_spotify_client()
    
    def setup_spotify_client(self):
        """کلاینت رو راه میندازه"""
        if not self.client_id or not self.client_secret:
            raise ValueError("Client ID و Secret نداری! تو env variables بذارشون")
        
        try:
            credentials_manager = SpotifyClientCredentials(
                client_id=self.client_id,
                client_secret=self.client_secret
            )
            self.sp = spotipy.Spotify(auth_manager=credentials_manager)
        except Exception as error:
            raise ConnectionError(f"نشد وصل بشم به اسپاتیفای: {error}")
    
    def get_playlist_basic_info(self, url_of_playlist):
        """اطلاعات کلی پلی‌لیست"""
        extracted_id = extract_playlist_id(url_of_playlist)
        if not extracted_id:
            raise ValueError("این URL درست نیست")
        
        try:
            # دیتا پلی‌لیست
            data_from_spotify = self.sp.playlist(extracted_id, fields="name,owner(display_name),images,tracks(total)")
            result_info = {
                "name": data_from_spotify.get('name', 'بدون نام'),
                "owner": data_from_spotify.get('owner', {}).get('display_name', 'نامشخص'),
                "image_url": data_from_spotify.get('images', [{}])[0].get('url'),
                "total_tracks": data_from_spotify.get('tracks', {}).get('total', 0)
            }
            return result_info
        except Exception as err:
            raise RuntimeError(f"مشکل تو گرفتن اطلاعات: {err}")
    
    # نام تابع رو عوض کردم
    def get_playlist_info(self, playlist_url):
        return self.get_playlist_basic_info(playlist_url)
    
    def extract_all_tracks(self, url_input, with_details=False):
        """همه آهنگ‌هارو میگیره"""
        id_extracted = extract_playlist_id(url_input)
        if not id_extracted:
            raise ValueError("URL اشتباهه")
        
        list_of_tracks = []
        
        try:
            # شروع گرفتن آهنگ‌ها
            spotify_results = self.sp.playlist_items(
                id_extracted, 
                fields="items(track(name, artists(name), album(name, images), external_urls.spotify)),next"
            )
            
            # حلقه برای همه صفحات
            while spotify_results:
                for single_item in spotify_results['items']:
                    track_data = single_item.get('track')
                    if not track_data or not track_data.get('name'):
                        continue
                    
                    # اطلاعات اصلی
                    info_of_track = {
                        "name": track_data['name'],
                        "artist": ", ".join([a['name'] for a in track_data.get('artists', [])]),
                        "url": track_data.get('external_urls', {}).get('spotify', '')
                    }
                    
                    # اطلاعات بیشتر اگه خواست
                    if with_details:
                        album_info = track_data.get('album', {})
                        info_of_track.update({
                            "album": album_info.get('name', 'نامشخص'),
                            "album_image": album_info.get('images', [{}])[0].get('url'),
                        })
                    
                    # اضافه کردن اگه URL داشت
                    if info_of_track["url"]:
                        list_of_tracks.append(info_of_track)
                
                # صفحه بعدی اگه داشت
                if spotify_results['next']:
                    spotify_results = self.sp.next(spotify_results)
                else:
                    spotify_results = None
                    
        except Exception as error_occurred:
            raise RuntimeError(f"مشکل تو گرفتن آهنگ‌ها: {error_occurred}")
        
        return list_of_tracks
    
    # نام کوتاه‌تر برای راحتی
    def extract_tracks(self, playlist_url, include_details=False):
        return self.extract_all_tracks(playlist_url, include_details)
    
    def write_to_text_file(self, track_list, file_name="playlist_tracks.txt"):
        """تو فایل متنی می‌نویسه"""
        clean_file_name = clean_filename(file_name)
        
        try:
            with open(clean_file_name, 'w', encoding='utf-8') as text_file:
                for single_track in track_list:
                    text_file.write(f"{single_track['name']} - {single_track['artist']}\n")
                    text_file.write(f"{single_track['url']}\n\n")
            return clean_file_name
        except Exception as write_error:
            raise IOError(f"نشد فایل رو بنویسم: {write_error}")
    
    # alias برای سازگاری
    def save_to_txt(self, tracks, filename="playlist_tracks.txt"):
        return self.write_to_text_file(tracks, filename)
    
    def write_csv_format(self, track_data, output_file="playlist_tracks.csv"):
        """تو CSV می‌نویسه"""
        cleaned_name = clean_filename(output_file)
        
        try:
            with open(cleaned_name, 'w', newline='', encoding='utf-8') as csv_file_handle:
                if not track_data:
                    return cleaned_name
                
                csv_writer = csv.DictWriter(csv_file_handle, fieldnames=track_data[0].keys())
                csv_writer.writeheader()
                csv_writer.writerows(track_data)
            return cleaned_name
        except Exception as csv_error:
            raise IOError(f"مشکل تو نوشتن CSV: {csv_error}")
    
    def save_to_csv(self, tracks, filename="playlist_tracks.csv"):
        return self.write_csv_format(tracks, filename)
    
    def export_json_format(self, data_tracks, json_filename="playlist_tracks.json"):
        """JSON میسازه"""
        final_filename = clean_filename(json_filename)
        
        try:
            with open(final_filename, 'w', encoding='utf-8') as json_file:
                json.dump(data_tracks, json_file, indent=2, ensure_ascii=False)
            return final_filename
        except Exception as json_err:
            raise IOError(f"مشکل تو JSON: {json_err}")
    
    def save_to_json(self, tracks, filename="playlist_tracks.json"):
        return self.export_json_format(tracks, filename)
    
    def do_extract_and_save(self, playlist_input_url, format_type="txt", output_filename=None):
        """یکجا استخراج و ذخیره"""
        extracted_tracks = self.extract_all_tracks(playlist_input_url, with_details=True)
        
        if not output_filename:
            info_data = self.get_playlist_basic_info(playlist_input_url) 
            output_filename = f"{info_data['name']}_tracks.{format_type}"
        
        # انتخاب فرمت
        format_lower = format_type.lower()
        if format_lower == "csv":
            return self.write_csv_format(extracted_tracks, output_filename)
        elif format_lower == "json":
            return self.export_json_format(extracted_tracks, output_filename) 
        else:
            return self.write_to_text_file(extracted_tracks, output_filename)
    
    def extract_and_save(self, playlist_url, output_format="txt", filename=None):
        return self.do_extract_and_save(playlist_url, output_format, filename)
    
    def calculate_stats(self, tracks_input):
        """آمار پلی‌لیست"""
        if not tracks_input:
            return {}
        
        # شمارش خواننده‌ها
        artist_counter = {}
        for track_item in tracks_input:
            artist_name = track_item.get('artist', 'نامشخص')
            if artist_name in artist_counter:
                artist_counter[artist_name] += 1
            else:
                artist_counter[artist_name] = 1
        
        # محبوب‌ترین خواننده
        top_artist_data = None
        if artist_counter:
            max_count = 0
            max_artist = None
            for artist, count in artist_counter.items():
                if count > max_count:
                    max_count = count
                    max_artist = artist
            top_artist_data = (max_artist, max_count)
        
        # مرتب کردن لیست خواننده‌ها
        sorted_artists = {}
        sorted_items = sorted(artist_counter.items(), key=lambda x: x[1], reverse=True)
        for artist, count in sorted_items[:10]:
            sorted_artists[artist] = count
        
        return {
            "total_tracks": len(tracks_input),
            "unique_artists": len(artist_counter),
            "top_artist": top_artist_data,
            "artists_count": sorted_artists
        }
    
    def get_stats(self, tracks):
        return self.calculate_stats(tracks)