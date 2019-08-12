import pickle
from enum import Enum
class AccessType(Enum):
    private = 0
    public = 1
    free = 2

DEBUG = False

class DataFileDescriptor():
    def __init__(self, file_path):
        self.file_path = file_path
        self.allowed_users = set()
        self.allowed_groups = set()
        self.access_type = AccessType.private

    def add_user(self, user):
        if user is not None :
            self.allowed_users.add(user)

    def add_group(self, group):
        if group is not None :
            self.allowed_groups.add(group)

    def set_access_type(self, access_type):
        self.access_type = access_type

    def __str__(self):
        return "%pth->"+self.file_path+"%grps->"+str(self.allowed_groups)+"%usrs->"+str(self.allowed_users)+"%acct->"+str(self.access_type)+"\n"

    __repr__ = __str__

class DataFileStorage():
    def __init__(self):
        self.storage = {}

    def add(self, key, value):
        self.storage[key] = value

    def get(self, key):
        return self.storage.get(key, "")

    def save(self, filename):
        if DEBUG:
            for key,value in self.storage.items() :
                print("{key}:{value}\n".format(key=str(key), value=str(value)))
        with open(filename, 'wb') as f:
            pickle.dump(self.storage, f, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        with open(filename, 'rb') as f:
            self.storage = pickle.load(f)

    def __str__(self):
        return str(self.storage)

    __repr__ = __str__



