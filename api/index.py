from flask import Flask, request
import requests
import os

app = Flask(__name__)

# دریافت اطلاعات از متغیرهای محیطی ورسل
BOT_TOKEN = os.environ.get('BOT_TOKEN')
MY_ID = os.environ.get('MY_ID')

@app.route('/', methods=['POST', 'GET'])
def webhook():
    # اگر تلگرام پیامی به ربات بفرستد (متد POST)
    if request.method == 'POST':
        try:
            update = request.get_json()
            
            # بررسی اینکه آیا آپدیت شامل متن است یا خیر
            if "message" in update and "text" in update["message"]:
                text = update["message"]["text"]
                
                # ارسال پیام دریافت شده به آیدی عددی شما (پیوی)
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                payload = {
                    "chat_id": MY_ID,
                    "text": f"🎁 **گیفت تایید شده:**\n\n{text}",
                    "parse_mode": "Markdown"
                }
                requests.post(url, json=payload)
                
        except Exception as e:
            print("Error:", e)
            
        return "OK", 200

    # اگر آدرس سایت ورسل را در مرورگر باز کنید این پیام را می‌بینید
    return "✅ Bot is running on Vercel successfully!", 200

# فقط برای تست در محیط لوکال
if __name__ == '__main__':
    app.run(debug=True)
