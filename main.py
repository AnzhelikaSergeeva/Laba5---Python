import turtle

# класс, отвечающий за вумерную L-систему
class LSystem2D:
    def __init__(self, t, axiom, width, length, angle):
        self.axiom = axiom      # инициатор, относительно которого формируем фрактал
        self.state = axiom      # строка с набором команд для фрактала (вначале это инициатор)
        self.width = width      # толщина линии рисования
        self.length = length    # длина одного линейного сегмента кривой
        self.angle = angle      # фиксированный угол поворота
        self.t = t              # сама черепашка
        self.rules = {}  # словарь для хранения правил формирования кривых
        self.t.pensize(self.width) # станавливаем ширину линии рисования

    # метод, добавляющий правила (в виде списка кортежей)
    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value

    # метод ля генерации фрактала (его кривой)
    def generate_path(self, n_iter):
        for n in range(n_iter):
            for key, value in self.rules.items(): # перебираем правила (ключ-значение)
                self.state = self.state.replace(key, value.lower()) # берем текущее правило (тек. маршрут) и заменяем ключи на значения

            self.state = self.state.upper() # после всех замен возвращаем все в верхний регист

    def draw_turtle(self, start_pos, start_angle):
         # ***************
        turtle.tracer(1, 0)     # форсажный режим для черепашки, чтобы быстрее ходила
        self.t.up()                 # черепашку поднимаем (чтобы не было следа, когда на начальную позицию перемещается)
        self.t.setpos(start_pos)    # начальная стартовая позиция
        self.t.seth(start_angle)    # начальный угол поворота
        self.t.down()               # черепашка опускается
        # ***************
        for move in self.state: # перебираем набор коман
            if move == 'F':
                self.t.forward(self.length)
            elif move == 'S':
                self.t.up()
                self.t.forward(self.length)
                self.t.down()
            elif move == '+':
                self.t.left(self.angle)
            elif move == '-':
                self.t.right(self.angle)

        turtle.done()        # чтобы окно не закрывалось после отрисовки


# ************** чтобы окно появлялось в левом верхнем углу с размерами 1200x600
width = 1200
height = 600
screen = turtle.Screen()
screen.setup(width, height, 0, 0) # устанавливаем в начальную (верхнюю левую) точку
# **************

t = turtle.Turtle()  # создаем экземпляр черепашки
t.ht()          # скрываем черепашку

pen_width = 2   # толщина линии рисования (в пикселах)
f_len = 5      # длина одного сегмента прямой (в пикселах)
angle = 60      # фиксированный угол поворота (в градусах)

axiom = "FXF--FF--FF"  # для ковра Серпинского (угол 60 градусов)

l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
l_sys.add_rules(("F", "FF"), ("X", "--FXF++FXF++FXF--"))	# кортеж ключ-значение
l_sys.generate_path(5) # переаем кол-во итераций
print(l_sys.state)
l_sys.draw_turtle((0, 0), -180)
