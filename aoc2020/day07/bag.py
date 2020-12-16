from copy import copy

class Bag:
    '''Describes a bag and its contents'''

    def __init__(self, color: str) -> None:
        self.found_contents = False
        self.color = color
        self.contents = set()
        self.rules = dict()

    def add_rule(self, color: str, count) -> None:
        '''Adds a rule about contained bags'''

        self.rules[color] = count

    def build_contents(self, bags: list) -> None:
        '''Constructs a set of all contained bags'''

        changed = True

        while changed:
            own_contents = copy(self.contents)

            changed = False
            if len(self.rules) != 0 and len(self.contents) == 0:
                # Start with a bag's own contents
                for rule in self.rules:
                    for bag in bags:
                        if bag.color == rule:
                            own_contents |= {bag}
                            break

                self.contents |= own_contents
                changed = True

            for bag in self.contents:
                if not bag.found_contents:
                    bag.build_contents(bags)
                own_contents |= bag.contents

                if self.contents != own_contents:
                    own_contents |= self.contents
                    changed = True

            self.contents = own_contents
            self.found_contents = True

    def count_bags(self) -> int:
        '''Count bags contained in this bag'''

        contained_bag_count = 0

        for bag in self.contents:
            if bag.color in self.rules:
                sub_count = bag.count_bags()
                multiplier = self.rules[bag.color]
                contained_bag_count += (sub_count + 1) * multiplier

        return contained_bag_count
