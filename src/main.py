from app.live_chat_monitor import Monitor
from app.room_control import RoomControl
from app.utility import change_room_display_id, is_logged_in, get_room_display_id, get_credentials
from gui import user_interface

def update(id, msg, ban):
    print(msg)
    # ban(1)

if __name__ == '__main__':
    option = input('0 to close\n1 to start\n2 to change room\n3 to change login cookie\n')
    room_display_id = get_room_display_id()
    credential = get_credentials()
    while option.isdigit():
        print(f'\nYou entered: {option}\n')
        match int(option):
            case 0:
                print('Exiting...')
                break
            case 1:
                # print('Starting monitor')
                monitor = Monitor(update, credential, room_display_id)
                gui = user_interface.Gui(monitor.room_control.ban)
                monitor.run()
                gui.run()
                # monitor = None
                # control = None
                # gui = None
            case 2:
                print('Changing room display id')
                room_display_id = change_room_display_id()
            case 3:
                print('Changing login cookie')
                is_logged_in(0)
            case _:
                print('Exiting...')
                break
        option = input('0 to close\n1 to start\n2 to change room\n')
    print('Exiting...')
