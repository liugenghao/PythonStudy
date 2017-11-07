__Author__ = 'Bill Lau'
import requests
i1 = requests.get(url="http://dig.chouti.com/")
i2 = requests.post(
    url="http://dig.chouti.com/login",
    data={
        'phone':'8613618688800',
        'password':'111122qq',
        'oneMonth':''
    },
    cookies=i1.cookies.get_dict()
)
gpsd = i1.cookies.get_dict()['gpsd']
i3 = requests.post(
    url="http://dig.chouti.com/link/vote?linksId=15105956",
    cookies={'gpsd':gpsd}
)

print(i3.text)