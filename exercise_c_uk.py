united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
for nation in united_kingdom:
  if nation["name"] == "Wales":
    nation["capital"] = "Cardiff"

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom.append(
  {
    "name" : "Northern Ireland",
    "population": 1811000,
    "capital": "Belfast" 
  }
)

# 3. Use a loop to print the names of all the countries in the UK.
for nation in united_kingdom:
  print(nation["name"])

# 4. Use a loop to find the total population of the UK.
total_population = 0
for nation in united_kingdom:
  total_population += nation["population"]
print(f"The total population of the United Kingdom is {total_population}")
