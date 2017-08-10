# Types:
INVASION_TYPE_NORMAL = 0
INVASION_TYPE_MEGA = 1

# Flags:
IFSkelecog = 1 << 0
IFWaiter = 1 << 1
IFV2 = 1 << 2

# combo of Suit index and Type index, +1
comboToType = {
    '10': 'Bossbot Department Invasion',
    '11': 'Flunky',
    '12': 'Pencil Pusher',
    '13': 'Yesman',
    '14': 'Micromanager',
    '15': 'Downsizer',
    '16': 'Head Hunter',
    '17': 'Corporate Raider',
    '18': 'The Big Cheese',
    '20': 'Lawbot Department Invasion',
    '21': 'Bottom Feeder',
    '22': 'Bloodsucker',
    '23': 'Double Talker',
    '24': 'Ambulance Chaser',
    '25': 'Back Stabber',
    '26': 'Spin Doctor',
    '27': 'Legal Eagle',
    '28': 'Big Wig',
    '30': 'Cashbot Department Invasion',
    '31': 'Short Change',
    '32': 'Penny Pincher',
    '33': 'Tightwad',
    '34': 'Bean Counter',
    '35': 'Number Cruncher',
    '36': 'Money Bags',
    '37': 'Loan Shark',
    '38': 'Robber Baron',
    '40': 'Sellbot Department Invasion',
    '41': 'Cold Caller',
    '42': 'Telemarketer',
    '43': 'Name Dropper',
    '44': 'Glad Hander',
    '45': 'Mover and Shaker',
    '46': 'Two Face',
    '47': 'The Mingler',
    '48': 'Mr. Hollywood',
    '50': 'Boardbot Department Invasion',
    '51': 'Con Artist',
    '52': 'Connoisseur',
    '53': 'The Swindler',
    '54': 'Middleman',
    '55': 'Toxic Manager',
    '56': 'Magnate',
    '57': 'Big Fish',
    '58': 'Head Honcho'
}
