


class Gateway(object):
    """
    Base class for all gateways.
    """
    def __init__(self, *args, **kwargs):
        self._options = kwargs

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__
    
    