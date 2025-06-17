# import gradio as gr
# import yt_dlp
# import os
# import uuid

# # Create downloads directory
# DOWNLOAD_DIR = "downloads"
# os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# # Download logic
# def download_video(url):
#     try:
#         unique_id = str(uuid.uuid4())
#         output_path = os.path.join(DOWNLOAD_DIR, f"{unique_id}.%(ext)s")

#         ydl_opts = {
#             'format': 'bestvideo+bestaudio/best',
#             'outtmpl': output_path,
#         }

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=True)
#             filename = ydl.prepare_filename(info)
#             title = info.get("title", "No Title")
#             thumbnail = info.get("thumbnail", None)

#         return f"✅ '{title}' downloaded successfully!", filename, thumbnail or None

#     except Exception as e:
#         return f"❌ Error: {str(e)}", None, None

# # ---------------------- 💅 Custom CSS ----------------------
# custom_css = """
# body {
#     background: linear-gradient(120deg, #1e1e2f, #121218);
#     font-family: 'Segoe UI', sans-serif;
#     color: #f5f5f5;
# }

# #main {
#     max-width: 700px;
#     margin: 40px auto;
#     padding: 40px;
#     border-radius: 20px;
#     background: rgba(30, 30, 30, 0.8);
#     backdrop-filter: blur(8px);
#     box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
#     border: 1px solid rgba(255, 255, 255, 0.05);
# }

# h1 {
#     text-align: center;
#     font-size: 2.2em;
#     margin-bottom: 0.3em;
#     color: #00aaff;
# }

# p.slogan {
#     text-align: center;
#     font-size: 1.1em;
#     color: #bbbbbb;
# }

# .gr-button {
#     background-color: #00aaff !important;
#     color: #fff !important;
#     border-radius: 12px !important;
#     padding: 14px 26px !important;
#     font-size: 16px !important;
#     font-weight: bold;
#     transition: background 0.2s ease-in-out;
# }
# .gr-button:hover {
#     background-color: #008ecc !important;
# }

# input, textarea {
#     background-color: #2b2b2b !important;
#     border-radius: 10px !important;
#     color: #ffffff !important;
#     border: 1px solid #444 !important;
# }

# .gr-image, .gr-file {
#     border-radius: 14px !important;
#     border: 1px solid #444;
#     margin-top: 10px;
# }

# .footer-note {
#     text-align: center;
#     font-size: 13px;
#     color: #999;
#     margin-top: 30px;
# }
# """

# # ---------------------- 🧱 Gradio UI ----------------------
# with gr.Blocks(css=custom_css) as app:
#     with gr.Column(elem_id="main"):
#         gr.Markdown("<h1>📥 StreamSnatch Pro</h1>")
#         gr.Markdown("<p class='slogan'>Snatch your streams. Smoothly. Securely.</p>")

#         url_input = gr.Textbox(label="🔗 Paste Video URL", placeholder="https://...")
#         download_btn = gr.Button("🎬 Download Video")

#         status_output = gr.Textbox(label="Status", interactive=False)
#         thumbnail_output = gr.Image(label="🎞️ Thumbnail Preview", interactive=False)
#         file_output = gr.File(label="📁 Downloaded File")

#         gr.Markdown("""
#         <div class="footer-note">
#         ✅ Supports YouTube, TikTok, Instagram, Facebook, Twitter<br>
#         🚫 Private/restricted videos not supported
#         </div>
#         """)

#         download_btn.click(fn=download_video,
#                            inputs=[url_input],
#                            outputs=[status_output, file_output, thumbnail_output])


# app.launch(share=True)

import gradio as gr
import yt_dlp
import os

# Create downloads directory
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Download logic
def download_video(url):
    try:
        output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")  # Save as title.ext

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': output_path,
            'merge_output_format': 'mp4',
            'noplaylist': True,
            'nocheckcertificate': True,
            'cachedir': False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            title = info.get("title", "No Title")
            thumbnail = info.get("thumbnail", None)

        return f"✅ '{title}' downloaded successfully!", filename, thumbnail or None

    except Exception as e:
        return f"❌ Error: {str(e)}", None, None


# ---------------------- 💅 Custom CSS ----------------------
custom_css = """
body {
    background: linear-gradient(120deg, #1e1e2f, #121218);
    font-family: 'Segoe UI', sans-serif;
    color: #f5f5f5;
}
#main {
    max-width: 700px;
    margin: 40px auto;
    padding: 40px;
    border-radius: 20px;
    background: rgba(30, 30, 30, 0.8);
    backdrop-filter: blur(8px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.05);
}
h1 {
    text-align: center;
    font-size: 2.2em;
    margin-bottom: 0.3em;
    color: #00aaff;
}
p.slogan {
    text-align: center;
    font-size: 1.1em;
    color: #bbbbbb;
}
.gr-button {
    background-color: #00aaff !important;
    color: #fff !important;
    border-radius: 12px !important;
    padding: 14px 26px !important;
    font-size: 16px !important;
    font-weight: bold;
    transition: background 0.2s ease-in-out;
}
.gr-button:hover {
    background-color: #008ecc !important;
}
input, textarea {
    background-color: #2b2b2b !important;
    border-radius: 10px !important;
    color: #ffffff !important;
    border: 1px solid #444 !important;
}
.gr-image, .gr-file {
    border-radius: 14px !important;
    border: 1px solid #444;
    margin-top: 10px;
}
.footer-note {
    text-align: center;
    font-size: 13px;
    color: #999;
    margin-top: 30px;
}
"""

# ---------------------- 🧱 Gradio UI ----------------------
with gr.Blocks(css=custom_css) as app:
    with gr.Column(elem_id="main"):
        gr.Markdown("<h1>📥 StreamSnatch Pro</h1>")
        gr.Markdown("<p class='slogan'>Snatch your streams. Smoothly. Securely.</p>")

        url_input = gr.Textbox(label="🔗 Paste Video URL", placeholder="https://...")
        download_btn = gr.Button("🎬 Download Video")

        status_output = gr.Textbox(label="Status", interactive=False)
        thumbnail_output = gr.Image(label="🎞️ Thumbnail Preview", interactive=False)
        file_output = gr.File(label="📁 Downloaded File")

        gr.Markdown("""
        <div class="footer-note">
        ✅ Supports YouTube, TikTok, Instagram, Facebook, Twitter<br>
        🚫 Private/restricted videos requiring CAPTCHA or login are not supported without cookies
        </div>
        """)

        download_btn.click(fn=download_video,
                           inputs=[url_input],
                           outputs=[status_output, file_output, thumbnail_output])

app.launch(share=True)
