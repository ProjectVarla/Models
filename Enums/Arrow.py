from ..DataStructures import Pair


class Arrow(Pair):
    """"""
    # 0,0 at the top X is inverted
    up: Pair = Pair(-1, 0)
    down: Pair = Pair(1, 0)

    right: Pair = Pair(0, 1)
    left: Pair = Pair(0, -1)
