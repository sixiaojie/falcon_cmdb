from conf import mysql
from conf import Config
import urllib2
import json
import sys

class Base(object):

    def __init__(self):
        self.server = Config.Falcon
        self.header = {"Content-Type": "application/json"}
        self.username = Config.Falcon_user
        self.password = Config.Falcon_password
        self._set_header()

    def _set_header(self):
        sig = self._sig()
        token = {"name":self.username,"sig":sig}
        self.header["Apitoken"] = json.dumps(token)

    def _sig(self):
        url = "/api/v1/user/login"
        if self.server.endswith("/"):
            url = "api/v1/user/login"
        else:
            url = "/api/v1/user/login"
        userinfo = {"name":self.username,"password":self.password}
        url = self.server+ url
        result = self._response(url,json.dumps(userinfo))
        if result.has_key("sig"):
            return result["sig"]
        print "can't get sig"
        sys.exit(10)


    def _response(self,url,data):
        request = urllib2.Request(url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        try:
            result = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print "Failed, please Check:",e.message
            result = ""
        return result

    def _deal(self,data):
        try:
            result = json.loads(data.read())
        except Exception,e:
            print "data deal is error:"+e.message
            result = ""
        return result