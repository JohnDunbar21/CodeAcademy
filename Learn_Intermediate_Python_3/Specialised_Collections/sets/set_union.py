"""
When working with a 'set' or 'frozenset' container, one of the most common operations we can perform is a merge.
To do this, we can return the union of two sets using the 'union()' method or '|' operator.
Doing so will return a new 'set' or 'frozenset' containing all elements from both sets without duplicates.

The resulting set contains all the elements in both set A and set B as well as elements they have in common (minus the duplicates).

The return value takes the form of the left operand.
"""


song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

new_song_data = {}
for key,value in song_data.items():
  song_tag_set = set(value)
  user_tag_set = set(user_tag_data[key])
  new_song_data[key] = song_tag_set.union(user_tag_set) # could use '|' instead of 'union()' method. 
print(new_song_data)