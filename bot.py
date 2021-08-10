# try:
#   import unzip_requirements
# except ImportError:
#   pass

import json
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler, dispatcher, Updater
from handlers.handlers import start, echo, unknown, help, about, rel

# bot = Bot(token = "1914281995:AAFE9G4PkzUg7yTuRwQSDky5w0r1hQ7tBJY")
# dispatcher = Dispatcher(bot, None)
# dispatcher.add_handler(CommandHandler("start", start))
# dispatcher.add_handler(CommandHandler("about", about))
# dispatcher.add_handler(CommandHandler("rel", rel))
# dispatcher.add_handler(CommandHandler("help", help))
# dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
# dispatcher.add_handler(MessageHandler(Filters.command, unknown))

def main () :
  updater = Updater("1914281995:AAFE9G4PkzUg7yTuRwQSDky5w0r1hQ7tBJY", use_context=True)
  dp = updater.dispatcher

  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("about", about))
  dp.add_handler(CommandHandler("rel", rel))
  dp.add_handler(CommandHandler("help", help))
  dp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
  dp.add_handler(MessageHandler(Filters.command, unknown))

  updater.start_polling()
  updater.idle()

# def lambda_handler (event, context) :
#     dispatcher.process_update(Update.de_json(json.loads(event["body"]), bot))
#     return {"statusCode": 200}

if __name__ == '__main__':
    main()