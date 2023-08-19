import telebot
bot = telebot.TeleBot("6424779417:AAEnJUqpuS8yBblzGRJOhQ-r4h2Y_ituLRA")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 't':
        bot.send_photo(message.chat.id, photo='https://imgur.com/qRdbSWx')
    if message.text.strip() == 's':
        bot.send_photo(message.chat.id, photo="https://imgur.com/Nwm4i03",caption="Hello, World!")
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

bot.polling(none_stop=True, interval=0)

