# Authot:Bill Lew
import time
user= "bill"
pwd = "111122"

def auth(*auth_type):
    print("auth_type is：",*auth_type)
    def outter_wrapper(func):
        def wrapper(*args,**kwargs):
            print("wrapper func args:",*args,**kwargs)
            if auth_type[0]== 'local':
                usernamme = input('Username:').strip()
                password = input('Password:').strip()
                if usernamme == user and password == pwd:
                    print("\033[32;1m登录成功.\033[0m")
                else:
                    print("\033[31;1m登录失败.\033[0m")
                return func(*args,**kwargs)
            else:
                print("\033[31;只能本地登录\033[0m")
        return wrapper
    return  outter_wrapper



def index():
    print("Welcome index page")
@auth('local')
def home():
    print("Welcome home page")
@auth('remote')
def bbs():
    print("Welcome bbs page")
index()
home()
bbs()