# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/network/tc/tc.yaml
#
# DONOT EDIT - generated by diligent bots

import pytest

from dent_os_testbed.lib.tc.linux.linux_tc_qdisc_impl import LinuxTcQdiscImpl
from dent_os_testbed.lib.test_lib_object import TestLibObject


class TcQdisc(TestLibObject):
    """
        - tc [ OPTIONS ] qdisc [ add | change | replace | link | delete ] dev DEV [ parent qdisc-id | root ]
        [ handle qdisc-id ] [ ingress_block BLOCK_INDEX ] [ egress_block BLOCK_INDEX ] qdisc
        [ qdisc specific parameters ]
        - tc [ OPTIONS ] [ FORMAT ] qdisc show [ dev DEV ]
        OPTIONS := { [ -force ] -b[atch] [ filename ] | [ -n[etns] name ] | [ -nm | -nam[es] ] |
          [ { -cf | -c[onf] } [ filename ] ] [ -t[imestamp] ] | [ -t[short] | [ -o[neline] ] }
        FORMAT := { -s[tatistics] | -d[etails] | -r[aw] | -i[ec] | -g[raph] | -j[json] | -p[retty] | -col[or] }
        
    """
    async def _run_command(api, *argv, **kwarg):
        devices = kwarg['input_data']
        result = list()
        for device in devices:
            for device_name in device:
                device_result = {
                    device_name : dict()
                }
                # device lookup
                if 'device_obj' in kwarg:
                    device_obj = kwarg.get('device_obj', None)[device_name]
                else:
                    if device_name not in pytest.testbed.devices_dict:
                        device_result[device_name] =  "No matching device "+ device_name
                        result.append(device_result)
                        return result
                    device_obj = pytest.testbed.devices_dict[device_name]
                commands = ""
                if device_obj.os in ['dentos', 'cumulus']:
                    impl_obj = LinuxTcQdiscImpl()
                    for command in device[device_name]:
                        commands += impl_obj.format_command(command=api, params=command)
                        commands += '&& '
                    commands = commands[:-3]
        
                else:
                    device_result[device_name]['rc'] = -1
                    device_result[device_name]['result'] = "No matching device OS "+ device_obj.os
                    result.append(device_result)
                    return result
                device_result[device_name]['command'] = commands
                try:
                    rc, output = await device_obj.run_cmd(("sudo " if device_obj.ssh_conn_params.pssh else "") + commands)
                    device_result[device_name]['rc'] = rc
                    device_result[device_name]['result'] = output
                    if 'parse_output' in kwarg:
                        parse_output = impl_obj.parse_output(command=api, output=output, commands=commands)
                        device_result[device_name]['parsed_output'] = parse_output
                except Exception as e:
                    device_result[device_name]['rc'] = -1
                    device_result[device_name]['result'] = str(e)
                result.append(device_result)
        return result
        
    async def add(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcQdisc.add(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'root':'bool',
                        'handle':'int',
                        'ingress_block':'int',
                        'egress_block':'string',
                        'qdisc':'int',
                        'options':'string',
                        'format':'string',
                }],
            }],
        )
        Description:
        tc  [  OPTIONS ] qdisc [ add | change | replace | link | delete ] dev DEV [ parent
        qdisc-id | root ] [ handle qdisc-id ] [ ingress_block BLOCK_INDEX ] [ egress_block
        BLOCK_INDEX ] qdisc [ qdisc specific parameters ]
        
        """
        return await TcQdisc._run_command("add", *argv, **kwarg)
        
    async def change(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcQdisc.change(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'root':'bool',
                        'handle':'int',
                        'ingress_block':'int',
                        'egress_block':'string',
                        'qdisc':'int',
                        'options':'string',
                        'format':'string',
                }],
            }],
        )
        Description:
        tc  [  OPTIONS ] qdisc [ add | change | replace | link | delete ] dev DEV [ parent
        qdisc-id | root ] [ handle qdisc-id ] [ ingress_block BLOCK_INDEX ] [ egress_block
        BLOCK_INDEX ] qdisc [ qdisc specific parameters ]
        
        """
        return await TcQdisc._run_command("change", *argv, **kwarg)
        
    async def replace(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcQdisc.replace(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'root':'bool',
                        'handle':'int',
                        'ingress_block':'int',
                        'egress_block':'string',
                        'qdisc':'int',
                        'options':'string',
                        'format':'string',
                }],
            }],
        )
        Description:
        tc  [  OPTIONS ] qdisc [ add | change | replace | link | delete ] dev DEV [ parent
        qdisc-id | root ] [ handle qdisc-id ] [ ingress_block BLOCK_INDEX ] [ egress_block
        BLOCK_INDEX ] qdisc [ qdisc specific parameters ]
        
        """
        return await TcQdisc._run_command("replace", *argv, **kwarg)
        
    async def link(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcQdisc.link(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'root':'bool',
                        'handle':'int',
                        'ingress_block':'int',
                        'egress_block':'string',
                        'qdisc':'int',
                        'options':'string',
                        'format':'string',
                }],
            }],
        )
        Description:
        tc  [  OPTIONS ] qdisc [ add | change | replace | link | delete ] dev DEV [ parent
        qdisc-id | root ] [ handle qdisc-id ] [ ingress_block BLOCK_INDEX ] [ egress_block
        BLOCK_INDEX ] qdisc [ qdisc specific parameters ]
        
        """
        return await TcQdisc._run_command("link", *argv, **kwarg)
        
    async def delete(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcQdisc.delete(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'root':'bool',
                        'handle':'int',
                        'ingress_block':'int',
                        'egress_block':'string',
                        'qdisc':'int',
                        'options':'string',
                        'format':'string',
                }],
            }],
        )
        Description:
        tc  [  OPTIONS ] qdisc [ add | change | replace | link | delete ] dev DEV [ parent
        qdisc-id | root ] [ handle qdisc-id ] [ ingress_block BLOCK_INDEX ] [ egress_block
        BLOCK_INDEX ] qdisc [ qdisc specific parameters ]
        
        """
        return await TcQdisc._run_command("delete", *argv, **kwarg)
        
    async def show(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcQdisc.show(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'options':'string',
                        'format':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] [ FORMAT ] qdisc show [ dev DEV ]
        
        """
        return await TcQdisc._run_command("show", *argv, **kwarg)
        
