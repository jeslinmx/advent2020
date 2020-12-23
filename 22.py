# Problem: https://adventofcode.com/2020/day/22

# Input
from sys import stdin
b_start = []
for line in stdin:
    if "Player 1" in line or not line.strip():
        continue
    elif "Player 2" in line:
        a_start, b_start = b_start, []
    else:
        b_start.append(int(line))

# Part 1
from collections import deque
a_deck, b_deck = deque(a_start), deque(b_start)
while a_deck and b_deck:
    a, b = a_deck.popleft(), b_deck.popleft()
    if a > b:
        a_deck.append(a)
        a_deck.append(b)
    else:
        b_deck.append(b)
        b_deck.append(a)
winner = a_deck or b_deck
winner.reverse()
print(sum((i * card for i, card in enumerate(winner, start=1))))

# Part 2
from itertools import islice
def combat(a_start, b_start):
    a_deck, b_deck = deque(a_start), deque(b_start)
    a_wins = False
    states = set()
    while a_deck and b_deck:
        # infinite recursion prevention
        state = (tuple(a_deck), tuple(b_deck))
        if state in states:
            a_wins = True
            break
        else:
            states.add(state)
        # determine round winner
        a, b = a_deck.popleft(), b_deck.popleft()
        if a <= len(a_deck) and b <= len(b_deck):
            a_wins_round, _ = combat(islice(a_deck, a), islice(b_deck, b))
        else:
            a_wins_round = a > b
        # add cards to deck of winner
        a_deck.extend([a, b]) if a_wins_round else b_deck.extend([b, a])

    a_wins = a_wins or (len(b_deck) == 0)
    score = sum((
        i * card
        for i, card in enumerate(
            reversed(a_deck if a_wins else b_deck),
            start=1
            )
        ))
    return a_wins, score

_, score = combat(a_start, b_start)
print(score)