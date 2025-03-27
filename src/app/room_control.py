from bilibili_api import live, sync

class RoomControl():
    def __init__(self, room_display_id, credential):

        # Create bilibili_api.live.LiveRoom object to handle room specific actions
        self.live_room = live.LiveRoom(
            credential=credential,
            room_display_id=room_display_id
        )

    # Called with id to create and push ban request
    def ban(self, id):
        try:
            sync(self.live_room.ban_user(id))
        except Exception as e:
            print(f'ban failed at live_room: {e}')