class ResourceMap:
    resource_index = {"seed": 0, "soil": 1, "fertilizer": 2, "water": 3,
                      "light": 4, "temperature": 5, "humidity": 6, "location": 7}

    def __init__(self, resources):
        if type(resources) is not list and type(resources) is not dict:
            raise TypeError("resources must be a list or dict")

        if len(resources) != len(self.resource_index):
            raise ValueError("resources does not match expected length. expected: " +
                             str(len(self.resource_index)) + " got: " + str(len(resources)))

        if type(resources) is list:
            self._resources = resources
        else:
            self._resources = [0] * len(self.resource_index)
            for key in resources:
                # check that key is in resource_index
                if key not in self.resource_index:
                    raise ValueError(
                        "key " + key + " not found in resource_index")
                self._resources[self.resource_index[key]] = resources[key]

    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, new_resources):
        self._resources = new_resources

    # get the index of a resource by name
    def get_resource_index(self, resource):
        # sanitize resource
        if type(resource) is not str:
            return "resource must be a string"
        if resource not in self.resource_index:
            return "resource name not found"

        return self.resource_index[resource]

    # get the value of a resource by index or name
    def get_resource_value(self, resource):
        # sanitize resource
        if type(resource) is not str and type(resource) is not int:
            return "resource must be a string or integer"
        if type(resource) is str and resource not in self.resource_index:
            return "resource name not found"
        if type(resource) is int and (resource < 0 or resource > 7):
            return "resource index out of bounds"

        if type(resource) is str:
            return self._resources[self.get_resource_index(resource)]
        else:
            return self._resources[resource]

    # set the value of a resource by index or name
    def set_resource_value(self, resource, value):
        # sanitize value
        if type(value) is not int:
            return "value must be an integer"

        # sanitize resource
        if type(resource) is not str and type(resource) is not int:
            return "resource must be a string or integer"
        if type(resource) is str and resource not in self.resource_index:
            return "resource name not found"
        if type(resource) is int and (resource < 0 or resource > 7):
            return "resource index out of bounds"

        if type(resource) is str:
            self._resources[self.get_resource_index(resource)] = value
        else:
            self._resources[resource] = value
