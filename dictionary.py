"""

A simple .py file that stores the dictionary for colors.
It will be accessed when drawing the game in the game.py file.
"""





# 2048 game color dictionary (key: tile value, value: rgb color). Tried to make as similar as possible to ios colors
colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),

          #for early values, the lighter shade looks better with lighter texts
          'light text': (249, 246, 242),

          #similarly, for larger values, shade looks better with darker texts
          'dark text': (119, 110, 101),

          #in case we get to above 2048: will just color black
          'other': (0, 0, 0),

          #board color: ios board was brownish in color
          'bg': (187, 173, 160)}