

# اولین برنامه ام برای گرفتن لیست آهنگای اسپاتیفای
# امیدوارم کار کنه چون واقعا نمیدونم چیکار دارم میکنم
# ولی اینترنت گفت اینجوری باید بنویسم

import requests
import json
import sys
import os
import argparse
import base64
import time

# اینا credential های اسپاتیفایه که از سایت اسپاتیفای گرفتم
# نمیدونم چرا دوتا کلید میخواد ولی خب همینه
CLIENT_ID = "2418ea40feb745118a1187ecd6dfde7c"
CLIENT_SECRET = "24d2c291409d448a8aed94ca2dd1f61f"

def get_access_token():
    # خب اول باید یه access token بگیرم از اسپاتیفای
    # تو مستندات نوشته بود اینجوری باید بکنم، امیدوارم کار کنه
    auth_url = "https://accounts.spotify.com/api/token"
    
    # باید کلیدای من رو به base64 تبدیل کنم
    # چرا base64؟ نمیدونم ولی همه همینو گفتن
    client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_header = base64.b64encode(client_credentials.encode()).decode()
    
    # حالا باید header هارو درست کنم
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # و این data هم باید بفرستم
    data = {
        "grant_type": "client_credentials"
    }
    
    # حالا بریم ببینم کار میکنه یا نه
    try:
        response = requests.post(auth_url, headers=headers, data=data)
        if response.status_code == 200:
            token_info = response.json()
            access_token = token_info["access_token"]
            return access_token
        else:
            print("خطا: نتونستم token بگیرم")
            return None
    except Exception as error:
        print(f"یه مشکلی پیش اومد: {error}")
        return None

def extract_playlist_id_from_url(playlist_url):
    # باید از URL پلی لیست فقط همون ID رو بکشم بیرون
    # مثلا از این: https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd
    # فقط این قسمت میخوام: 37i9dQZF1DX0XUsuxWHRQd
    
    if "playlist/" in playlist_url:
        # URL رو تیکه تیکه میکنم
        url_parts = playlist_url.split("playlist/")
        if len(url_parts) > 1:
            playlist_id = url_parts[1]
            # بعضی وقتا آخر URL یه چیزای اضافه داره مثل ?si=...
            # اونارو باید پاک کنم
            if "?" in playlist_id:
                playlist_id = playlist_id.split("?")[0]
            return playlist_id
    
    # اگه اینجا رسیدیم یعنی URL اشتباهه
    return None

def get_playlist_info(playlist_id, token):
    # این تابع باید اطلاعات پلی لیست رو بگیره
    # اسمش، سازندش و اینا
    spotify_api_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    
    # باید token رو تو header بذارم
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    try:
        response = requests.get(spotify_api_url, headers=headers)
        if response.status_code == 200:
            playlist_data = response.json()
            return playlist_data
        else:
            print(f"نتونستم اطلاعات پلی لیست رو بگیرم. کد خطا: {response.status_code}")
            return None
    except Exception as error:
        print(f"یه مشکلی پیش اومد: {error}")
        return None

def get_all_tracks_from_playlist(playlist_id, token):
    # اینجا باید همه آهنگای پلی لیست رو بگیرم
    # مشکل اینه که اسپاتیفای فقط ۱۰۰ تا آهنگ میده هر بار
    # پس باید تو یه حلقه برم تا همش رو بگیرم، حوصله ندارم ولی مجبورم
    
    track_list = []
    api_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    
    # باز باید header رو درست کنم
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # تا وقتی URL داره میرم جلو
    while api_url:
        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                response_data = response.json()
                track_items = response_data.get("items", [])
                
                # حالا باید هرکدوم از آهنگا رو بررسی کنم
                for track_item in track_items:
                    track_data = track_item.get("track")
                    if track_data and track_data.get("name"):
                        # اسم آهنگ
                        song_name = track_data.get("name", "نامشخص")
                        
                        # خوانندگان - گاهی یه آهنگ چندتا خواننده داره
                        artist_list = []
                        for artist_info in track_data.get("artists", []):
                            artist_name = artist_info.get("name", "خواننده نامشخص")
                            artist_list.append(artist_name)
                        all_artists = ", ".join(artist_list)
                        
                        # لینک اسپاتیفای آهنگ
                        spotify_url = track_data.get("external_urls", {}).get("spotify", "")
                        
                        # همه چی رو تو یه dictionary میذارم
                        single_track = {
                            "name": song_name,
                            "artist": all_artists,
                            "url": spotify_url
                        }
                        
                        track_list.append(single_track)
                
                # ببینم صفحه بعدی داره یا نه
                api_url = response_data.get("next")
            else:
                print(f"خطا تو گرفتن آهنگا. کد خطا: {response.status_code}")
                break
        except Exception as error:
            print(f"یه چیزی خراب شد: {error}")
            break
    
    return track_list

def save_tracks_to_file(track_list, output_filename, file_format):
    # این تابع باید همه آهنگا رو تو فایل ذخیره کنه
    # کاربر میتونه بگه چه فرمتی میخواد
    
    if file_format == "txt":
        # ساده ترین حالت - یه فایل متنی معمولی
        try:
            with open(output_filename, "w", encoding="utf-8") as text_file:
                for track in track_list:
                    # هر آهنگ رو تو یه خط مینویسم
                    text_file.write(f"{track['name']} - {track['artist']}\n")
                    text_file.write(f"{track['url']}\n")
                    text_file.write("\n")  # یه خط خالی هم میذارم بینشون
            print(f"تموم شد! {len(track_list)} تا آهنگ رو ذخیره کردم تو {output_filename}")
        except Exception as error:
            print(f"خطا تو ذخیره فایل متنی: {error}")
    
    elif file_format == "json":
        # فرمت JSON برای کسایی که بلدن برنامه نویسی
        try:
            with open(output_filename, "w", encoding="utf-8") as json_file:
                json.dump(track_list, json_file, indent=2, ensure_ascii=False)
            print(f"آفرین! {len(track_list)} تا آهنگ رو به صورت JSON ذخیره کردم")
        except Exception as error:
            print(f"مشکل تو ذخیره JSON: {error}")
    
    elif file_format == "csv":
        # CSV برای اکسل و اینا
        try:
            import csv  # این کتابخونه رو میخوام
            with open(output_filename, "w", newline="", encoding="utf-8") as csv_file:
                csv_writer = csv.writer(csv_file)
                # اول سر ستون ها رو مینویسم
                csv_writer.writerow(["نام آهنگ", "خواننده", "لینک اسپاتیفای"])
                # بعد همه آهنگا رو
                for track in track_list:
                    csv_writer.writerow([track["name"], track["artist"], track["url"]])
            print(f"عالی! {len(track_list)} تا آهنگ رو به فرمت CSV ذخیره کردم")
        except Exception as error:
            print(f"خطا تو ذخیره CSV: {error}")

def main():
    # اینجا تابع اصلی برنامه هست که همه چیز رو اجرا میکنه
    # اول باید argument ها رو تنظیم کنم
    parser = argparse.ArgumentParser(description="برنامه ساده من برای گرفتن لیست آهنگای اسپاتیفای")
    parser.add_argument("url", help="لینک پلی لیست اسپاتیفایی که میخوای استخراج کنی")
    parser.add_argument("-f", "--format", choices=["txt", "json", "csv"], 
                       default="txt", help="چه فرمتی میخوای فایل رو ذخیره کنی (پیشفرض txt هست)")
    parser.add_argument("-o", "--output", help="اسم دلخواه برای فایل خروجی")
    
    # حالا ببینم کاربر چی گفته
    user_args = parser.parse_args()
    
    print("شروع کردم استخراج پلی لیست...")
    
    # اول باید از URL پلی لیست، ID رو بکشم بیرون
    playlist_id = extract_playlist_id_from_url(user_args.url)
    if not playlist_id:
        print("خطا: این لینک درست نیست، مطمئنی از اسپاتیفایه؟")
        sys.exit(1)
    
    print(f"پیدا کردم! ID پلی لیست: {playlist_id}")
    
    # حالا باید token بگیرم از اسپاتیفای
    print("دارم token میگیرم از اسپاتیفای...")
    my_access_token = get_access_token()
    if not my_access_token:
        print("خطا: نتونستم token بگیرم، یه مشکلی هست")
        sys.exit(1)
    
    # بذار ببینم این پلی لیست چیه
    print("دارم اطلاعات پلی لیست رو میگیرم...")
    playlist_info = get_playlist_info(playlist_id, my_access_token)
    if not playlist_info:
        print("خطا: نتونستم اطلاعات پلی لیست رو بگیرم")
        sys.exit(1)
    
    # به کاربر نشون میدم چی پیدا کردم
    playlist_name = playlist_info.get("name", "پلی لیست نامشخص")
    playlist_owner = playlist_info.get("owner", {}).get("display_name", "نامشخص")
    total_tracks = playlist_info.get("tracks", {}).get("total", 0)
    print(f"نام پلی لیست: {playlist_name}")
    print(f"سازنده: {playlist_owner}")
    print(f"تعداد آهنگ: {total_tracks}")
    
    # حالا برم همه آهنگا رو بگیرم
    print("دارم همه آهنگا رو استخراج میکنم...")
    all_tracks = get_all_tracks_from_playlist(playlist_id, my_access_token)
    
    if not all_tracks:
        print("خطا: هیچ آهنگی پیدا نکردم تو این پلی لیست")
        sys.exit(1)
    
    print(f"یول! {len(all_tracks)} تا آهنگ پیدا کردم!")
    
    # حالا باید بفهمم اسم فایل خروجی چی باشه
    if user_args.output:
        output_filename = user_args.output
    else:
        # از اسم پلی لیست یه اسم فایل میسازم
        # باید کاراکترای مشکل ساز رو حذف کنم
        safe_playlist_name = ""
        for character in playlist_name:
            if character.isalnum() or character in (' ', '-', '_'):
                safe_playlist_name += character
        safe_playlist_name = safe_playlist_name.strip()
        output_filename = f"{safe_playlist_name}.{user_args.format}"
    
    # حالا همه آهنگا رو ذخیره میکنم
    print(f"دارم ذخیره میکنم تو {output_filename}...")
    save_tracks_to_file(all_tracks, output_filename, user_args.format)
    
    print("تمووووم شد! برو چک کن فایلت رو.")

if __name__ == "__main__":
    main()
