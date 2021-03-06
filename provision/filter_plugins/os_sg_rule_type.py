#!/usr/bin/env python
import os
import sys
import abc
import StringIO
from ansible import errors

def translate_ruletype(ruletype):
    if ruletype == "inbound":
        return "ingress"
    if ruletype == "outbound":
        return "egress"
    else:
        return "invalid ruletype "

class FilterModule(object):
    ''' A filter to fix network format '''
    def filters(self):
        return {
            'os_sg_rule_type': translate_ruletype
        }
