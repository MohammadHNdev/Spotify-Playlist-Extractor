# cli.py - رابط خط فرمان

import argparse
import sys
import os
from .core import SpotifyExtractor
from .helpers import is_valid_spotify_url, get_env_credentials

def display_welcome():
    """پیام خوشامد"""
    print("🎵 Spotify Playlist Extractor CLI")
    print("=" * 40)

def setup_args():
    """تنظیم argument parser"""
    parser = argparse.ArgumentParser(
        description="استخراج پلی‌لیست‌های اسپاتیفای از خط فرمان",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
نمونه استفاده:
  spotify-extract https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd
  spotify-extract -f json -o my_playlist.json [URL]
  spotify-extract --stats [URL]
        """
    )
    
    parser.add_argument(
        'url',
        help='URL پلی‌لیست اسپاتیفای'
    )
    
    parser.add_argument(
        '-f', '--format',
        choices=['txt', 'csv', 'json'],
        default='txt',
        help='فرمت خروجی (پیش‌فرض: txt)'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='نام فایل خروجی'
    )
    
    parser.add_argument(
        '--stats',
        action='store_true',
        help='نمایش آمار پلی‌لیست'
    )
    
    parser.add_argument(
        '--info-only',
        action='store_true', 
        help='فقط اطلاعات کلی پلی‌لیست'
    )
    
    parser.add_argument(
        '--client-id',
        help='Spotify Client ID (اختیاری)'
    )
    
    parser.add_argument(
        '--client-secret',
        help='Spotify Client Secret (اختیاری)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='نمایش جزئیات بیشتر'
    )
    
    return parser

def check_credentials(args):
    """بررسی credentials"""
    if args.client_id and args.client_secret:
        return args.client_id, args.client_secret
    
    # چک متغیرهای محیطی
    env_creds = get_env_credentials()
    if env_creds['valid']:
        return env_creds['client_id'], env_creds['client_secret']
    
    print("❌ خطا: Spotify API credentials یافت نشد!")
    print("\nروش‌های تنظیم:")
    print("1. متغیرهای محیطی:")
    print("   export SPOTIFY_CLIENT_ID='your_client_id'")
    print("   export SPOTIFY_CLIENT_SECRET='your_client_secret'")
    print("\n2. پارامترهای خط فرمان:")
    print("   --client-id YOUR_ID --client-secret YOUR_SECRET")
    print("\n3. ساخت App در: https://developer.spotify.com/dashboard")
    
    return None, None

def main():
    """تابع اصلی CLI"""
    parser = setup_args()
    args = parser.parse_args()
    
    if args.verbose:
        display_welcome()
    
    # بررسی URL
    if not is_valid_spotify_url(args.url):
        print(f"❌ URL نامعتبر: {args.url}")
        print("نمونه URL معتبر: https://open.spotify.com/playlist/...")
        sys.exit(1)
    
    # بررسی credentials
    client_id, client_secret = check_credentials(args)
    if not client_id or not client_secret:
        sys.exit(1)
    
    try:
        # ایجاد extractor
        if args.verbose:
            print("🔗 اتصال به Spotify API...")
        
        extractor = SpotifyExtractor(client_id, client_secret)
        
        # اطلاعات پلی‌لیست
        if args.info_only:
            print("📋 در حال دریافت اطلاعات پلی‌لیست...")
            info = extractor.get_playlist_info(args.url)
            
            print(f"\n📝 نام: {info['name']}")
            print(f"👤 سازنده: {info['owner']}")  
            print(f"🎵 تعداد آهنگ: {info['total_tracks']}")
            
            return
        
        # استخراج آهنگ‌ها
        if args.verbose:
            print("🎵 در حال استخراج آهنگ‌ها...")
        
        tracks = extractor.extract_tracks(args.url, include_details=True)
        
        if not tracks:
            print("❌ هیچ آهنگی یافت نشد!")
            sys.exit(1)
        
        print(f"✅ {len(tracks)} آهنگ پیدا شد!")
        
        # نمایش آمار
        if args.stats:
            stats = extractor.get_stats(tracks)
            print(f"\n📊 آمار:")
            print(f"   کل آهنگ‌ها: {stats['total_tracks']}")
            print(f"   خواننده‌های منحصربه‌فرد: {stats['unique_artists']}")
            if stats['top_artist']:
                print(f"   محبوب‌ترین خواننده: {stats['top_artist'][0]} ({stats['top_artist'][1]} آهنگ)")
        
        # ذخیره فایل
        if not args.info_only:
            if args.verbose:
                print(f"💾 ذخیره در فرمت {args.format.upper()}...")
            
            if args.format == 'csv':
                saved_file = extractor.save_to_csv(tracks, args.output or f"playlist_tracks.csv")
            elif args.format == 'json':
                saved_file = extractor.save_to_json(tracks, args.output or f"playlist_tracks.json")  
            else:
                saved_file = extractor.save_to_txt(tracks, args.output or f"playlist_tracks.txt")
            
            print(f"✅ فایل ذخیره شد: {saved_file}")
    
    except Exception as e:
        print(f"❌ خطا: {e}")  
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()