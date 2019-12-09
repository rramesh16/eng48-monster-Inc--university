# Monster Class file

class Monster():
    def __init__(self, name):
        self.names = name
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def set_name(self, name):
        the_new_monster_name = self
        the_new_monster_name.names.append(name)


# example_monster = Monster('Jim')
# example_monster.add_skill('Creativity')
# print(example_monster.skills)






#

