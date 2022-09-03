"""
Similar to how we can find elements in common between sets, we can also find unique elements in one set. 
To do so, the 'set' or 'frozenset' use the 'difference()' method or the '-' operator. 
This returns a 'set' or 'frozenset', which contains only the elements from the first set which are not found in the second set. 

Similar to the other operations, the type of the first operand (a 'set' or 'frozenset' on the left side of the operator or method) 
determines if a 'set' or 'frozenset' is returned when finding the difference.

This operation also supports an updating version of the method.
You can use 'difference_update()' to update the original 'set' with the result instead of returning a new 'set' or 'frozenset' object.
"""


song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

tag_diff = set(user_liked_song['Back To Art']) - set(user_disliked_song['Retro Words'])

recommended_songs = {}
for name, tags in song_data.items():
    for tag in tags:
        if tag in tag_diff:
            if name not in user_liked_song and name not in user_disliked_song:
                recommended_songs[name] = tags

print(recommended_songs)