# -*- coding: iso-8859-1 -*-
# Copyright (C) 2000-2005  Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import urllib

class ProxySupport (object):
    """get support for proxying and for urls with user:pass@host setting"""

    def set_proxy (self, proxy):
        """parse given proxy information and store parsed values"""
        self.proxy = proxy
        self.proxyauth = None
        if self.proxy:
            if self.proxy[:7].lower() != "http://":
                self.proxy = "http://"+self.proxy
            self.proxy = urllib.splittype(self.proxy)[1]
            self.proxy = urllib.splithost(self.proxy)[0]
            self.proxyauth, self.proxy = urllib.splituser(self.proxy)
            if self.proxyauth is not None:
                if ":" not in self.proxyauth:
                    self.proxyauth += ":"
                import base64
                self.proxyauth = base64.encodestring(self.proxyauth).strip()
                self.proxyauth = "Basic "+self.proxyauth
