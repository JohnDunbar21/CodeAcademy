inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}


#Write your code below (Checkpoint 2):
class InventoryError(Exception):
  pass


def submit_order(instrument, quantity):
  supply = inventory[instrument]
  
  # Write your code below (Checkpoint 3 & 4): 
  if quantity > supply:
    raise InventoryError
  else:
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)