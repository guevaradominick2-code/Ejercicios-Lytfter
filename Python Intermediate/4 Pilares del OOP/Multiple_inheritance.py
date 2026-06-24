class ArmorMix():
    def wear_armor(self):
        print("Jarvis! activate full armor")

    def close_mask(self):
        print("Jarvis! Close the Mask")
    
    def open_mask(self):
        print("Jarvis! Open the Mask")

class FlyMix():
    def fly(self):
        print("Jarvis! Let's Fly")

class WeaponsMix():
    def satellite_missiles(self):
        print("Jarvis! Deploy missiles")
    
    def hands_laser(self):
        print("Shooting lasers")

class Hero(ArmorMix, FlyMix, WeaponsMix):
    pass

iron_man = Hero()
iron_man.wear_armor()
iron_man.close_mask()
iron_man.open_mask()

iron_man.fly()
iron_man.satellite_missiles()
iron_man.hands_laser()