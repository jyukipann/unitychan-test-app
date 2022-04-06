from cgitb import text
from PIL import Image, ImageDraw
import sys
import time
import pyocr
pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import pyautogui as pg
import numpy as np

def alttab(n= 1):
    pg.keyDown('alt')
    for _ in range(n):
        pg.keyDown('tab')
        pg.keyUp('tab')
    pg.keyUp('alt')

if __name__ == "__main__":
    # tools = pyocr.get_available_tools()
    # tool = tools[0]
    # langs = tool.get_available_languages()
    # alttab()
    # # time.sleep(0)
    # sc = pg.screenshot()
    # alttab()
    # resize = (2,2)
    # target_image = sc.resize((sc.width // resize[0], sc.height // resize[1]))
    # txt_box = tool.image_to_string(
    #     target_image,
    #     lang="script/Japanese" if "script/Japanese" in langs else "eng",
    #     # builder=pyocr.builders.LineBoxBuilder(tesseract_layout=3), # WordBoxBuilder LineBoxBuilder
    #     builder=pyocr.builders.WordBoxBuilder(tesseract_layout=3), # WordBoxBuilder LineBoxBuilder
    # )
    # sc_draw = ImageDraw.Draw(sc)
    # array_box = np.array([t.position for t in txt_box])
    # array_box[:,:,0] *= resize[0]
    # array_box[:,:,1] *= resize[1]
    # for xyxy in array_box:
    #     sc_draw.rectangle(
    #         xyxy.ravel().tolist(), outline=(0, 255, 0), width=3
    #     )
    # sc.show()
    alttab(3)