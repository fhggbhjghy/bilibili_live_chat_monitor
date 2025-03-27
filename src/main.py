from app import live_chat_monitor, room_control
from gui import user_interface

if __name__ == '__main__':
    monitor = live_chat_monitor.Monitor()
    monitor.run()