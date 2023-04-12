import turtle as tr
from paddle import Paddle

screen = tr.Screen()
screen.setup(width=1200, height=600)
screen.bgcolor('black')
screen.title('Breakout')

paddle = Paddle()

screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)

screen.update()

tr.mainloop()