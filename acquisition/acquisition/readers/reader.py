from abc import ABCMeta, abstractproperty, abstractmethod

class Reader(metaclass=ABCMeta):

    
    @abstractproperty
    def base_url(self):
        pass

    @abstractmethod
    def __call__(self):
        pass




    