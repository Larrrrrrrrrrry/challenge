#python_challenger_color
import random, os
html_text = '<html><head></head><body><style> body {background-color:'
colors = ['magenta', 'cyan', 'yellow', 'black', 'white', 'grey', 'red', 'green', 'blue']
rgb = [(255, 0, 255), (0, 255, 255), (255, 255, 0), (0, 0, 0), (255, 255, 255), (128, 128, 128), (255, 0, 0), (0, 255, 0), (0, 0, 255)]

savePath = os.getcwd() + '/COLORS'
if not os.path.exists(savePath):
    os.makedirs(savePath)
os.chdir(savePath)

def _hex(color):
    a, b, c = color[0], color[1], color[2]
    a, b, c = buquan(hex(a)[2:]), buquan(hex(b)[2:]), buquan(hex(c)[2:])
    color = str(a) + str(b) + str(c)
    return color

def buquan(string):
    while len(string) < 2:
        string = '0' + string
    return string

#rgb(20,30,1);}</style></body></html>
color = (0, 0, 0)
html_text_new = html_text + 'rgb' + str(color) + ';}</style></body></html>'


for i in range(random.randint(100, random.randint(400, 600))):
    disgust = random.randint(0, 40)
    if disgust == 0:
        f = open('PeiYingLarry' + _hex(color) + '.html', 'w')
        color = colors[random.randint(0, 8)]
        html_text_new = '<html><head></head><body>The next color is ' + color + '.</body></html>'
        f.write(html_text_new)
        f.close()
        color = rgb[colors.index(color)]
        continue
    f = open('PeiYingLarry' + _hex(color) + '.html', 'w')
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    html_text_new = html_text + 'rgb' + str(color) + ';}</style></body></html>'
    f.write(html_text_new)
    f.close()

f = open('PeiYingLarry' + _hex(color) + '.html', 'w')
html_text_new = '<html><head></head><body>This is the end! PY is great! Larry is also minimally great! </body></html>'
f.write(html_text_new)
f.close()
  
