authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")

def last_names(author_names):
    author_last_names = []
    for name in author_names:
        temp = name.split(" ")
        author_last_names.append(temp[1])
    return author_last_names

author_last_names = last_names(author_names)