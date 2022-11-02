import math

#postavke igre
RES = WIDTH, HEIGHT = 1600, 900;
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0;

PLAYER_POS = 1.5, 5 # na maloj mapi
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

FOV = math.pi / 3 #sirina pogleda (vrijedi za kasnije)
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2     #broj rayeva(linija) koje pice iz karaktera(trenutno kugle) ._. lol
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS