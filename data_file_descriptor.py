import pickle
from enum import Enum
class AccessType(Enum):
    private = 0
    public = 1
    free = 2


class DataFileDescriptor():
    def __init__(self, file_path):
        self.file_path = file_path
        self.allowed_users = set()
        self.allowed_groups = set()
        self.access_type = AccessType.private

    def add_user(self, user):
        self.allowed_users.add(user)

    def add_group(self, group):
        self.allowed_groups.add(group)

    def set_access_type(self, access_type):
        self.access_type = access_type

class DataFileStorage():
    def __init__(self):
        self.storage = {}

    def add(self, key, value):
        self.storage[key] = value

    def get(self, key):
        return self.storage.get(key, "")

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.storage, f, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        with open(filename, 'rb') as f:
            self.storage = pickle.load(f)



