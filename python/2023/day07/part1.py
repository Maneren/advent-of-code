from dataclasses import dataclass


# Calculate the rank of given card.
# The order is A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2,
# where A = 12, 2 = 0
def rank_card(card: str) -> int:
    assert len(card) == 1

    if card.isdigit():
        return int(card) - 2

    if card == "T":
        return 8
    if card == "J":
        return 9
    if card == "Q":
        return 10
    if card == "K":
        return 11
    if card == "A":
        return 12

    raise ValueError(f"Invalid card: {card}")


def value_of_hand(counts_of_cards: list[int]) -> int:
    counts_of_kinds = [0] * 6

    for count_of_cards in counts_of_cards:
        counts_of_kinds[count_of_cards] += 1

    print(counts_of_kinds)

    if counts_of_kinds[5]:
        return 8
    if counts_of_kinds[4]:
        return 7
    if counts_of_kinds[3]:
        return 6 if counts_of_kinds[2] else 5
    if counts_of_kinds[2] == 2:
        return 4
    if counts_of_kinds[2]:
        return 3
    if all(counts_of_kinds):
        return 2

    return 0


@dataclass
class Hand:
    cards: str
    ranks: list[int]
    bid: int
    value: int

    def __init__(self, cards: str, bid: str):
        self.cards = cards
        self.ranks = [rank_card(card) for card in cards]
        self.bid = int(bid)

        counts = [0] * 13

        for card in self.ranks:
            counts[card] += 1

        self.value = value_of_hand(counts)

    def __str__(self) -> str:
        return f"{self.cards} {self.bid}"

    def __gt__(self, other: "Hand"):
        if self.value == other.value:
            return self.ranks > other.ranks
        return self.value > other.value


def solve(print, print_output):
    lines = open(0).read().splitlines()

    hands = [Hand(*line.split(" ")) for line in lines]

    print(hands)

    hands.sort()

    print(hands)

    total_winning = sum((rank + 1) * hand.bid for rank, hand in enumerate(hands))

    print_output(total_winning)
