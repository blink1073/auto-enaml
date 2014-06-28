
class MInfo(object):

    __slots__ = ('model', 'name')

    def __init__(self, model, name):
        self.model = model
        self.name = str(name)

    @property
    def member(self):
        return self.model.members()[self.name]

    @property
    def validator(self):
        return self.member.validate_mode[1]

    @property
    def value(self):
        return getattr(self.model, self.name)


class Partial(object):

    __slots__ = ('name', 'kwargs')

    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs
