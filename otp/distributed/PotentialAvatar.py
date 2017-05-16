
class PotentialAvatar:

    def __init__(self, id, names, dna, position, allowedName, creator = 1, shared = 1, online = 0, wishState = 'CLOSED', wishName = '', defaultShard = 0, lastLogout = 0, hp = 15, maxHp = 15, hat = [0, 0, 0], glasses = [0, 0, 0], backpack = [0, 0, 0], shoes = [0, 0, 0]):
        self.id = id
        self.name = names[0]
        self.dna = dna
        self.avatarType = None
        self.position = position
        self.wantName = names[1]
        self.approvedName = names[2]
        self.rejectedName = names[3]
        self.allowedName = allowedName
        self.wishState = wishState
        self.wishName = wishName
        self.creator = creator
        self.shared = shared
        self.online = online
        self.defaultShard = defaultShard
        self.lastLogout = lastLogout
        self.hp = hp
        self.maxHp = maxHp
        self.hat = hat
        self.glasses = glasses
        self.backpack = backpack
        self.shoes = shoes