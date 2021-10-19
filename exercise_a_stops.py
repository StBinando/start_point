stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh")

#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0,"Glasgow Queen St")

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(stops.index("Falkirk High")+1, "Polmont")

#4. Print out the index position of "Linlithgow"
print(f"The index position of Linlithgow is {stops.index('Linlithgow')}")

#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")

#6. Delete "Cumbernauld" from the list by index
del stops[stops.index("Cumbernauld")]

#7. Print the number of stops there are in the list
print(f"There are {len(stops)} stops in the list")

#8. Sort the list alphabetically
stops.sort()

#9. Reverse the positions of the stops in the list
stops.reverse()

#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)