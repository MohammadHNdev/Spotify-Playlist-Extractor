# basic_usage.py - نحوه استفاده ساده

"""
این فایل نشون میده چطور از کتابخانه استفاده کنی
برای شروع، فقط همین کدا رو کپی کن!
"""

from spotify_extractor import SpotifyExtractor

def simple_example():
    """مثال ساده - فقط ۵ خط کد!"""
    
    # NOTE: قبل از اجرا، اینارو تنظیم کن:
    # export SPOTIFY_CLIENT_ID="your_client_id_here"  
    # export SPOTIFY_CLIENT_SECRET="your_client_secret_here"
    
    # یا می‌تونی مستقیم بدی:
    # extractor = SpotifyExtractor("your_client_id", "your_client_secret")
    
    try:
        # ساخت extractor
        extractor = SpotifyExtractor()
        
        # URL پلی‌لیست (این یه نمونه‌س، خودت عوضش کن)
        playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"
        
        # استخراج آهنگ‌ها
        print("در حال استخراج...")
        tracks = extractor.extract_tracks(playlist_url)
        
        # نمایش نتیجه
        print(f"✅ {len(tracks)} آهنگ پیدا شد!")
        
        # ذخیره به فایل
        filename = extractor.save_to_txt(tracks, "my_playlist.txt")
        print(f"💾 ذخیره شد: {filename}")
        
        # نمایش ۳ آهنگ اول
        print("\n🎵 نمونه آهنگ‌ها:")
        for i, track in enumerate(tracks[:3]):
            print(f"{i+1}. {track['name']} - {track['artist']}")
    
    except Exception as e:
        print(f"❌ خطا: {e}")
        print("\nبرای راهنمای تنظیم API، اینجا رو ببین:")
        print("https://developer.spotify.com/dashboard")

def get_playlist_info_example():
    """مثال گرفتن اطلاعات پلی‌لیست"""
    
    extractor = SpotifyExtractor()
    playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"
    
    try:
        # اطلاعات کلی
        info = extractor.get_playlist_info(playlist_url)
        
        print("📋 اطلاعات پلی‌لیست:")
        print(f"   نام: {info['name']}")
        print(f"   سازنده: {info['owner']}")
        print(f"   تعداد آهنگ: {info['total_tracks']}")
        
        if info['image_url']:
            print(f"   تصویر: {info['image_url']}")
    
    except Exception as e:
        print(f"خطا: {e}")

def save_different_formats():
    """ذخیره در فرمت‌های مختلف"""
    
    extractor = SpotifyExtractor()
    playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"
    
    try:
        # استخراج با جزئیات کامل
        tracks = extractor.extract_tracks(playlist_url, include_details=True)
        
        # ذخیره در فرمت‌های مختلف  
        txt_file = extractor.save_to_txt(tracks, "playlist.txt")
        csv_file = extractor.save_to_csv(tracks, "playlist.csv") 
        json_file = extractor.save_to_json(tracks, "playlist.json")
        
        print(f"✅ فایل‌ها ذخیره شدند:")
        print(f"   📝 متن: {txt_file}")
        print(f"   📊 CSV: {csv_file}")
        print(f"   📋 JSON: {json_file}")
    
    except Exception as e:
        print(f"خطا: {e}")

def get_stats_example():
    """مثال گرفتن آمار"""
    
    extractor = SpotifyExtractor()
    playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd"
    
    try:
        tracks = extractor.extract_tracks(playlist_url)
        stats = extractor.get_stats(tracks)
        
        print("📊 آمار پلی‌لیست:")
        print(f"   کل آهنگ‌ها: {stats['total_tracks']}")
        print(f"   خواننده‌های مختلف: {stats['unique_artists']}")
        
        if stats['top_artist']:
            print(f"   محبوب‌ترین: {stats['top_artist'][0]} ({stats['top_artist'][1]} آهنگ)")
        
        print("\n🎤 ۵ خواننده برتر:")
        for artist, count in list(stats['artists_count'].items())[:5]:
            print(f"   {artist}: {count} آهنگ")
    
    except Exception as e:
        print(f"خطا: {e}")

if __name__ == "__main__":
    print("🎵 نمونه‌های استفاده از Spotify Extractor")
    print("=" * 50)
    
    # اجرای مثال‌ها
    print("\n1️⃣ مثال ساده:")
    simple_example()
    
    print("\n2️⃣ اطلاعات پلی‌لیست:")
    get_playlist_info_example()
    
    print("\n3️⃣ فرمت‌های مختلف:")
    save_different_formats()
    
    print("\n4️⃣ آمار پلی‌لیست:")
    get_stats_example()