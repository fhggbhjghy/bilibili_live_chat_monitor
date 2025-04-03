from bilibili_api import live, sync
from app.utility import get_credentials, get_room_display_id
from app.room_control import RoomControl
import threading
import logging

# Start logger
logger = logging.getLogger(__name__)

class Monitor():
    def __init__(self, update, credential, room_display_id):

        # Passed callback function to handle danmu event updates
        self.update = update

        # Grab credential and prepare chat hook
        self.live_danmaku = live.LiveDanmaku(
            room_display_id=room_display_id,
            credential=credential
        )

        # Create instance of room_control with bilibili_api.LiveRoom object
        self.room_control = RoomControl(room_display_id, credential)

        # Used to run process in sub-thread
        self.thread = None

        # Used to id messages
        self.id = 0

        # Message event handler
        @self.live_danmaku.on('DANMU_MSG')
        async def on_danmaku(event):

            # Check if event body is valid message structure
            data = event.get('data', None)
            if not data:
                return
            info = data.get('info', None)
            if not info:
                return
            if len(info) <= 2:
                return
            
            # Parse message body for content, identifier, and chat rank
            parsed_message_info = {}
            parsed_message_info['message'] = info[1]
            parsed_message_info['sender_uid'] = info[2][0]
            parsed_message_info['sender_name'] = info[2][1]

            # Check if user is equiping chat rank of current room, default to 0 if not
            parsed_message_info['fan_id'] = -1
            parsed_message_info['sender_rank'] = 0
            if len(info) > 3 and len(info[3]) > 3:
                parsed_message_info['fan_id'] = info[3][3]
                if info[3][3] == self.live_danmaku.room_display_id:
                    parsed_message_info['sender_rank'] = info[3][0]

            # Create structured text to be displayed on gui
            parsed_message_info['structured_message'] = f'{parsed_message_info["sender_name"]} (lv.{parsed_message_info['sender_rank']}): {parsed_message_info["message"]}'

            # Try calling callback method to update Gui, passing ban function for external access
            try:
                self.update(self.id, parsed_message_info, self.room_control.ban)
                self.id = (self.id+1)%36
            except Exception as e:
                print(e)

            # Debugging
            print(f'{parsed_message_info["sender_name"]} lv.{parsed_message_info['sender_rank']} ({parsed_message_info["sender_uid"]}): {parsed_message_info["message"]}')


    def launch_monitor(self):
        sync(self.live_danmaku.connect())

    def stop(self):
        sync(self.live_danmaku.disconnect())

    def run(self):

        # Spawn thread that connects to Bilibili danmu websocket
        try:
            self.thread = threading.Thread(
                target = self.launch_monitor,
                daemon = True
            )
            self.thread.start()
        except Exception as e:
            logger.info(e)
            return False
        return True