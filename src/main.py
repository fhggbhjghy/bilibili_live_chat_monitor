from app.live_chat_monitor import Monitor
from app.room_control import RoomControl
from app.utility import change_room_display_id, get_room_display_id, get_credentials
from gui import user_interface

def update(id, content):
    print(f'mock update: {id}, {content}')

if __name__ == '__main__':
    prompt = '0 to close\n1 to start\n2 to change room\n3 to change login cookie\n4 to run monitor without gui\n5 to run gui only\n'
    option = input(prompt)
    room_display_id = get_room_display_id()
    credential = get_credentials()
    while option.isdigit():
        print(f'\nYou entered: {option}\n')
        match int(option):
            case 0:
                print('Exiting...')
                break
            case 1:
                print('Starting monitor')
                monitor = Monitor(room_display_id, credential)
                gui = user_interface.Gui(monitor.room_control.ban)
                monitor.update = gui.update
                monitor.run()
                # if monitor.run():
                #     gui.run()
            case 2:
                print('Changing room display id')
                room_display_id = change_room_display_id()
            case 3:
                print('Changing login cookie')
                credential = get_credentials(0)
            case 4:
                print('Launch Headless Monitor')
                monitor = Monitor(room_display_id, credential)
                monitor.update = update
                monitor.run(0)
            case 5:
                print('Launch Gui Only')
                room_control = RoomControl(room_display_id, credential)
                gui = user_interface.Gui(room_control.ban)
            case _:
                print('Exiting...')
                break
        option = input(prompt)
    print('Exiting...')
