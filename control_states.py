#The following list contains all the possible button combinations
#that can be input into Rocket League.

#The following is the order in which these controls can be interpereted:
#[Forward/Backward Controls, Left/Right Controls, Jump, Boost, Shift]

FOWARDBACKWARD_INDEX = 0
LEFTRIGHT_INDEX = 1
JUMP_INDEX = 2
BOOST_INDEX = 3
SHIFT_INDEX = 4



control_states = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1],

    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1],

    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1],

    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],

    [0, -1, 0, 0, 0],
    [0, -1, 0, 0, 1],
    [0, -1, 0, 1, 0],
    [0, -1, 0, 1, 1],
    [0, -1, 1, 0, 0],
    [0, -1, 1, 0, 1],
    [0, -1, 1, 1, 0],
    [0, -1, 1, 1, 1],

    [-1, 0, 0, 0, 0],
    [-1, 0, 0, 0, 1],
    [-1, 0, 0, 1, 0],
    [-1, 0, 0, 1, 1],
    [-1, 0, 1, 0, 0],
    [-1, 0, 1, 0, 1],
    [-1, 0, 1, 1, 0],
    [-1, 0, 1, 1, 1],

    [-1, -1, 0, 0, 0],
    [-1, -1, 0, 0, 1],
    [-1, -1, 0, 1, 0],
    [-1, -1, 0, 1, 1],
    [-1, -1, 1, 0, 0],
    [-1, -1, 1, 0, 1],
    [-1, -1, 1, 1, 0],
    [-1, -1, 1, 1, 1],

    [1, -1, 0, 0, 0],
    [1, -1, 0, 0, 1],
    [1, -1, 0, 1, 0],
    [1, -1, 0, 1, 1],
    [1, -1, 1, 0, 0],
    [1, -1, 1, 0, 1],
    [1, -1, 1, 1, 0],
    [1, -1, 1, 1, 1],

    [-1, 1, 0, 0, 0],
    [-1, 1, 0, 0, 1],
    [-1, 1, 0, 1, 0],
    [-1, 1, 0, 1, 1],
    [-1, 1, 1, 0, 0],
    [-1, 1, 1, 0, 1],
    [-1, 1, 1, 1, 0],
    [-1, 1, 1, 1, 1]]

CONTROL_STATES_COUNT = len(control_states)