from toontown.toonbase.ToontownGlobals import *
# [Holiday, Weekday]
WEEKLY_HOLIDAYS = [
    [CIRCUIT_RACING, 0], # Monday
    [FISH_BINGO_NIGHT, 2],  # Wednesday
    [TROLLEY_HOLIDAY, 3],  # Thursday
    [SILLY_SATURDAY_BINGO, 5],  # Saturday
]

# [Holiday, begin[Month, Day, Hour, Minute], end[Month, Day, Hour, Minute]]
YEARLY_HOLIDAYS = [
    [TOP_TOONS_MARATHON, [1, 1, 12, 0], [1, 2, 0, 0]],
    [MORE_XP_HOLIDAY, [1, 20, 12, 0], [1, 28, 0, 0]],
    [VALENTINES_DAY, [2, 8, 12, 0], [2, 24, 0, 0]],
    [APRIL_FOOLS_COSTUMES, [3, 29, 12, 0], [4, 12, 0, 0]],
    [HALLOWEEN_PROPS, [10, 21, 12, 0], [11, 1, 0, 0]],
    [TRICK_OR_TREAT, [10, 21, 12, 0], [11, 1, 0, 0]],
    [HALLOWEEN, [10, 31, 12, 0], [11, 1, 0, 0]],
    [WINTER_DECORATIONS, [12, 14, 12, 0], [1, 4, 0, 0]],
]
