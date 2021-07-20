import requests
import json
from datetime import datetime


class API:
    # This is the class where all the base functions are defined to make the REST API calls.

    def __init__(self, server_location):
        self.base = server_location
        self.last_response_code = -1

    # Converts timestamp give to date time
    def timestamp_to_datetime(self):
        dt_object = datetime.fromtimestamp(self)
        return dt_object

    # Converts datetime to timestamp
    @staticmethod
    def datetime_to_timestamp():

        time_now = datetime.now()
        dt_object = datetime.timestamp(time_now)
        return dt_object

    # Removes an empty element from the list
    def remove_empty_element_from_list(self):
        while "" in self:
            self.remove("")
        return self

    # get json response by making a REST API call
    def call_rest_api(self, url_part, verb, data=None):
        # print url_part, verb

        url = self.base + url_part
        print(url, verb)
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json"
                   }
        resp = None

        if verb == "POST":
            resp = requests.post(url, json.dumps(data), headers=headers)
        elif verb == "DELETE":
            resp = requests.delete(url, headers=headers)
        elif verb == "PUT":
            resp = requests.put(url, data=json.dumps(data), headers=headers)
        elif verb == "GET":
            resp = requests.get(url, headers=headers)
        # print(resp.text)
        self.last_response_code = resp.status_code
        if resp.status_code != 200:
            print("BAD RESPONSE CODE: " + str(resp.status_code))
        return resp


class Node(object):
    # Simple object for storing Thing attributes. Nested Nodes can be used to represent a json tree as python object and hence dot notation can be used to navigate the structure. Can convert back to JSON.
    from json import JSONEncoder
    class NodeEncoder(JSONEncoder):
        def default(self, node_object):
            return node_object.__dict__

    def __repr__(self):
        type_name = type(self).__name__
        attr_strings = []

        for name, value in self._kwargs():
            attr_strings.append('{0!s}={1!r}'.format(name, value))

        return '{0!s}({1!s})'.format(type_name, ', '.join(attr_strings))

    def _kwargs(self):
        # Get a sorted collection of instance kwargs
        return sorted(self.__dict__.items())

    # def _args(self):
    #    return []

    def __init__(self, **kwargs):
        # Create a new instance based on the given kwargs.
        for name in kwargs:
            setattr(self, name, kwargs[name])

    def __getitem__(self, item):
        return self._lst[item]

    def __eq__(self, other):
        # Comparison on instance vars which is the __dict__ of each object
        return vars(self) == vars(other)

    def __contains__(self, key):
        # Tests for key in dict of instance vars
        return key in self.__dict__

    def __iter__(self):
        return iter([k for k in self._kwargs()])

    def to_JSON(self):
        return Node.NodeEncoder().encode(self)

    @staticmethod
    def to_NodeTree(json_tree):
        return json.loads(json_tree, object_hook=lambda d: Node(**d))
