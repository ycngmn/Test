from flask import Flask, request
import logging
from telegram.ext import CommandHandler, Dispatcher, Updater

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create an instance of the bot with the token
bot_token = '6399873051:AAHnJF3b3uaLeBgRqKKRcjPI1VB0Q_zIp80'
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Define a command handler for the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, welcome to the bot!")

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

# Define the webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK'

if __name__ == '__main__':
    # Set the webhook
    webhook_url = 'YOUR_WEBHOOK_URL'
    updater.bot.setWebhook(webhook_url)
    # Start the Flask web server
    app.run(port=5000)
