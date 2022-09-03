"""
There are two methods for removing specific elements from a set:

1. The 'remove()' method searches for an element within the set and removes it if it exists, otherwise a KeyError is thrown.

2. The 'discard()' method works the same way, but does not throw an exception if an element is not present.
"""


song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

tag_set = set(song_data_users['Retro Words'])
tag_set.discard('onion')
tag_set.discard('helloworld')
tag_set.discard('spam')
song_data_users['Retro Words'] = tag_set