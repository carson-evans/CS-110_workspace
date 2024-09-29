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
    cardString = "Ace"
elif card == 11:
    cardString = "Jack"
elif card == 12:
    cardString = "Queen"
elif card == 13:
    cardString = "King"
else:
    cardString = str(card) # For cards 2 through 10, just convert to string

# Concat
stdio.write(cardString)
stdio.write(" of ")
stdio.write(suitString)