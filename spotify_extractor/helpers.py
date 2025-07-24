# helpers.py - توابع کمکی

import re
import os
from typing import Optional

def extract_playlist_id(url: str) -> Optional[str]:
    """
    از URL پلی‌لیست، ID رو جدا می‌کنه
    مثال: https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd
    """
    if not url:
        return None
    
    # الگوهای مختلف URL
    patterns = [
        r'playlist/([a-zA-Z0-9]+)',  # URL معمولی
        r'spotify:playlist:([a-zA-Z0-9]+)',  # URI format
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None

def clean_filename(filename: str) -> str:
    """
    نام فایل رو تمیز می‌کنه از کاراکترهای غیرمجاز
    """
    if not filename:
        return "untitled.txt"
    
    # کاراکترهای غیرمجاز
    invalid_chars = '<>:"/\\|?*'
    
    clean_name = filename
    for char in invalid_chars:
        clean_name = clean_name.replace(char, '_')
    
    # حذف space های اضافی
    clean_name = re.sub(r'\s+', ' ', clean_name.strip())
    
    return clean_name

def format_duration(ms: int) -> str:
    """
    مدت زمان رو از میلی‌ثانیه به دقیقه:ثانیه تبدیل می‌کنه
    """
    if not ms or ms < 0:
        return "00:00"
    
    seconds = ms // 1000
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    
    return f"{minutes:02d}:{remaining_seconds:02d}"

def validate_spotify_credentials(client_id: str, client_secret: str) -> bool:
    """
    اعتبار API credentials رو چک می‌کنه
    """
    if not client_id or not client_secret:
        return False
    
    # چک طول و فرمت کلی
    if len(client_id) != 32 or len(client_secret) != 32:
        return False
    
    # چک اینکه فقط کاراکترهای مجاز داشته باشه
    valid_chars = re.compile(r'^[a-zA-Z0-9]+$')
    
    return bool(valid_chars.match(client_id) and valid_chars.match(client_secret))

def get_env_credentials():
    """
    credentials رو از متغیرهای محیطی می‌گیره
    """
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    
    return {
        'client_id': client_id,
        'client_secret': client_secret,
        'valid': validate_spotify_credentials(client_id or '', client_secret or '')
    }

def format_track_info(track_data: dict, template: str = "{name} - {artist}") -> str:
    """
    اطلاعات آهنگ رو طبق الگو فرمت می‌کنه
    """
    try:
        return template.format(**track_data)
    except (KeyError, ValueError):
        return f"{track_data.get('name', 'نامشخص')} - {track_data.get('artist', 'نامشخص')}"

def batch_process_urls(urls: list, batch_size: int = 5):
    """
    لیست URL ها رو دسته‌بندی می‌کنه برای پردازش دسته‌ای
    """
    for i in range(0, len(urls), batch_size):
        yield urls[i:i + batch_size]

def is_valid_spotify_url(url: str) -> bool:
    """
    چک می‌کنه URL اسپاتیفای معتبر هست یا نه
    """
    if not url or not isinstance(url, str):
        return False
    
    spotify_patterns = [
        r'https?://open\.spotify\.com/playlist/[a-zA-Z0-9]+',
        r'spotify:playlist:[a-zA-Z0-9]+'
    ]
    
    return any(re.match(pattern, url.strip()) for pattern in spotify_patterns)