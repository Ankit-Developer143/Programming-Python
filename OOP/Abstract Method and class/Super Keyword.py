from abc import ABC , abstractmethod

class computer(ABC):
    pass

@abstractmethod
def process(self):
    pass

class laptop(computer):
    def process(self):
        print("Process ongoing...")
        
class desktop(laptop):
    def process(self):
        
        #Using superKeyword
        super().process()
       
        print("progress....desktop")
        
        
# l = laptop()
# l.process()
d = desktop()
d.process()

# Process ongoing...
# progress....desktop
