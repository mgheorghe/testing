# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/linux/network/ip/neighbor.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.lib.test_lib_object import TestLibObject


class LinuxIpNeighbor(TestLibObject):
    """
        ip [ OPTIONS ] neigh { COMMAND | help }
        ip neigh { add | del | change | replace } { ADDR [ lladdr LLADDR ]
                 [ nud { permanent | noarp | stale | reachable } ] | proxy ADDR } [ dev DEV ]
        ip neigh { show | flush } [ proxy ] [ to PREFIX ] [ dev DEV ] [ nud STATE ]
        
    """
    def format_modify(self, command, *argv, **kwarg):
        raise NotImplementedError
        
    def parse_modify(self, command, output, *argv, **kwarg):
        raise NotImplementedError
        
    def format_show(self, command, *argv, **kwarg):
        raise NotImplementedError
        
    def parse_show(self, command, output, *argv, **kwarg):
        raise NotImplementedError
        
    def format_command(self, command, *argv, **kwarg):
        if command in ['add', 'delete', 'change', 'replace']:
            return self.format_modify(command, *argv, **kwarg)
        
        if command in ['show', 'flush']:
            return self.format_show(command, *argv, **kwarg)
        
        
        raise NameError("Cannot find command "+command)
        
    def parse_output(self, command, output, *argv, **kwarg):
        if command in ['add', 'delete', 'change', 'replace']:
            return self.parse_modify(command, output, *argv, **kwarg)
        
        if command in ['show', 'flush']:
            return self.parse_show(command, output, *argv, **kwarg)
        
        
        raise NameError("Cannot find command "+command)
        
