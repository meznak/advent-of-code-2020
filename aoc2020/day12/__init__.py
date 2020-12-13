'''
Advent of Code Day 12
Rainy Risk
'''

SAMPLE_SOLUTIONS = [25, 286]

class Ship(object):
    '''A ferry'''

    def __init__(self, position = (0,0)):
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.direction = 90

    def turn(self, action: chr, value: int) -> None:
        '''Turn the ship'''

        if action == 'R':
            self.direction += value
        else:
            self.direction -= value

        self.direction %= 360

    def move(self, action: chr, value: int) -> None:
        '''Move the ship'''

        if action == 'N':
            self.y_pos += value
        elif action == 'E':
            self.x_pos += value
        elif action == 'S':
            self.y_pos -= value
        elif action == 'W':
            self.x_pos -= value
        elif action in ['L', 'R']:
            self.turn(action, value)
        elif action == 'F':
            if self.direction == 0:
                self.move('N', value)
            elif self.direction == 90:
                self.move('E', value)
            elif self.direction == 180:
                self.move('S', value)
            elif self.direction == 270:
                self.move('W', value)

    def rotate(self, action: chr, value: int) -> None:
        '''Rotate waypoint around a ship'''

        while value > 0:
            if action == 'R':
                # Swap, negate y
                temp = self.y_pos
                self.y_pos = self.x_pos * -1
                self.x_pos = temp
            else:
                # Negate y, swap
                temp = self.y_pos * -1
                self.y_pos = self.x_pos
                self.x_pos = temp

            value -= 90



    def move_to_waypoint(self, value: int, waypoint: object) -> None:
        '''Move ship to the waypoint'''

        for _ in range(value):
            self.x_pos += waypoint.x_pos
            self.y_pos += waypoint.y_pos


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        if item != '':
            action = item[0]
            value = int(item[1:])
            output.append((action, value))

    return output

def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    ship = Ship()

    for action, value in dataset:
        ship.move(action, value)

    return abs(ship.x_pos) + abs(ship.y_pos)

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    ship = Ship()
    waypoint = Ship((10, 1))

    for action, value in dataset:
        if action in ['N', 'E', 'S', 'W']:
            waypoint.move(action, value)
        elif action in ['R', 'L']:
            waypoint.rotate(action, value)
        elif action == 'F':
            ship.move_to_waypoint(value, waypoint)

    return abs(ship.x_pos) + abs(ship.y_pos)