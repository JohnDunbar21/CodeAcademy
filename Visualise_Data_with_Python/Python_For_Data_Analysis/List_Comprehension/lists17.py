capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
locations = [capital+', '+country for (capital, country) in zip(capitals, countries)]