from abc import ABC ,abstractmethod

class Voice(ABC):
    @abstractmethod
    def use_Assistance(self):
        pass
    @abstractmethod
    def use_server(self):
        pass
    @abstractmethod
    def use_os(self):
        pass

class Siri(Voice):
    def use_Assistance(self):
        print('it is Siri of Apple')
    def use_server(self):
        print('it uses Apple servers')
    def use_os(self):
        print('uses ios ')

class Alexa(Voice):
    def use_Assistance(self):
        print('it is Alexa of Amazon')
    def use_server(self):
        print('it uses Amazon servers')
    def use_os(self):
        print('it uses Amazon os')

class Google(Voice):
    def use_Assistance(self):
        print('its google assistance of google')
    def use_server(self):
        print('it uses Google servers')
    def use_os(self):
        print('it uses android os')
        

def Assistance(ref):
    ref. use_Assistance()
    ref.use_server()
    ref.use_os()

s = Siri()
a = Alexa()
g = Google()

Assistance(s)
Assistance(a)
Assistance(g)
