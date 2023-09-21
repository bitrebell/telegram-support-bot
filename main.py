from telegram.ext import Updater

from handlers import setup_dispatcher
from settings import TELEGRAM_TOKEN, HEROKU_APP_NAME, PORT

# Setup bot handlers

TELEGRAM_TOKEN = "6412441114:AAF5nri-Vw1kcwvMn4JT4KzXH2Fjpxv3HHA"
PORT = '8443'

updater = Updater(TELEGRAM_TOKEN)

dp = updater.dispatcher
dp = setup_dispatcher(dp)



updater.start_polling()
updater.idle()

