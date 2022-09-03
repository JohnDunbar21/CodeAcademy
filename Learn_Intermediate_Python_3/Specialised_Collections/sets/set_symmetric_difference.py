"""
We can think of symmetric difference as the opposite of the intersection operation.
A resulting set will include all elements from the sets which are in one or the other, but not both. 
In other words, elements that are unique to each set.

To perform this operation on the 'set' or 'frozenset' containers, we can use the 'symmetric_difference()' method or the '^' operator. 
Like the other operators, the type of the first operand (a 'set' or 'frozenset' on the left side of the operator or method) determines 
if a 'set' or 'frozenset' is returned when finding the symmetric difference.

We can also update the original set using this operation by using the 'symmetric_difference_update()' method to update the original 
set with the result instead of returning a new 'set' or 'frozenset' object.
"""


user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_tags = set()
for name,tags in user_song_history.items():
  user_tags.update(set(tags))
    
friend_tags = set()
for name,tags in friend_song_history.items():
  friend_tags.update(set(tags))

unique_tags = user_tags.symmetric_difference(friend_tags) # checks what tags are unique to each set, not just one. 
print(unique_tags)