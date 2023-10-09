from pico2d import *
import random


# Game object class here
class Grass:  # class의 이름은 명사로, 첫 글자는 대문자로.
    def __init__(self):  # 생성자 함수, 객체가 생성이 될때 항상 맨처음 불러와 짐. 객체의 초기상태 설정.
        self.image = load_image('grass.png')  # self는 생성된 객체를 가르키는 변수, self 안에 속성이 담김.

    def draw(self):  # 잔디를 그려주는 행위를 함.
        self.image.draw(400, 30)  # self로 가르켜야함.

    def update(self): pass  # 통일을 위한 dummy 함수이다.


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5  # 오른쪽으로 이동

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y > 70:
            self.y -= random.randint(1, 10)
        else:
            self.y = 70

    def draw(self):
        self.image.draw(self.x, self.y)


class Ball2:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 75:
            self.y -= random.randint(1, 10)
        else:
            self.y = 75

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()


def reset_world():
    global running
    global grass
    global team
    global falling_ball
    global falling_ball2
    global world

    running = True
    world = []  # 새로운 객체를 추가할 때 update_world와 render_world의 코드를 수정하지 않아도 됨.
    # 새로운 객체를 생성하면 world list에 만 넣어주면 됨.

    grass = Grass()  # 파라미터가 들어갈 수 있기 때문에 ()를 해주어야함.
    world.append(grass)

    team = [Boy() for i in range(10)]  # List comperhension 이용
    world += team

    falling_ball = [Ball() for n in range(10)]
    world += falling_ball

    falling_ball2 = [Ball2() for k in range(10)]
    world += falling_ball2


def update_world():
    grass.update()
    for o in team:
        o.update()
    for n in falling_ball:
        n.update()
    for i in falling_ball2:
        i.update()


def render_world():
    clear_canvas()
    grass.draw()  # clear와 update 사이에 glass를 그려줌.
    # 여러개의 오브젝트를 그릴 때는 그리는 순서가 중요함.
    for o in team:
        o.draw()
    for n in falling_ball:
        n.draw()
    for i in falling_ball2:
        i.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()  # game logic
    update_world()  # game logic
    render_world()  # draw world
    delay(0.05)

# finalization code

close_canvas()
