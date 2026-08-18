#solution...(just copy pasted)


def best_hands(hands):
    hands = serialize(hands)
    return [
        deserialize(hand)
        for hand in hands
        if card_ranks(hand) == card_ranks(max(hands, key=hand_rank))
    ]


def serialize(hands):
    """["10C AH"] -> [("0", "C"), ("A", "H"),]"""
    _hands = []
    for hand in hands:
        _hand = []
        for card in hand.split():
            _hand.append((card[-2], card[-1]))
        _hands.append(_hand)
    return _hands


def deserialize(hand):
    """[("0", "C"), ("A", "H"),] -> ["10C AH"]"""
    return " ".join(["".join(["10" if r == "0" else r, s]) for r, s in hand])


def hand_rank(hand):
    """takes serialized hands and resturns its ranking"""
    ranks = card_ranks(hand)
    groups = [(ranks.count(i), i) for i in set(ranks)]
    groups.sort(reverse=True)
    counts, number = zip(*groups)
    straight = (len(counts) == 5) and (max(number) - min(number) == 4)
    flush = len(set([s for r, s in hand])) == 1
    return (
        8 if straight and flush else
        7 if counts == (4, 1) else
        6 if counts == (3, 2) else
        5 if flush else
        4 if straight else
        3 if counts == (3, 1, 1) else
        2 if counts == (2, 2, 1) else
        1 if counts == (2, 1, 1, 1) else
        0, number
    )


def card_ranks(hand):
    ranks = ["--234567890JQKA".index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks
