music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

frozen_tag_union = my_tags.union(music_tags) # returns a frozenset
regular_tag_intersect = music_tags.intersection(my_tags) # returns a normal set
frozen_tag_difference = my_tags.difference(music_tags) # returns a frozenset
regular_tag_sd = music_tags.symmetric_difference(my_tags) # returns a normal set