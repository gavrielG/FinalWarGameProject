from DeckOfCards import DeckOfCards
from CardGame import CardGame

new = CardGame("Natan", 26, "Gavriel", 26)

print("Bank", DeckOfCards(), "\n")
print(f"{new.player.playername}'s hand", new.player.player_deck)
print(len(new.player.player_deck), "cards\n")
print(f"{new.player2.playername}'s hand", new.player2.player_deck)
print(len(new.player2.player_deck), "cards\n")

print("Starting Game!")
for i in range(10):
    print(f"round {i+1}")
    a = new.player.get_card()
    b = new.player2.get_card()
    print(f"{new.player.playername} threw {a}")
    print(f"{new.player2.playername} threw {b}")
    if a > b:
        new.player.add_card(b)
        print(f"{new.player.playername} won this round\n")
    else:
        new.player2.add_card(a)
        print(f"{new.player2.playername} won this round\n")
new.get_winner()
print(f"{new.player.playername} has {len(new.player.player_deck)} cards")
print(f"{new.player2.playername} has {len(new.player2.player_deck)} cards")
print(new.player.player_deck)
print(new.player2.player_deck)
