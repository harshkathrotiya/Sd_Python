#create a user define exception which check the host name if hostname not found
#raise a exception.
class NetworkError(RuntimeError):
    def __init__(self,arg):
        self.args=arg
try :
    raise NetworkError("bad hostname")
except NetworkError:
    print("network error")
