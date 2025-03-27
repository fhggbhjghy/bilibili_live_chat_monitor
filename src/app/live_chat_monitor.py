from bilibili_api import live, sync
from app.utility import get_credentials, get_room_display_id
import threading
import logging

# Start logger
logger = logging.getLogger(__name__)

class Monitor():
    def __init__(self):
        self.credential = get_credentials()
        self.room_display_id = get_room_display_id()
        self.room = live.LiveDanmaku(
            room_display_id=self.room_display_id,
            credential=self.credential
        )
        self.thread = None

    def run(self):
        try:
            self.thread = threading.Thread(
                target = sync(self.room.connect()),
                daemon = True
            )
        except Exception as e:
            logger.info(e)
            return False
        return True