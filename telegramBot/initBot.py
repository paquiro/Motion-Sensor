# -*- coding: utf-8 -*-

import time
import sys
from commandsBot import *

reload(sys)
sys.setdefaultencoding("utf-8")

bot.polling(none_stop=True) # Bot must continue if it fails
while True:
    time.sleep(300)
