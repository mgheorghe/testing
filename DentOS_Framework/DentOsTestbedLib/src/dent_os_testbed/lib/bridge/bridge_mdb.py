# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/network/bridge/bridge.yaml
#
# DONOT EDIT - generated by diligent bots

import pytest
from dent_os_testbed.lib.test_lib_object import TestLibObject
from dent_os_testbed.lib.bridge.linux.linux_bridge_mdb_impl import LinuxBridgeMdbImpl
class BridgeMdb(TestLibObject):
    """
        mdb objects contain known IP multicast group addresses on a link.
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
                    impl_obj = LinuxBridgeMdbImpl()
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
        BridgeMdb.add(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'port':'int',
                        'grp':'int',
                        'permanent':'bool',
                        'temp':'bool',
                        'vid':'int',
                }],
            }],
        )
        Description:
        bridge mdb { add | del } dev DEV port PORT grp GROUP [ permanent | temp ] [ vid VID ]

        """
        return await BridgeMdb._run_command("add", *argv, **kwarg)

    async def delete(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        BridgeMdb.delete(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'port':'int',
                        'grp':'int',
                        'permanent':'bool',
                        'temp':'bool',
                        'vid':'int',
                }],
            }],
        )
        Description:
        bridge mdb { add | del } dev DEV port PORT grp GROUP [ permanent | temp ] [ vid VID ]

        """
        return await BridgeMdb._run_command("delete", *argv, **kwarg)

    async def show(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        BridgeMdb.show(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'options':'string',
                }],
            }],
        )
        Description:
        bridge mdb show [ dev DEV ]

        """
        return await BridgeMdb._run_command("show", *argv, **kwarg)

