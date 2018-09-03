import abc


class Switcher(object, metaclass=abc.ABCMeta):
    """An abstract base class for creating a switcher (i.e. switch statements in python)
    """
    @abc.abstractmethod
    def handle_action(self, action):
        raise NotImplementedError('user(s) must define handle_action to use this base class')
