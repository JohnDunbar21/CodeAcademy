"""
In Python, 'set' and 'frozenset' items cannot be accessed by a specific index.
This is due to the fact that both containers are unordered and have no indices.

However, like most other Python containers, we can use the 'in' keyword to test if an element is in a 'set' or 'frozenset'.
"""


allowed_tags = ['pop',
'hip-hop',
'rap', 
'dance', 
'electronic', 
'latin', 
'indie', 
'alternative rock', 
'classical', 
'k-pop', 
'country', 
'rock', 
'metal', 
'jazz', 
'exciting', 
'sad', 
'happy', 
'upbeat', 
'party', 
'synth', 
'rhythmic', 
'emotional', 
'relationship', 
'warm', 
'guitar', 
'fiddle', 
'romance', 
'chill', 
'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

tag_set = set(song_data_users['Retro Words'])
bad_tags = []
for tag in tag_set:
  if tag in allowed_tags:
    continue
  else:
    bad_tags.append(tag)

for tag in bad_tags:
  if tag in tag_set:
    tag_set.discard(tag)

song_data_users['Retro Words'] = tag_set
print(song_data_users)