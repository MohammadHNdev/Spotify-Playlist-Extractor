# spotify_extractor package
# ساده‌ترین راه برای استخراج پلی‌لیست اسپاتیفای

__version__ = "1.0.0"
__author__ = "Mohammad Hossein Norouzi"
__email__ = "mohammadhn.dev@gmail.com"

# import اصلی برای راحتی استفاده
from .core import SpotifyExtractor
from .helpers import extract_playlist_id, format_duration, clean_filename

# برای استفاده آسان
__all__ = [
    "SpotifyExtractor",
    "extract_playlist_id", 
    "format_duration",
    "clean_filename"
]

# پیام خوشامد
def get_info():
    """اطلاعات کتابخانه رو برمی‌گردونه"""
    return {
        "name": "spotify-playlist-extractor",
        "version": __version__,
        "author": __author__,
        "description": "استخراج ساده پلی‌لیست‌های اسپاتیفای"
    }