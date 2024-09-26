import stdio
import stdrandom

...

# Deck of 52 cards
# 13 cards in each suit
# 4 Suits
# 1, 2, ..., 10, Jack, Queen, King, Ace

# Get Random Suit
suit = stdrandom.uniformInt(1, 4)

if suit == 1:
    suitString = "Clubs"

if suit == 2:
    suitString = "Spades"

if suit == 3:
    suitString = "Hearts"

if suit == 4:
    suitString = "Diamonds"

# Get random card
card = stdrandom.uniformInt(1, 13)

if card == 1:
    cardString = "1"

if card == 2:
    cardString = "2"

if card == 3:
    cardString = "3"

if card == 4:
    cardString = "4"

if card == 5:
    cardString = "5"

if card == 6:
    cardString = "6"

if card == 7:
    cardString = "7"

if card == 8:
    cardString = "8"

if card == 9:
    cardString = "9"

if card == 10:
    cardString = "10"

if card == 11:
    cardString = "Jack"

if card == 12:
    cardString = "Queen"

if card == 13:
    cardString = "King"

if card == 14:
    cardString = "Ace"

# Concat
stdio.write(cardString)
stdio.write(" of ")
stdio.write(suitString)