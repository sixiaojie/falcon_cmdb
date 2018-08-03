
from base import Base

class rsync(Base):

    def __init__(self):
        Base.__init__()
        self.add_user = ""

    def _add_user(self,user):
        pass

    def _add_usergroup(self,usergroupname,user_list):
        pass

    def _del_usergroup(self,usergroupname):
        pass

    def _del_user(self,user):
        pass

    def _add_hostgroup(self,groupname):
        pass

    def _del_hostgroup(self,groupname):
        pass

    def _add_host(self,hostname):
        pass

    def _del_host(self,hostname):
        pass

    def _bindorremove_host_group(self,groupname,host_list):
        pass
