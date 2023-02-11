import time
import telebot
from key import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

# Responde a los comandos
@bot.message_handler(commands=['start'])
def send_welcome(message):
	chat_action(message)
	bot.reply_to(message, "Booenas") # Cita el mensaje y le responde

#mandar una foto
@bot.message_handler(commands=['foto'])
def send_foto(message):
	chat_action(message)
	foto = open("img\op.jpg", "rb" ) # guarda la foto
	bot.send_photo(message.chat.id, foto, "La mas bonita de todas") # Manda la foto con una cita

#mandar un archio
@bot.message_handler(commands=['archivo'])
def send_foto(message):
	chat_action(message)
	archivo = open("archivo\Clase 13-06- Simulación sistema de control automatico de jardin- Práctica.pdf", "rb" ) # guarda el archivo
	bot.send_document(message.chat.id, archivo, caption="Pa el indoor") # Manda la foto con una cita

# Responde a todos los mensajes
@bot.message_handler(content_types=['text'])
def message_texto(message):
	if message.text.startswith('/'):
		chat_action(message)
		bot.send_message(message.chat.id , 'Comando inexistente')
	else:
		chat_action(message)
		x= bot.send_message(message.chat.id , '<u>Tranqui rey</u>' , parse_mode='html')
		time.sleep(2)
		bot.edit_message_text("<u>Nada</u>", message.chat.id, x.message_id, parse_mode='html')# edita los mensajes
		time.sleep(2)
		bot.delete_message(message.chat.id, message.message_id)# elimina el mensaje

def chat_action(message): # Figura cuando esta escribiendo el bot
	bot.send_chat_action(message.chat.id, 'typing')


bot.infinity_polling()
