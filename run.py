from highrise.__main__ import *
import time
import traceback

bot_file_name = "main"
bot_class_name = "Bot"
room_id = "65b55167841db902ae2ff618"
bot_token = "adec5dbe443466033099a5461f3e11d87d7d7582d111436e6536bdee0b99dfae"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occourred: {e}")
        traceback.print_exc()
        time.sleep(5)
