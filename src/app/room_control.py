from bilibili_api import live, sync
from json import loads
from app.utility import get_credentials

class RoomControl():
    def __init__(self, room_display_id, credential):

        # Create bilibili_api.live.LiveRoom object to handle room specific actions
        self.live_room = live.LiveRoom(
            credential=credential,
            room_display_id=room_display_id
        )

        self.count = 1

        # for key, val in sync(self.live_room.get_user_info_in_room()).items():
        #     print(f'{key}: {val}\n')

        self.is_admin = False
        status = sync(self.live_room.get_user_info_in_room())
        if (status.get('badge', {'is_room_admin': False}).get('is_room_admin') 
            or status.get('uinfo', {'uid': -1}).get('uid') == sync(self.live_room.get_ruid())):
            self.is_admin = True

        # print(self.is_admin)

    # Called with id to create and push ban request
    def ban(self, user):
        if self.count:
            sync(self.live_room.ban_user(self.count))
            self.count+=1
        if not self.is_admin:
            print('not admin')
            return False
        if user[0] == -1:
            print(f'invalid uid {user[0]}')
            return False
        try:
            # sync(self.live_room.ban_user(user[0]))
            # print('user banned')
            print(f'banning {user}')
            return True
        except Exception as e:
            print(f'{e}')
            match e.message:
                case '不能禁言自己哦':
                    print('cannot ban self')
                    return False
                case '此用户已经被禁言了':
                    print('user already banned')
                    return True
                case _:
                    print(f'unrecognized code: {e.code}, {e.message}')
        return False