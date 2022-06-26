from turtle import *
import time

bgcolor("black")
r, g, b = 255, 0, 0
hideturtle()
pensize(3)
time.sleep(5)
for i in range(255 * 2):
    colormode(255)

    if i < 255 // 3:
        g += 3
    elif i < 255 * 2 // 3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < 255 * 4 // 3:
        g -= 3
    elif i < 255 * 5 // 3:
        r += 3
    else:
        b -= 3

        fe(50 + 2.05 + i)
        rt(90.5)
        pencolor(r, g, b)
    mainloop()
