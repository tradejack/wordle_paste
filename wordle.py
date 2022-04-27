from PIL import Image
from PIL import ImageGrab
from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager
import time

black_square = "\U00002B1B"
green_square = "\U0001F7E9"
yellow_square = "\U0001F7E8"

black = (58, 58, 60, 255)
green = (83, 141, 78, 255)
yellow = (181, 159, 59, 255)
colors = [black, green, yellow]

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.get('https://www.powerlanguage.co.uk/wordle/')
# driver.execute_script("""
# const a = JSON.parse(window.localStorage.gameState);
# a.lastPlayedTs = Date.now();
# window.localStorage.gameState = JSON.stringify(a);
# """)
# driver.refresh()
# time.sleep(3.0)
# driver.save_screenshot("screenshot.png")

try:
    img = ImageGrab.grabclipboard()
    print("image loaded from clipboard")
    width, height = img.size

except:
    print("clipboard image not found, loading wordle.png")
    img = Image.open("wide_wordle.png")
    img = img.convert('RGBA')
    width, height = img.size

first_square = 0
pix = img.load()

for x in range(width):
    for y in range(height):
        color = pix[x,y]
        if color in colors:
            #print(x, y, color)
            if first_square == 0:
                x_0 = x
                y_0 = y
                first_square = 1
            elif first_square == 2:
                y_m = y
                first_square = 3
                break
        else:
            if first_square == 1:
                y_n = y
                first_square = 2
    if first_square == 3:
        break

square_len = y_n - y_0
margin_len = y_m - y_n
print(square_len, margin_len)
row = ""
count = 1
for y in range(y_0+2, height, square_len + margin_len):
    for x in range(x_0+2, width, square_len + margin_len):
        color = pix[x,y]
        #print(x,y)
        if color not in colors:
            #print("color:",color)
            break
        if color == black:
            row += black_square
        elif color == green:
            row += green_square
        elif color == yellow:
            row += yellow_square
        if not count % 5:
            print(row)
            row = ""
        count += 1
