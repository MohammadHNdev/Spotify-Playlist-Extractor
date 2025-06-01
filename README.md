# SpotTrack - Spotify Playlist Extractor (Web App)

![Python Project Icon](https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg)


---

## درباره SpotTrack

SpotTrack یک اپلیکیشن وب قدرتمند و کاربرپسند است که با استفاده از Streamlit و پایتون ساخته شده است. هدف این اپلیکیشن، ساده‌سازی فرآیند استخراج و مدیریت آهنگ‌ها از پلی‌لیست‌های اسپاتیفای است. این برنامه به کاربران امکان می‌دهد تا به راحتی لینک یک پلی‌لیست اسپاتیفای را وارد کرده، تمام آهنگ‌های موجود در آن را مشاهده، مرتب‌سازی، آهنگ‌های خاصی را انتخاب و لینک‌های دانلود مستقیم را برای [ربات تلگرام SpotTrack](https://t.me/SpotTrack_Bot) تولید کنند.

این اپلیکیشن با هدف ارائه تجربه‌ای یکپارچه برای علاقه‌مندان به موسیقی طراحی شده است که مایلند آهنگ‌های اسپاتیفای مورد علاقه خود را به طور کارآمد سازماندهی و دانلود کنند.

---

## About SpotTrack

SpotTrack is a powerful and user-friendly web application built with Streamlit and Python, designed to simplify the process of extracting and managing tracks from Spotify playlists. It allows users to easily input a Spotify playlist URL, view all the tracks within it, sort them, select specific tracks, and generate direct download links for the [SpotTrack Telegram Bot](https://t.me/SpotTrack_Bot).

This application aims to provide a seamless experience for music enthusiasts who wish to organize and download their favorite Spotify tracks efficiently.

---

## ویژگی‌ها

*   **رابط کاربری بصری:** یک رابط وب تمیز و با قابلیت ناوبری آسان که توسط Streamlit ارائه شده است.
*   **استخراج پلی‌لیست اسپاتیفای:** جزئیات جامع (نام، هنرمند، آلبوم، URL) را برای تمام آهنگ‌های موجود در یک پلی‌لیست اسپاتیفای مشخص دریافت می‌کند.
*   **سیستم احراز هویت:** سیستم احراز هویت ساده مبتنی بر نام کاربری برای کاربران تایید شده.
*   **نمایش جزئیات پلی‌لیست:** نام پلی‌لیست، صاحب، تصویر کاور و تعداد کل آهنگ‌ها را نمایش می‌دهد.
*   **مدیریت آهنگ‌ها:**
    *   **مرتب‌سازی:** آهنگ‌ها را بر اساس نام، هنرمند یا آلبوم مرتب کنید.
    *   **صفحه‌بندی:** با استفاده از کنترل‌های صفحه‌بندی آسان، در پلی‌لیست‌های بزرگ پیمایش کنید.
    *   **انتخاب:** آهنگ‌های تکی را انتخاب کنید یا لینک‌های دانلود را برای تمام آهنگ‌ها دریافت کنید.
*   **ادغام با ربات تلگرام:** لینک‌های مستقیم برای دانلود آهنگ‌های انتخاب شده را از طریق [ربات تلگرام SpotTrack](https://t.me/SpotTrack_Bot) تولید می‌کند.
*   **دانلود انبوه:** یک فایل متنی (`.txt`) حاوی تمام URLهای آهنگ‌های انتخاب شده یا تمام URLهای آهنگ‌های پلی‌لیست را دانلود کنید.
*   **طراحی واکنش‌گرا:** برای تجربه کاربری یکسان، با اندازه‌های مختلف صفحه نمایش سازگار است.

---

## Features

*   **Intuitive User Interface:** A clean and easy-to-navigate web interface powered by Streamlit.
*   **Spotify Playlist Extraction:** Fetches comprehensive details (name, artist, album, URL) for all tracks in a given Spotify playlist.
*   **Authentication System:** Simple username-based authentication for approved users.
*   **Playlist Details Display:** Shows playlist name, owner, cover image, and total track count.
*   **Track Management:**
    *   **Sorting:** Sort tracks by Name, Artist, or Album.
    *   **Pagination:** Browse through large playlists with easy-to-use pagination controls.
    *   **Selection:** Select individual tracks or download links for all tracks.
*   **Telegram Bot Integration:** Generates direct links to download selected tracks via the [SpotTrack Telegram Bot](https://t.me/SpotTrack_Bot).
*   **Bulk Download:** Download a `.txt` file containing all selected track URLs or all track URLs from the playlist.
*   **Responsive Design:** Adapts to various screen sizes for a consistent user experience.

---

## شروع به کار (برای توسعه‌دهندگان)

برای راه‌اندازی و اجرای این پروژه به صورت محلی، مراحل زیر را دنبال کنید:

### پیش‌نیازها

*   پایتون 3.8 به بالا
*   `pip` (مدیر بسته پایتون)

### 1. کلون کردن مخزن

ابتدا، این مخزن را به سیستم محلی خود کلون کنید

2. تنظیم متغیرهای محیطی
برای دسترسی به داده‌های اسپاتیفای، به اعتبارنامه‌های API اسپاتیفای (Client ID و Client Secret) نیاز دارید.

به داشبورد توسعه‌دهندگان اسپاتیفای بروید.
وارد شوید یا ثبت‌نام کنید.
برای ایجاد یک اپلیکیشن جدید، روی "Create an App" کلیک کنید.
Client ID و Client Secret خود را یادداشت کنید.
یک فایل به نام .env در دایرکتوری اصلی پروژه خود (جایی که app.py قرار دارد) ایجاد کنید.
اعتبارنامه‌های خود را به صورت زیر به فایل .env اضافه کنید:
SPOTIFY_CLIENT_ID="your_spotify_client_id_here"
SPOTIFY_CLIENT_SECRET="your_spotify_client_secret_here"
مهم: فایل .env در .gitignore قرار داده شده است تا از آپلود شدن اعتبارنامه‌های حساس شما به گیت‌هاب جلوگیری شود.
3. نصب وابستگی‌ها
تمام پکیج‌های پایتون مورد نیاز را با استفاده از pip نصب کنید:

bash
Copy Code
pip install -r requirements.txt
4. اجرای اپلیکیشن
پس از نصب وابستگی‌ها، می‌توانید اپلیکیشن Streamlit را اجرا کنید:

bash
Copy Code
streamlit run app.py
اپلیکیشن در مرورگر وب پیش‌فرض شما باز می‌شود، معمولاً در آدرس http://localhost:8501.

Getting Started (For Developers)
To set up and run this project locally, follow these steps:

Prerequisites
Python 3.8+
pip (Python package installer)
1. Clone the Repository
First, clone this repository to your local machine:

bash
Copy Code
git clone https://github.com/MohammadHNDev/SpotTrack-Streamlit-App.git # Replace with your actual repository URL
cd SpotTrack-Streamlit-App
2. Set up Environment Variables
You need Spotify API credentials (Client ID and Client Secret) to access Spotify's data.

Go to the Spotify for Developers Dashboard.
Log in or sign up.
Click "Create an App" to create a new application.
Note down your Client ID and Client Secret.
Create a file named .env in the root directory of your project (where app.py is located).
Add your credentials to the .env file like this:
SPOTIFY_CLIENT_ID="your_spotify_client_id_here"
SPOTIFY_CLIENT_SECRET="your_spotify_client_secret_here"
Important: The .env file is included in .gitignore to prevent your sensitive credentials from being uploaded to GitHub.
3. Install Dependencies
Install all required Python packages using pip:

bash
Copy Code
pip install -r requirements.txt
4. Run the Application
Once dependencies are installed, you can run the Streamlit application:

bash
Copy Code
streamlit run app.py
The application will open in your default web browser, usually at http://localhost:8501.

ساختار پروژه
.
├── app.py                  # فایل اصلی اپلیکیشن Streamlit
├── auth.py                 # منطق احراز هویت کاربر را مدیریت می‌کند
├── requirements.txt        # لیست وابستگی‌های پایتون
├── .env.example            # فایل نمونه .env برای متغیرهای محیطی
├── .gitignore              # فایل‌ها/دایرکتوری‌هایی که باید در گیت نادیده گرفته شوند را مشخص می‌کند
├── styles/                 # دایرکتوری برای فایل‌های CSS
│   └── style.css           # CSS سفارشی برای استایل‌دهی به اپلیکیشن
├── spotify_logo.png        # لوگوی اسپاتیفای که به عنوان آیکون صفحه استفاده می‌شود
├── placeholder.png         # تصویر جایگزین برای کاورهای آلبوم گم‌شده
└── README.md               # همین فایل README
Project Structure
.
├── app.py                  # Main Streamlit application file
├── auth.py                 # Handles user authentication logic
├── requirements.txt        # List of Python dependencies
├── .env.example            # Example .env file for environment variables
├── .gitignore              # Specifies files/directories to ignore in Git
├── styles/                 # Directory for CSS files
│   └── style.css           # Custom CSS for styling the app
├── spotify_logo.png        # Spotify logo used as page icon
├── placeholder.png         # Placeholder image for missing album covers
└── README.md               # This README file
احراز هویت
اپلیکیشن از یک سیستم احراز هویت ساده مبتنی بر نام کاربری استفاده می‌کند که در فایل auth.py تعریف شده است.

کاربران تایید شده: کاربرانی که در لیست APPROVED_USERS در auth.py قرار دارند، می‌توانند وارد شوند.
کاربر ادمین: ADMIN_USERNAME در auth.py دارای امتیازات ادمین است (اگرچه در رابط کاربری فعلی به طور کامل استفاده نشده است).
Authentication
The application uses a simple username-based authentication system defined in auth.py.

Approved Users: Users listed in APPROVED_USERS in auth.py can log in.
Admin User: The ADMIN_USERNAME in auth.py has admin privileges (though not fully utilized in the current UI).
مشارکت
مشارکت‌ها مورد استقبال قرار می‌گیرند! اگر پیشنهاداتی برای بهبود، رفع اشکال یا ویژگی‌های جدید دارید، لطفاً یک Issue باز کنید یا یک Pull Request ارسال کنید.

Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to open an issue or submit a pull request.

تماس
این پروژه توسط محمد حسین نوروزی توسعه یافته است.

تلگرام: DiamondcodeTech
برای هرگونه سوال یا همکاری، با من در تماس باشید!

Contact
This project was developed by Mohammad Hossein Norouzi.

Telegram: DiamondcodeTech
Feel free to reach out for any questions or collaborations!


