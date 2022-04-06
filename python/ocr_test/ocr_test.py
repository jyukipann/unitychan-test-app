from PIL import Image, ImageDraw
import sys
import time
import pyocr
pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.

time_s = time.time()
target_image = Image.open(r'unitychan-test-app\python\スクリーンショット 2022-04-06 134947.png')
target_image = target_image.resize((target_image.width // 2, target_image.height // 2))

txt_box = tool.image_to_string(
    target_image,
    lang="script/Japanese" if "script/Japanese" in langs else "eng",
    builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6)
)

target_draw = ImageDraw.Draw(target_image)

print(type(txt_box))
print(len(txt_box))
for t in txt_box:
    # print(t.position,t.content)
    target_draw.rectangle(
        t.position, outline=(0, 255, 0), width=3
    )
print(f"ocr time : {time.time() - time_s}")

target_image.show()