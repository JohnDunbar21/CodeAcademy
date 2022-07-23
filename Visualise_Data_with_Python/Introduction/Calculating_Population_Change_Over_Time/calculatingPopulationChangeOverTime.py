city_name = 'Istanbul, Turkey'
pop_1927 = 691000
pop_2017 = 15029231
pop_change = pop_2017 - pop_1927
percentage_growth = (pop_change/pop_1927)*100
annual_growth = percentage_growth/90 # 90 years have passed since the data started being gathered and concluded

def population_growth(year_one, year_two, population_one, population_two):
    growth_rate = (((population_two - population_one)/population_one)*100)/(year_two-year_one)
    return growth_rate

print(annual_growth)
set_one = population_growth(1927, 2017, 691000, 15029231)
print(set_one)
print(f"The population in {city_name} between the years 1927 and 2017 has an annual growth rate of {set_one}")