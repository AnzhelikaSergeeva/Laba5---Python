import turtle
import time


# Draw triangle between the three points in the points list
def draw_triangle(points, t):
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])


def get_mid(p1, p2):
    return (p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2


def sierpinski(points, depth, t):
    draw_triangle(points, t)
    if depth > 0:
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                   depth - 1, t)
        sierpinski([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])],
                   depth - 1, t)
        sierpinski([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])],
                   depth - 1, t)


def main():
    t = turtle.Turtle()
    turtle.tracer(10, 0)
    t.ht()

    width = 1200
    height = 700
    screen = turtle.Screen()
    screen.setup(width, height, 0, -50)

    points_list = [[-300, -150], [0, 300], [300, -150]]
    depth = 5
    sierpinski(points_list, depth, t)

    # Building up a table
    for i in range(1, 6):
        turtle.TurtleScreen._RUNNING = True
        turtle_time = turtle.Turtle()
        turtle_time.ht()
        turtle.tracer(2, 0)

        start = time.time()
        sierpinski(points_list, i, turtle_time)
        finish = time.time() - start
        print("Current depth: {} - Time: {}".format(i, '%8.8f' % finish))

    screen.exitonclick()


main()