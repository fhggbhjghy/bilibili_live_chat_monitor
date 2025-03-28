from app import live_chat_monitor, room_control
from app.utility import change_room_display_id, is_logged_in
from gui import user_interface

def update(id, msg, ban):
    print(msg)
    # ban(1)

if __name__ == '__main__':
    option = input('0 to close\n1 to start\n2 to change room\n3 to change login cookie\n')
    while option.isdigit():
        print(f'\nYou entered: {option}\n')
        match int(option):
            case 0:
                print('Exiting...')
                break
            case 1:
                # print('Starting monitor')
                # monitor = live_chat_monitor.Monitor(update)
                # monitor.run()
                gui = user_interface.Gui()
                gui.run()
            case 2:
                print('Changing room display id')
                change_room_display_id()
            case 3:
                print('Changing login cookie')
                is_logged_in(0)
            case _:
                print('Exiting...')
                break
        option = input('0 to close\n1 to start\n2 to change room\n')
    print('Exiting...')
