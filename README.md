# 🎬 Secure Video Downloader (Flask + yt-dlp)

A web-based video downloading tool built using **Flask**, **yt-dlp**, and **Google reCAPTCHA**. This app allows users to securely download high-quality videos from supported platforms through a simple, user-friendly interface.

---

## 🚀 Features

- ✅ Supports high-quality video + audio downloads
- 🔍 Displays video thumbnail preview
- 🔒 Integrated with Invisible Google reCAPTCHA
- 🧼 Sanitizes file names to avoid system conflicts
- 🗂 Downloads saved locally with secure file access
- 🖥 Built with Python, Flask, and yt-dlp

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Video Processing**: yt-dlp
- **Frontend**: HTML, CSS (Jinja2 templating)
- **Security**: Google reCAPTCHA v2 (Invisible)
- **Others**: requests, os, re, urllib

---

## 💡 How It Works

1. User enters a video URL in the form.
2. Google reCAPTCHA is triggered and validated.
3. Video metadata is extracted using yt-dlp.
4. The best quality video + audio is downloaded.
5. A thumbnail is shown and a download link is generated.

---

## ⚙️ How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/asjid12/your-repo-name.git
cd your-repo-name
pip install flask yt-dlp requests
python app.py
