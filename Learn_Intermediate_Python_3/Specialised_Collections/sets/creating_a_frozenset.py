"""
Unlike a normal 'set()', you can only create a 'frozenset()' using its constructor.

Remember that using a frozenset means that you cannot modify the elements inside of it.
"""

top_genres = ['rap', 'rock', 'pop']

frozen_top_genres = frozenset(top_genres)

print(frozen_top_genres)