card_values = {
    "A": 11, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10
}

deck = {
    f'{rank} of {suit}' : value
    for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
    for rank, value in card_values.items()
}
