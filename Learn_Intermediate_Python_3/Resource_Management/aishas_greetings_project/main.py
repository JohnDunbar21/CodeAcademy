"""
Due to the nature of this repository spanning multiple fields, the relative path links are interfering with string methods such as '\n' or '\a', and as such,
the files in this folder should be run in a separate directory from the main repository in order for it to execute properly.
"""


from contextlib import contextmanager

@contextmanager
def generic(card_type, sender, receiver):
    card = open(f"{card_type}.txt", "r+")
    
    try:
      card.write(f"""
      Dear {receiver},
      {card.read()}
      Sincerely, {sender}.
      """)
      yield card

    finally:
      card.close()

# test code
#with generic("thankyou_card", "Mwenda", "Amanda") as card:
  #print("Card Generated!")
  #print(card.read())

class personalised:
  def __init__(self, sender_name, receiver_name):
    self.sender_name = sender_name
    self.receiver_name = receiver_name
    self.file = open(f"{sender_name}_personalized.txt", "w")

  def __enter__(self):
    self.file.write(f"Dear {self.receiver_name},")
    return self.file

  def __exit__(self, exc_type, exc_value, traceback):
    self.file.write(f"Sincerely {self.sender_name}.")
    self.file.close()

with personalised("John", "Michael") as card:
  card.write("""
I am so proud of you!
Being your friend for all these years has been nothing but a blessing.
I don't say it often but I just wanted to let you know that you inspire me and I love you!
All the best. Always.
  """)

with generic("happy_bday", "Josiah", "Remy") as b_day_card:
  with personalised("Josiah", "Ester") as personalised_card:
    b_day_card.write("""
Happy Birthday!!
I love you to the moon and back.
Even though you're a pain sometimes, you're a pain I can't live without.
I am incredibly proud of you and grateful to have you as a sister.
Cheers to 25!! You're getting old!
    """)