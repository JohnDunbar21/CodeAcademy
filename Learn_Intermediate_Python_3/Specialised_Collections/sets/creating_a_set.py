"""
A set object can be created by passing an iterable object into its constructor, using curly braces, or using a set comprehension.

The 'set()' method takes an array '[]' as an argument. It will automatically remove duplicates from the array.

Set comprehension uses '{}' and can be seen in the code below:
"""


genre_results = ['rap',
'classical',
'rock',
'rock',
'country',
'rap',
'rock',
'latin',
'country',
'k-pop',
'pop',
'rap',
'rock',
'k-pop',
'rap',
'k-pop',
'rock', 
'rap',
'latin',
'pop', 
'pop', 
'classical', 
'pop', 
'country', 
'rock', 
'classical', 
'country', 
'pop', 
'rap', 
'latin']

survey_genres = {genre for genre in genre_results}
survey_abbreviated = {genre[0:3] for genre in genre_results}
print(survey_abbreviated)