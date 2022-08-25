flight_statuses = {
  903: 'Departed',
  834: 'Boarding',
  359: 'Delayed',
  128: 'On time',
  385: 'On time',
}

print('***Small World Air Flight Information***')
for flight, status in flight_statuses.items():
  print('Flight ' + str(flight) + ' status: ' + status)