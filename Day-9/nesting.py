capitals = {
    "France": "Paris",
    "Germany": "Birlin",
}

# nested list

travel = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "berlin"],
}

print(travel["France"][1])

nested_list = ["A", "B", ["c", "D"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
       "cities_visited": ["Stuttgart", "Berlin", "Hamburg"],
       "total_visits": 5,
       }
}

print(travel_log["Germany"]["cities_visited"][0])