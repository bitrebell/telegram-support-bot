from telegram.ext import Updater

from handlers import setup_dispatcher
from settings import TELEGRAM_TOKEN, HEROKU_APP_NAME, PORT

# Setup bot handlers
updater = Updater(TELEGRAM_TOKEN)

dp = updater.dispatcher
dp = setup_dispatcher(dp)



updater.start_polling()
updater.idle()

