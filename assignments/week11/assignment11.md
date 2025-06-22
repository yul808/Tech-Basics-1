# Assignment 11 Read Some Code
## Blackjack-Barebones

---

### Where it was Found and Why it was Chosen
Since we were mostly concerned with coding small games in this course, the idea for this assignment was to find myself a comparable game that either used py.game or was mainly text-based. 
As the search with the suggested prompt "python" did not lead to any fitting results on github, the prompt "python game" led to a multitude of appropriate .py files. 
The decision was made in connection with the length of the code. The code `blackjack-barebones.py` by Al Sweigart fullfilled all my requirements and ended up as my first choice for this assignment.

The aim of this code study is to hopefully get an impression of how other (more advanced) programmers would approach similar coding tasks. 
It is thought to help learn common methods in coding and apply these to my own codes in the future. 

---

### Structure & General Function
As the name of the code already suggests, the program lets the user play a simple game of Blackjack. 
The goal of this game of cards is to get as close as possible to the card value of 21, without exceeding it. 
You play against the dealer. 
Whoever is closer to 21 wins.

When executing the code for the first time, the player as well as the dealer are dealt 2 cards each.
The sum of their values is presented to you, your opponents cards are only partly revealed to you, which means that you only know one card and its value for their overall score.
With simple input you as a player can then decide to if you want to draw another card or stay with your current cards. 
Once you decide to stay with your cards, the dealer will get a chance to draw another card, then the result is revealed with a respective message as well as little ASCII Arts for the cards.

Structure-wise, the code is considerably straight forward. In the first relevant line, they import the `random` library, followed by the definition of some constants, which in this case are not more than the cards symbols using Python's `chr` function. 

After that, they define the `main()` function of the game, which will call for a few other functions when executed.
These are defined afterwards and include `displayHands(playerHand, dealerHand)`, `getHandValue(allCards)`, and `displayCards(allCards)`.

In the following, I will not explain the `main()` function as it appears too long to discuss in detail. 
The `displayCards(allCards)` function for instance, also covers many different techniques and is especially interesting, since it is not directly called by the `main()` function, but rather by the `displayHands(playerHand, dealerHand)` function.

---

### `displayCards(allCards)` Function in Detail
Generally speaking, the function enables the program to display the dealt cards as it creates the respective ASCII Arts necessary. 


The function: 
```
def displayCards(allCards):
    rows = ['', '', '', '', '']  

    for card in allCards:
        rank = card[0]
        suit = card[1]
        rows[0] += ' ___  '  
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)
```
In the first line of the actual function, they define a list called `rows`.
The strings inside only contain spaces, so they don't have any relevant content for now.
This is used to prepare every individual row of the ASCII for later manipulation. 

This manipulation takes place in the next step. 
They use a `for` loop here to assign a specific value to the variables `rank` and `suit`. 
Within the same loop, they use these variables to  go through every item from the list (which represent each row of the ASCII) and manipulate them in the respective order by using the index and `+=` to add more lines for the edges as well as their value and suit.
They use `.format(rank.ljust(2))` as well as `.format(rank.rjust(2, '_'))`for these rows.

Admittedly, this was quite hard to figure out. 
Apparently, these functions ensure, that the `rank` takes exactly 2 character spaces, which helps with consistent alignment of the characters when printing the cards. 

In the final step, they go through the rows again by using another `for` loop to finally `print` each row once the function is called. 
As already mentioned, this happens within another function that is then called by the `main()` function. 
This specific function therefore makes it possible globally to print these small card ASCII Arts. 

---

### Takeaways
As mentioned, the idea behind choosing this specific function for the analysis was to have a look at how more advanced programmers would approach tasks familiar to myself. 
The ASCII Art especially seemed more straight forward in the beginning, than this example code has shown to be. 
The approach with `.format(rank.ljust(2))` and `.format(rank.rjust(2, '_'))` is a small detail, that I personally wouldn't have thought about using (as I didn't know it existed). 

Also, it was quite interesting to see how this programmer included their functions into their other functions. There seemed to be an internal logic that was easy to follow when reading the code.
When looking at my coding assignments, my code seems way less organized in comparison. 
This is probably something I could familiarize myself more with. 

---

### Difficulties
As already mentioned the `.format(rank.ljust(2))` as well as `.format(rank.rjust(2, '_'))` were quite difficult to understand in the beginning. 
However, once looked up on the internet they made more sense to me as they serve an important purpose in printing these playing cards. 