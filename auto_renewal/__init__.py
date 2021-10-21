from auto_renewal.renewal import auto_renewal_func
from auto_renewal.credentials import cred


def renew():
    # print("Hello World")
    auto_renewal_func(userid= cred['username'],password= cred['password'])