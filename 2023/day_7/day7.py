#!/bin/bash/python3
import sys
from collections import Counter
from functools import cmp_to_key

CARD_STRENGTH = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }

def compare_cards_2(card_one, card_two):
    CARD_STRENGTH['J'] = 1
    if card_one == card_two:
        return 0
    
    elif CARD_STRENGTH[card_one] > CARD_STRENGTH[card_two]:
        return -1
    
    else:
        return 1

def compare_cards(card_one, card_two):
    if card_one == card_two:
        return 0
    
    elif CARD_STRENGTH[card_one] > CARD_STRENGTH[card_two]:
        return -1
    
    else:
        return 1

def get_hand_strength(hand, part2 = False):
    strength = 0

    count = Counter(hand)

    if part2:
        j_count = count['J']
        count.pop('J', None)

        if not count:
            count['J'] = 0

        count[max(count, key=count.get)] += j_count

    appears = count.values()
    
    if any(c == 5 for c in appears):
        strength = 7
    
    elif any(c == 4 for c in appears):
        strength = 6
    
    elif any(c == 3 for c in appears) and any(c == 2 for c in appears):
        strength = 5

    elif any(c == 3 for c in appears): # Not the full house case
        strength = 4
    
    elif any(c == 2 for c in appears) and len(count.keys()) == 3: # Two pairs
        strength = 3
    
    elif any(c == 2 for c in appears):
        strength = 2
    
    else:
        strength = 1

    return strength

def compare_hands_2(hand_one, hand_two):
    result = 0

    hand_one = hand_one[0]
    hand_two = hand_two[0]

    strength_one = get_hand_strength(hand_one, True)
    strength_two = get_hand_strength(hand_two, True)
    
    if strength_one > strength_two:
        result = -1

    elif strength_one < strength_two:
        result = 1

    else:
        card_comparison = 0
        for i in range(len(hand_one)):
            card_comparison = compare_cards_2(hand_one[i], hand_two[i])
            if card_comparison != 0:
                result = card_comparison
                break

    return result

def compare_hands(hand_one, hand_two):
    result = 0

    hand_one = hand_one[0]
    hand_two = hand_two[0]

    strength_one = get_hand_strength(hand_one)
    strength_two = get_hand_strength(hand_two)

    if strength_one > strength_two:
        result = -1

    elif strength_one < strength_two:
        result = 1

    else:
        card_comparison = 0
        for i in range(len(hand_one)):
            card_comparison = compare_cards(hand_one[i], hand_two[i])
            if card_comparison != 0:
                result = card_comparison
                break

    return result

def day7(filename, part2=False):

    hands = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            parsed = line.split(" ")
            hands.append((parsed[0], int(parsed[1])))

    if not part2:
        arranged = sorted(hands, key=cmp_to_key(compare_hands))
    
    else:
        arranged = sorted(hands, key=cmp_to_key(compare_hands_2))

    total = 0
    for i in range(len(arranged)):
        total += arranged[i][1] * (len(arranged) - i)
    
    return total

if __name__=="__main__":
    value = day7(sys.argv[1])
    print(f"The answer for part 1 is {value}.")

    value = day7(sys.argv[1], True)
    print(f"The answer for part 2 is {value}.")