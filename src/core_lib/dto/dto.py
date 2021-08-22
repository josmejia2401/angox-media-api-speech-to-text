import json
import datetime

class DTO(object):
    def __init__(self, dataAsJson={}, ignored_none=False):
        self.ignored_none = ignored_none
        self.id = None
        if dataAsJson is None:
            return
        if 'id' in dataAsJson and dataAsJson['id']:
            self.id = dataAsJson['id']

    def validate(self, validateItems=[]):
        for item in validateItems:
            if any(item == element for element in self.__dict__):
                if item not in self.__dict__ or self.__dict__[item] is None:
                    raise Exception(item + ' not found (1)')
            else:
                raise Exception(item + ' not found (2)')

    def default(self,  o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)

    def to_json(self):
        to_json_value = {}
        for k in self.__dict__:
            if k == 'ignored_none':
                continue
            if self.ignored_none == True and self.__dict__[k] is None:
                continue
            v = self.__dict__[k]
            if v and isinstance(v, (datetime.date, datetime.datetime)):
                v = v.isoformat()
            to_json_value[k] = v
        #return json.dumps(self.__dict__, sort_keys=True, indent=1, default=self.default)
        return to_json_value
        
    def get_json(self):
        return {
            'id': self.id,
            'updateAt': self.updateAt.isoformat(),
            'createAt': self.createAt.isoformat()
        }
