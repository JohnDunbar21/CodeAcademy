class CustomerCounter:

  def __iter__(self):
    self.count = 0
    return self

  def __next__(self):
    if self.count >= 100:
      raise StopIteration
    self.count += 1
    return self.count

customer_counter = CustomerCounter()

for customer in customer_counter:
  print(customer)