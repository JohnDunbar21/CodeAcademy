"""
There are two ways to add elements to a set:

1. The 'add()' method can add a single element to the set.

2. The 'update()' method can add multiple elements.

Neither of the above methods will add a duplicate item to a set.

A 'frozenset' can not have any items added to it, so neither of these methods will work.

Elements in a 'set' or 'frozenset' will not be ordered as all sets are unordered.
"""

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

tag_set = set(song_data['Retro Words'])
user_tags = [user_tag_1, user_tag_2, user_tag_3] # to use update() method, you must have all items in a list. 
tag_set.update(user_tags)

song_data['Retro Words'] = tag_set