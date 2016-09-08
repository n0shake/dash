from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue
import grequests

concurrent = 200

def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        # doSomethingWithResult(status, url)
        q.task_done()

def getStatus(ourl):
    try:
        url = urlparse(ourl)
        print ourl
        conn = httplib.HTTPConnection(url.netloc) 
        headers = { 'cookie': "myacinfo=DAWTKNV2d1f777b5bed504e0946ab8f8b381ff6c9a5fdc45a66547080881ac0d97b0228c7c7649455e887e7bbb9822859912bca2d7bc4f04af18bc8fcdb0bc83f7d9080e17ed7a8f15fb6a8a70adc721277f1fd79c25b5724fa95eefe6ac65f0bc09c97f9b81b79ca4f0ffded16ee44e2d78db5a9ceabadab706c895bb27d5aace0426ff156116b5b0e47151105d649b9fe76b293e66852390668fd844d9840e3b30d2349a6ef0d3fb5d2f878bd187af236ab7a65acd3071afc85a6c9bd996d17eabbd5691b2270f673c848c949c0c22fffd94807bf1ee9deb9c733fd0daa731e7f898f07697bbf8eb92e5c7a6399a33e30174c102547035a99f6ebfd61c35986898b535eed7d20add710cf66db02649bbfbd7d18b355e56cba43e94dd043990eb0f90e5MVRYV2;",
                    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}  
        conn.request("GET", url.path, headers = headers)
        res = conn.getresponse()
        return res.status, ourl
    except:
        return "error", ourl

def doSomethingWithResult(status, url):
    print status, url

header = {'Cookie' : 'myacinfo=DAWTKNV2d1f777b5bed504e0946ab8f8b381ff6c9a5fdc45a66547080881ac0d97b0228c7c7649455e887e7bbb9822859912bca2d7bc4f04af18bc8fcdb0bc83f7d9080e17ed7a8f15fb6a8a70adc721277f1fd79c25b5724fa95eefe6ac65f0bc09c97f9b81b79ca4f0ffded16ee44e2d78db5a9ceabadab706c895bb27d5aace0426ff156116b5b0e47151105d649b9fe76b293e66852390668fd844d9840e3b30d2349a6ef0d3fb5d2f878bd187af236ab7a65acd3071afc85a6c9bd996d17eabbd5691b2270f673c848c949c0c22fffd94807bf1ee9deb9c733fd0daa731e7f898f07697bbf8eb92e5c7a6399a33e30174c102547035a99f6ebfd61c35986898b535eed7d20add710cf66db02649bbfbd7d18b355e56cba43e94dd043990eb0f90e5MVRYV2; '}
urlArray = ['https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.40.0', 'https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.39.0',
            'https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.38.1', 'https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.38.0',
            'https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2', 'https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2','https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2','https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2','https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2','https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2','https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2','https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2','https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2','https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2','https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2','https://crashtracer.ios.apple.com/app/show/10044?osv=9.3.5&users=external&appv=9.37.2']
rs = (grequests.get(u, headers=header) for u in urlArray)
responses = grequests.map(rs)
i = 0
for response in responses:
    print response.status_code
    i+=1
print i
