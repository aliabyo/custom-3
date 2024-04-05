from highrise import BaseBot, Position, User, AnchorPosition, GetMessagesRequest
import asyncio, random
from emotes import Dance_Floor
from highrise.__main__ import *
import random
import time
from highrise import BaseBot, Position, User, AnchorPosition, GetMessagesRequest
import asyncio, random
from highrise.__main__ import *
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from typing import Union
import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from typing import Any, Dict, Union
import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re

from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from highrise import BaseBot, Position
from highrise import __main__
from highrise.models import Item
from asyncio import run as arun
from highrise.models import AnchorPosition
import requests
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import BaseBot
from collections import UserDict
from highrise.models import SessionMetadata, User
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
import random
from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task
from typing import Union
import asyncio
import contextlib
import random
from typing import Any, Dict, Union
from importlib.machinery import ModuleSpec
from click.decorators import pass_context
from highrise import BaseBot
from typing import Any, Dict, Union
from highrise import *
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *

import asyncio
import contextlib
import random
from typing import Any, Dict, Union
from importlib.machinery import ModuleSpec
from click.decorators import pass_context
from highrise import BaseBot
from typing import Any, Dict, Union
from highrise import *
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *
from highrise.models import (
    AnchorPosition,
    Item,
    Position,
    SessionMetadata,
    User,
)
from highrise.models import (
    CurrencyItem,
    GetMessagesRequest,
    Item,
    SessionMetadata,
)
import random
import requests
import os
import importlib
import asyncio
import contextlib
import logging
from highrise import BaseBot, AnchorPosition, Position, User, TaskGroup
class Bot(BaseBot):
    def __init__(self):
        super().__init__()

        #conversation id var
        self.convo_id_registry = []

        #dance floor position
        min_x = 1.5
        max_x = 9.5
        min_y = 0.25
        max_y = 0.25
        min_z = 12.5
        max_z = 29.5

        self.dance_floor_pos = [(min_x, max_x, min_y, max_y, min_z, max_z)]

        #dancer variable
        self.dancer = []

        #dance floor emotes var
        self.emotesdf = Dance_Floor


    
  
    async def on_start(self, session_metadata):

        self.highrise.tg.create_task(self.highrise.walk_to(Position(x=8.0, y=0.25, z=13.5, facing='BackLeft')))
        
 
        asyncio.create_task(self.dance_floor())
        
            


    async def dance_floor(self):

        while True:

            try:
                if self.dance_floor_pos and self.dancer:
                    ran = random.randint(1, 73)
                    emote_text, emote_time = await self.get_emote_df(ran)
                    emote_time -= 1

                    tasks = [asyncio.create_task(self.highrise.send_emote(emote_text, user_id)) for user_id in self.dancer]

                    await asyncio.wait(tasks)

                    await asyncio.sleep(emote_time)

                await asyncio.sleep(1)

            except Exception as e:
                print(f"{e}")

    #function to get emote
    async def get_emote_df(self, target) -> None:

        try:
            emote_info = self.emotesdf.get(target)
            return emote_info
        except ValueError:
            pass

    async def on_user_move(self, user: User, destination: Position | AnchorPosition) -> None:

        #get user position on move and add them on self.dancer if on dancefloor
        if user:
            print(f"{user.username}: {destination}")

            if self.dance_floor_pos:

                if isinstance(destination, Position):

                    for dance_floor_info in self.dance_floor_pos:

                        if (
                            dance_floor_info[0] <= destination.x <= dance_floor_info[1] and
                            dance_floor_info[2] <= destination.y <= dance_floor_info[3] and
                            dance_floor_info[4] <= destination.z <= dance_floor_info[5]
                        ):

                            if user.id not in self.dancer:
                                self.dancer.append(user.id)

                            return

                # If not in any dance floor area
                if user.id in self.dancer:
                    self.dancer.remove(user.id)





    async def on_chat(self, user: User, message: str) -> None:
    
         print(f"{user.username} said: {message}")
      
         
             
         if message == "-daw":
          shirt = ["shirt-n_room12019cropsweaterblack"]
          pant = ["pants-n_room12019rippedpantsblue"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-n_basic2018pillowthinpeaked', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018pinkshadow2', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_whitedans', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='glasses-n_room12019halfrimblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='necklace-n_room32019locknecklace', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='bag-n_room32019sweaterwrapblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='handbag-n_room12019iphonepink', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),


          ]) 
          await self.highrise.chat(f"good {xox}")
         
