customer_rewards = {
  'Zoltan': 82570,
  'Guadalupe': 29850,
  'Mario': 17849
}

def display_rewards_account(customer):
  # Write your code below:
  try:
    rewards_number = customer_rewards[customer]
    print('Rewards account number is: ' + str(rewards_number))
  except KeyError:
    print('Customer was not found in rewards program!')
  else:
    print('Rewards account number is: '+str(rewards_number))


customer = 'Mario'
display_rewards_account(customer)
customer = 'Luigi'
display_rewards_account(customer)