sku_list = [7046538, 8289407, 9056375, 2308597]

# Write your code below:
print(dir(sku_list))

sku_iterator_object_one = sku_list.__iter__()
print(sku_iterator_object_one)

sku_iterator_object_two = iter(sku_list)
print(sku_iterator_object_two)