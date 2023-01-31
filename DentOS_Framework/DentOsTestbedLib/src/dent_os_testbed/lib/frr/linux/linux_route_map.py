# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/linux/protocol/frr/routemap.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.lib.test_lib_object import TestLibObject


class LinuxRouteMap(TestLibObject):
    """
        vtysh
        
    """
    def format_configure(self, command, *argv, **kwarg):
        raise NotImplementedError
        
    def parse_configure(self, command, output, *argv, **kwarg):
        raise NotImplementedError
        
    def format_command(self, command, *argv, **kwarg):
        if command in ['configure']:
            return self.format_configure(command, *argv, **kwarg)
        
        
        raise NameError("Cannot find command "+command)
        
    def parse_output(self, command, output, *argv, **kwarg):
        if command in ['configure']:
            return self.parse_configure(command, output, *argv, **kwarg)
        
        
        raise NameError("Cannot find command "+command)
        
