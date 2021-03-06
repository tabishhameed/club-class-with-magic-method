class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __len__(self):
        return len(self.players)

    def __getitem__(self, i):
        return self.players[i]

    def __repr__(self):
        return f"Club {self.name}: {self.players}"

    def __str__(self):
        return f"Club {self.name} with {len(self)} players"

club_arsenal = Club('Jr')
print(repr(club_arsenal))
print(club_arsenal)
print(len(club_arsenal))

club_arsenal.players.append('tab')
club_arsenal.players.append('sam')
club_arsenal.players.append('tb')
club_arsenal.players.append('tom')
print((club_arsenal.players [0:3]))