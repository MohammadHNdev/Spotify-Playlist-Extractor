# batch_processing.py - پردازش دسته‌ای چندین پلی‌لیست

"""
برای زمانی که چندین پلی‌لیست داری و می‌خوای همه رو یکجا پردازش کنی
"""

from spotify_extractor import SpotifyExtractor
from spotify_extractor.helpers import batch_process_urls, is_valid_spotify_url
import time
import os

def process_multiple_playlists():
    """پردازش چندین پلی‌لیست"""
    
    # لیست URL های پلی‌لیست‌ها
    playlist_urls = [
        "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd",
        "https://open.spotify.com/playlist/37i9dQZF1DXcBWFJPTuWp6", 
        "https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwABJCa",
        # بقیه URL هات رو اینجا اضافه کن
    ]
    
    extractor = SpotifyExtractor()
    results = []
    
    print(f"🚀 شروع پردازش {len(playlist_urls)} پلی‌لیست...")
    
    for i, url in enumerate(playlist_urls, 1):
        try:
            # بررسی معتبر بودن URL
            if not is_valid_spotify_url(url):
                print(f"❌ URL {i} نامعتبر: {url}")
                continue
            
            print(f"\n📋 پردازش پلی‌لیست {i}/{len(playlist_urls)}")
            
            # گرفتن اطلاعات
            info = extractor.get_playlist_info(url)
            print(f"   نام: {info['name']}")
            print(f"   تعداد آهنگ: {info['total_tracks']}")
            
            # استخراج آهنگ‌ها
            tracks = extractor.extract_tracks(url, include_details=True)
            
            # ذخیره با نام مناسب
            safe_name = info['name'].replace('/', '_').replace('\\', '_')[:50]
            filename = f"{safe_name}_tracks.json"
            saved_file = extractor.save_to_json(tracks, filename)
            
            result = {
                'url': url,
                'name': info['name'], 
                'tracks_count': len(tracks),
                'file': saved_file,
                'success': True
            }
            
            results.append(result)
            print(f"   ✅ ذخیره شد: {saved_file}")
            
            # مکث کوتاه برای API rate limit
            time.sleep(1)
            
        except Exception as e:
            print(f"   ❌ خطا در پلی‌لیست {i}: {e}")
            results.append({
                'url': url,
                'success': False,
                'error': str(e)
            })
    
    # خلاصه نتایج
    print(f"\n📊 خلاصه نتایج:")
    successful = [r for r in results if r.get('success')]
    failed = [r for r in results if not r.get('success')]
    
    print(f"   ✅ موفق: {len(successful)}")
    print(f"   ❌ ناموفق: {len(failed)}")
    print(f"   📝 کل آهنگ‌ها: {sum(r.get('tracks_count', 0) for r in successful)}")
    
    return results

def process_from_file():
    """خوندن URL ها از فایل و پردازش"""
    
    # فایل حاوی URL ها (هر خط یک URL)
    urls_file = "playlist_urls.txt"
    
    # ساخت فایل نمونه اگه وجود نداره
    if not os.path.exists(urls_file):
        sample_urls = [
            "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd",
            "https://open.spotify.com/playlist/37i9dQZF1DXcBWFJPTuWp6",
            "# خطوط شروع شده با # نادیده گرفته میشن",
            "# URL های خودت رو اینجا اضافه کن"
        ]
        
        with open(urls_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(sample_urls))
        
        print(f"📝 فایل نمونه ساخته شد: {urls_file}")
        print("URL های خودت رو اضافه کن و دوباره اجرا کن!")
        return
    
    # خوندن URL ها
    try:
        with open(urls_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # فیلتر کردن خطوط معتبر
        urls = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and is_valid_spotify_url(line):
                urls.append(line)
        
        if not urls:
            print("❌ هیچ URL معتبری در فایل پیدا نشد!")
            return
        
        print(f"📁 {len(urls)} URL از فایل خوانده شد")
        
        # پردازش دسته‌ای
        extractor = SpotifyExtractor()
        all_tracks = []
        
        for batch in batch_process_urls(urls, batch_size=3):
            print(f"\n🔄 پردازش دسته {len(batch)} پلی‌لیست...")
            
            for url in batch:
                try:
                    tracks = extractor.extract_tracks(url)
                    all_tracks.extend(tracks)
                    print(f"   ✅ {len(tracks)} آهنگ از {url[:50]}...")
                except Exception as e:
                    print(f"   ❌ خطا: {e}")
            
            # مکث بین دسته‌ها
            time.sleep(2)
        
        # ذخیره همه آهنگ‌ها در یک فایل
        if all_tracks:
            merged_file = extractor.save_to_json(all_tracks, "merged_playlists.json")
            print(f"\n💾 همه آهنگ‌ها ذخیره شد: {merged_file}")
            print(f"📊 کل آهنگ‌ها: {len(all_tracks)}")
        
    except Exception as e:
        print(f"❌ خطا در خوندن فایل: {e}")

def remove_duplicates_example():
    """حذف آهنگ‌های تکراری"""
    
    extractor = SpotifyExtractor()
    
    # فرض کن چندین پلی‌لیست داری با آهنگ‌های مشترک
    urls = [
        "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd",
        "https://open.spotify.com/playlist/37i9dQZF1DXcBWFJPTuWp6"
    ]
    
    all_tracks = []
    
    # جمع‌آوری همه آهنگ‌ها
    for url in urls:
        try:
            tracks = extractor.extract_tracks(url)
            all_tracks.extend(tracks)
            print(f"✅ {len(tracks)} آهنگ اضافه شد")
        except Exception as e:
            print(f"❌ خطا: {e}")
    
    print(f"\n📊 کل آهنگ‌ها (با تکراری): {len(all_tracks)}")
    
    # حذف تکراری‌ها بر اساس URL
    unique_tracks = {}
    for track in all_tracks:
        url = track.get('url')
        if url and url not in unique_tracks:
            unique_tracks[url] = track
    
    unique_list = list(unique_tracks.values())
    print(f"🎯 آهنگ‌های منحصربه‌فرد: {len(unique_list)}")
    print(f"🗑️ تکراری‌های حذف شده: {len(all_tracks) - len(unique_list)}")
    
    # ذخیره لیست تمیز
    clean_file = extractor.save_to_json(unique_list, "unique_tracks.json")
    print(f"💾 فایل تمیز: {clean_file}")

if __name__ == "__main__":
    print("🔄 پردازش دسته‌ای پلی‌لیست‌ها")
    print("=" * 50)
    
    choice = input("\nانتخاب کن:\n1. پردازش چندین پلی‌لیست\n2. پردازش از فایل\n3. حذف تکراری‌ها\n\nانتخاب (1-3): ")
    
    if choice == "1":
        process_multiple_playlists()
    elif choice == "2": 
        process_from_file()
    elif choice == "3":
        remove_duplicates_example()
    else:
        print("انتخاب نامعتبر!")