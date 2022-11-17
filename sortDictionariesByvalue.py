#Sort the dictionary based on values
dt = {5:2,1:6,6:3}
sorted_dt = {key: value for key, value in sorted(dt.items(), key = lambda item: item[1])}
print(sorted_dt)
"""Here, key=lambda item: item[1] returns the values of each key:value pair.
From each key:value pair of dt.item(), sorted() sorts the items based on values."""

#Sort only the values
dt = {5:4, 1:6, 6:3}

sorted_dt_value = sorted(dt.values())
print(sorted_dt_value)