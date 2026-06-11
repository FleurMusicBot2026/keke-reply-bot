# keke-reply-botimport random
import time
from pyrogram import Client, filters

api_id = "32729712"
api_hash = "ba2d17f6fd71db636d1599ddc7f22248
"
bot_token = "8935324081:AAGCGdS3yVmdRe_U84pr5HLPflHkFMaJuVg"

app = Client("keke-reply-bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

replies = [
    "ဟေ့ 👋 မင်းစာကို ငါမြင်တယ် 😆",
    "ဘာလိုချင်တာလဲ 😏",
    "အိုကေ 👍 သိပြီနော်",
    "ဟားဟား 😄 မင်းပြောတာနားလည်တယ်",
    "စိတ်ဝင်စားစရာပဲ 🤔",
    "ပြန်နေတယ်နော် ⏳"
]

@app.on_message(filters.text)
def auto_reply(client, message):
    time.sleep(1.5)

    user = message.from_user.first_name if message.from_user else "သူငယ်ချင်း"

    text = random.choice(replies)

    message.reply_text(f"{user} 👤\n{text}")

print("Keke Reply Bot run နေပြီ...")
app.run()
