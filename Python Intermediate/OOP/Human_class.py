class Finger():
    def __init__(self):
        pass

class Hand():
    def __init__(self, finger):
        self.finger = finger

class Arm():
    def __init__(self, hand):
        self.hand = hand

class Foot():
    def __init__(self):
        pass

class Leg():
    def __init__(self, foot):
        self.foot = foot

class Head():
    def __init__(self):
        pass

class Torso():
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Human():
    def __init__(self, torso):
        self.torso = torso


finger = Finger()
hand = Hand(finger)
right_arm = Arm(hand)
left_arm = Arm(hand)

foot = Foot()
right_leg = Leg(foot)
left_leg = Leg(foot)

head = Head()
torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

human_1 = Human(torso)
