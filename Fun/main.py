
"""This is the flavor text for this funny.main program. Masato (I) made it a fun program
because I'm having a really bad day. This is in hopes that I can heal myself and become
a better person. I just want to make people laugh and be happy. Kinda' sad isn't it.
Almost sounds like the start of a bad movie."""


class Player:
    """This is the player, the main character the PC man. Played Character.
    He's got health, what his primary weapon's name is, his three inventory slots and
    what location he's in."""
    def ___init___(self, health, primaryWeapon, inv1, inv2, inv3, location):
        self.health = health
        self.primaryWeapon = primaryWeapon
        self.inv1 = inv1
        self.inv2 = inv2
        self.inv3 = inv3
        self.location = location




class Room:
    def ___init___(self, listOfUnits):
        self.listOfUnits = listOfUnits

class Knife:
    """"This is a knife. 1d6 damage"""
    def ___init___(self, location, quality, price, damage):
        self.location = location
        self.quality = quality
        self.price = price
        self.damage = damage



vvKnife = Knife("vv", "Average", 30, "1d6")

#vv = Player(100, vvKnife)'''