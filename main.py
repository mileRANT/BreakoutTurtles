import turtle as tr
from paddle import Paddle
from ball import Ball
import time

screen = tr.Screen()
screen.setup(width=1200, height=600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle()
ball = Ball()

playing_game = True

screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)


def check_collision_with_walls():
    global ball

    # detect collision with left and right walls:
    if ball.xcor() < -580 or ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return

    # detect collision with upper wall
    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)
        return

    # detect collision with bottom wall
    # In this case, user failed to hit the ball
    # thus he loses. The game resets.
    if ball.ycor() < -280:
        ball.reset()
        return
def check_collision_with_paddle():
    pass
def check_collision_with_bricks():
    pass


while playing_game:
    screen.update()
    time.sleep(0.01)
    ball.move()

    check_collision_with_walls()

tr.mainloop()