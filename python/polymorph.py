class Messanger:
    def use_keyboard(self):
        print('use keyboard')
    def send_message(self):
        print('send message')
    def recive_message(self):
        print('recive message')
        
        
class Whatsapp(Messanger):
    def send_message(self):
        print('send message using whatsapp')
    def recive_message(self):
        print('recive message using whatsapp')
    def location(self):
        print('send live location')
        
        
class Facebook(Messanger):
    def send_message(self):
        print('send message using Facebook')
    def recive_message(self):
        print('recive message using Facebook')
    def built_app(self):
        print('built in apps')
        
        
class Insta(Messanger):
    def send_message(self):
        print('send message using insta')
    def recive_message(self):
        print('recive message using insta')
    def use_filter(self):
        print('use filers')

def use_messenger(ref):
    ref.use_keyboard()
    ref.send_message()
    ref.recive_message()
    if type(ref) == Whatsapp:
        ref.location()
    if type(ref) == Facebook:
        ref.built_app()
    if type(ref) == Insta:
        ref.use_filter()

Wa = Whatsapp()
Fb = Facebook()
In = Insta()

use_messenger(Wa)
use_messenger(Fb)
use_messenger(In)