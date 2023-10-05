from pico2d import *


# Game object class here
class Grass: # class의 이름은 명사로, 첫 글자는 대문자로.
    def __init__(self): # 생성자 함수, 객체가 생성이 될때 항상 맨처음 불러와 짐. 객체의 초기상태 설정.
        self.image = load_image('grass.png') # self는 생성된 객체를 가르키는 변수, self 안에 속성이 담김.

    def draw(self): # 잔디를 그려주는 행위를 함.
        self.image.draw(400, 30) # self로 가르켜야함.

    def update(self): pass

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

    running = True
    grass = Grass() # 파라미터가 들어갈 수 있기 때문에 ()를 해주어야함.


def update_world():
    grass.update()
    pass


def render_world():
    clear_canvas()
    grass.draw() # clear와 update 사이에 glass를 그려줌.
    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events() # game logic
    update_world() # game logic
    render_world() # draw world
    delay(0.05)

# finalization code

close_canvas()
