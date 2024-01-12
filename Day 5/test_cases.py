from resource_map import ResourceMap

# create with invalid resources type
# resource_map = ResourceMap("invalid")

# create with invalid list length
# resources = [0, 10, 20, 30, 40, 50, 60]
# resource_map = ResourceMap(resources)

# create with invalid dict length
# resources = {"seed": 0, "soil": 10, "fertilizer": 20, "water": 30,
#              "light": 40, "temperature": 50, "humidity": 60}
# resource_map = ResourceMap(resources)

# create with invalid dict key
# resources = {"seed": 0, "soil": 10, "fertilizer": 20, "water": 30,
#              "light": 40, "temperature": 50, "humidity": 60, "lotion": 70}
# resource_map = ResourceMap(resources)

# create with a dict
resources = {"seed": 0, "soil": 10, "fertilizer": 20, "water": 30,
             "light": 40, "temperature": 50, "humidity": 60, "location": 70}
resource_map = ResourceMap(resources)
print(resource_map.resources)

# create with a list
resources = [0, 10, 20, 30, 40, 50, 60, 70]
resource_map = ResourceMap(resources)
print(resource_map.resources)

# get with invalid type
print(resource_map.get_resource_index(1))
# get with invalid key
print(resource_map.get_resource_index("dont exist"))
# get with valid key
print(resource_map.get_resource_index("seed"))
# set with invalid value type
print(resource_map.set_resource_value("seed", "100"))
# set with invalid key type
print(resource_map.set_resource_value(True, 100))
# set with invalid key
print(resource_map.set_resource_value("dont exist", 100))
# set with invalid index
print(resource_map.set_resource_value(8, 100))
# set with valid index
resource_map.set_resource_value(1, 100)
print(resource_map.resources)
# set with valid key
resource_map.set_resource_value("seed", 100)
print(resource_map.resources)

# set with invalid method
# this should not be allowed and throw an AttributeError
resource_map.resources[0] = 0
print(resource_map.resources)
