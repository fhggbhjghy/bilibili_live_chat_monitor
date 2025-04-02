import ctypes
import os
from json import load
from pathlib import Path
from customtkinter import CTkFrame

OUTPUT_PATH = Path(__file__).parent

def justify_frame(frame: CTkFrame, index, direction, weight = 1) -> None:
    match direction:
        case 'both':
            frame.grid_rowconfigure(index, weight=weight)
            frame.grid_columnconfigure(index, weight=weight)
        case 'width':
            frame.grid_columnconfigure(index, weight=weight)
        case 'height':
            frame.grid_rowconfigure(index, weight=weight)

def load_settings() -> dict:
    path = OUTPUT_PATH / 'option.json'

    if not os.path.exists(path):
        print('file not found')
        return None

    with open(path, 'r') as file:
        settings = load(file)
        if settings['custom']:
            print('not empty')
            return settings['custom']
        # print('empty')
        return settings['default']

def get_window_scaling():
    try:
        return ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
    except AttributeError as e:
        return 1.0
    except Exception as e:
        print(e)

def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1+radius, y1,
        x1+radius, y1,
        x2-radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1+radius,
        x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

if __name__ == '__main__':
    print(load_settings())