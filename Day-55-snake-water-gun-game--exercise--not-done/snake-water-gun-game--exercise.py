# Snake, Water and Gun is a variation of the children's gam

# Rules:
# * Snake 🐍 drinks Water 💧 → Snake wins
# * Water 💧 douses Gun 🔫 → Water wins
# * Gun 🔫 shoots Snake 🐍 → Gun wins
# * Same choice = draw


### Rules:

# * **Snake 🐍 drinks Water 💧** → **Snake wins**
# * **Water 💧 douses Gun 🔫** → **Water wins**
# * **Gun 🔫 shoots Snake 🐍** → **Gun wins**
# * Same choice = **draw**

# ### How to play:

# Both players secretly choose **Snake**, **Water**, or **Gun**, then reveal at the same time.


# S = -1
# W = 0
# G = 1

# D = Draw
# W = Win
# L = Lose

#                   S W G
# computer =       -1 0 1
# player   = S -1   D W L
#          = W 0    L D W
#          = G 1    W L D





# **Snake–Water–Gun as a math matrix** 🧮

#Let the strategies be ordered as:

#S = Snake, W = Water, G = Gun


### Payoff matrix (Player A vs Player B)

# Rows = Player A
# Columns = Player B
# Payoff: **+1 = win, 0 = draw, −1 = loss**


#   |  S  W  G
# -------------
# S |  0 +1 -1
# W | -1  0 +1
# G | +1 -1  0

# ### Interpretation

# * (S) beats (W) → (+1)
# * (W) beats (G) → (+1)
# * (G) beats (S) → (+1)
# * Same choices → (0)