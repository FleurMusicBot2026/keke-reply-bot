import random
import time
from pyrogram import Client, filters

api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_BOT_TOKEN"

app = Client("keke-reply-bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# 🔥 smart brain replies
positive = ["အိုကေ 👍", "ကောင်းတယ် 😎", "ဟုတ်ပြီ 👌", "သိပြီ 😆"]
question = ["ဟုတ်တယ် 👍", "မသေချာဘူး 🤔", "ရှင်းပြပေးမယ် 👇", "စောင့်ပါ ⏳"]
funny = ["😂😂", "ဟားဟား 😆", "မင်းကတော်တယ် 😎", "အရမ်းကောင်းတယ် 🔥"]
normal = ["ဟေ့ 👋", "ဘာလိုချင်လဲ 😏", "ဆက်ပြောပါ 🤖", "နားလည်တယ် 👍"]

# 🟢 /start
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(
        "👋 Keke AI Bot ကြိုဆိုပါတယ် 🤖\n\nစာပို့ရင် smart reply ပြန်မယ် 😎"
    )

# 🔁 AI-style reply engine
@app.on_message(filters.text)
def smart_ai(client, message):
    text = message.text.lower()

    time.sleep(1)

    user = message.from_user.first_name if message.from_user else "သူငယ်ချင်း"

    # 🎯 logic brain
    if "?" in text:
        reply = random.choice(question)

    elif any(w in text for w in ["good", "nice", "ok", "ကောင်း"]):
        reply = random.choice(positive)

    elif any(e in text for e in ["😂", "😆", "lol"]):
        reply = random.choice(funny)

    else:
        reply = random.choice(normal)

    message.reply_text(f"{user} 👤\n{reply}")

print("🔥 Keke AI Bot v2 Running...")
app.run()
