from abc import ABC,abstractmethod
class chat(ABC):
    def __init__(self,send,recive):
        self.send = send
        self.recive = recive
    @abstractmethod
    def msg_sent(self):
        pass
    @abstractmethod
    def msg_recive(self):
        pass
    def __str__(self):
        return f'{self.send}\n{self.recive}\n'
class Fb(chat):
    def msg_sent(self):
        print('sent in fb')
    def msg_recive(self):
        print('recive in fb')
class Inst(chat):
    def msg_sent(self):
        print('send in inst')
    def msg_recive(self):
        print('recive in inst')

def dis(ref):
    ref.msg_sent()
    ref.msg_recive()
    print(ref)

f = Fb('hello.img','hi.img')
i = Inst('hello.mp4','hi.mp4')

dis(f)
dis(i)