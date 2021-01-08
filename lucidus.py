
"""
The following code is Card Game with shuffle deck, get top card, sort cards and get winner
"""

"""
# Import
"""
import pydealer
import pydealer.card as card

"""
    Defining the own rank according to question
"""
new_ranks = {
    "values": {
        "Ace": 13,
        "King": 12,
        "Queen": 11,
        "Jack": 10,
        "10": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1
    },
    "suits": {
        "Spades": 1,
        "Diamonds": 2,
        "Hearts": 3,
        "Clubs": 4
    }
}

class card_deck():
    """
    Card class with creating deck of 52 cards
    """
    
    def __init__(self):
        """
        Constructor (init function) to initial and declare deck of 52 cards
        according to new ranks
        """
        self.deck = pydealer.Deck(ranks = new_ranks)
        
    def deck_shuffle(self):
        """
        Shuffle the deck randomly. Using inbuilt function shuffle from pydealer lib.
        
        :Returns:
            deck - shuffle cards in random order
        """
        self.deck.shuffle()
        return self.deck
    
    def get_top_card(self):
        """
        Get the top card from the deck
        
        :Returns:
            list - List with card value and suits
        """
        try:
            return self.deck.get(0)
        except IndexError as e:
            print(e)
    
    def sort_cards(self,cards):
        """
        Sorts a given list of cards according to rank
        :Arg cards:
            The cards deck to sort.
        :Returns:
            list - The sorted cards.
        """
        if(len(cards) == 0):
            return "Empty deck; nothing to sort"
        
        ranks = new_ranks
        
        if ranks.get("values"):
            cards = sorted(
                cards,
                key=lambda x: ranks["values"][x.value]
            )
        if ranks.get("suits"):
            cards = sorted(
                cards,
                key=lambda x: ranks["suits"][x.suit]
            )
        return cards
    
class player():
    """
    Player class creating player and storing their hands details
    """
    def __init__(self, name):
        """
        Constructor (init function) to initial and declare player name, the 
        cards player hold from the deck and the points
        :Arg name:
            string - player name
        """
        if(len(name) == 0):
            self.name = "Jon Doe"
        else:
            self.name = name
        self.hand = []
        self.point = 0 
        
    def draw_card(self, deck):
        """
        Getting the cards that player will hold and storing it in hand variable
        :Args deck : 
            deck of cards
        :Returns:
            None.
        """
        if(not deck):
            return "Not deck"
        self.hand = deck.deal(3)
        
    def player_points(self):
        """
        Calculates the points according to the suit and value of card from the
        new rank
        :Returns:
            None.
        """
        for i in self.hand:
            self.point += new_ranks['values'][i.value] * new_ranks['suits'][i.suit]
    
    def winner(self, other_player):
        """
        Get the winner of the game by comparing the points of the two player
        :Arg other_player:
            Object - object of other player from whom comparsion is done
        :Returns:
            string - Name of the winning player
        """
        if(self.point > other_player.point):
            return self.name
        return other_player.name
    
    def get_points(self):
        """
        Getter function for getting the points of a particular player
        :Returns:
            int - points of player
        """
        return self.point
    
#Creating object of card_deck class
obj = card_deck()

#Shuffling the deck randomly
shuffle_deck = obj.deck_shuffle()
print("Shuffle deck:\n",shuffle_deck,"\n")

#get the card from the deck
top_card = obj.get_top_card()
print("Top card from deck:\n",top_card,"\n")

# creating list of cards
c = [
     card.Card(value='2', suit='Spades'), 
     card.Card(value='5', suit='Diamonds'), 
     card.Card(value='King', suit='Spades'), 
     card.Card(value='3', suit='Hearts'), 
     card.Card(value='Ace', suit='Clubs'), 
    ]
#Printing the sort order of the card
print("Sort Card Deck:\n",obj.sort_cards(c),"\n")

#Creating two players
p1 = player('Player1')
p2 = player('Player2')

# Drawing 3 cards form the deck
p1.draw_card(obj.deck)
p2.draw_card(obj.deck)

#Calculating points on the card to particular player
p1.player_points()
p2.player_points()

#Printing the player name whose has won depending upon the points
print("Winner is ",p1.winner(p2))

