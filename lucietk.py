import telebot

print("bu kod @BenYakup tarafından yazıldı")

bot = telebot.TeleBot("6347172241:AAE5pVT6ASZuE9Kd4gicFGF4ZeayPrR1EGY")

@bot.message_handler(func=lambda message: message.text.startswith("@everyone"))
def handle_everyone(message):

    chat_id = message.chat.id
    group_info = bot.get_chat(chat_id)
    group_members = group_info.get("members", [])

    member_names = [member.user.first_name for member in group_members]

    members_message = ", ".join(member_names)

    bot.reply_to(message, f"Grup üyeleri: {members_message}")

bot.polling()
