"""
Let's say that we have two or more sets, and we want to find which items both sets have in common.
The 'set' container has a method called 'intersection()' which returns a new 'set' or 'frozenset' consisting of those elements.
An intersection can also be performed on multiple sets using the '&' operator.

Similar to the other operations, the type of the first operand (a 'set' or 'frozenset' on the left side of the operator or method) 
determines if a 'set' or 'frozenset' is returned when finding the intersection.

In addition to a regular intersection, the 'set' container can also use a method called 'intersection_update()'.
Instead of returning a new 'set', the original 'set' is updated to contain the result of the intersection.
"""


song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

user_set = set(user_recent_songs['Retro Words'])
user_set_2 = set(user_recent_songs['Lowkey Space'])
tags_int = user_set.intersection(user_set_2)

recommended_songs = {}

for name,tags in song_data.items():
  for tag in tags:
    if tag in tags_int:
      if name not in user_recent_songs:
        recommended_songs[name] = tags

print(recommended_songs)