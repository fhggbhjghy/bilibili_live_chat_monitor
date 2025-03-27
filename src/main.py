from app import live_chat_monitor, room_control
from app.utility import change_room_display_id
from gui import user_interface

def update(id, msg, ban):
    print(msg)
    # ban(1)

if __name__ == '__main__':
    option = input('0 to close\n1 to start\n2 to change room\n')
    while option.isdigit():
        print(f'\nYou entered: {option}\n')
        match int(option):
            case 0:
                print('Exiting...')
                break
            case 1:
                print('Starting monitor')
                monitor = live_chat_monitor.Monitor(update)
                monitor.run()
            case 2:
                print('Changing room display id')
                change_room_display_id()
            case _:
                print('Exiting...')
                break
        option = input('0 to close\n1 to start\n2 to change room\n')
    print('Exiting...')
