py_header = """# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file %s
#
# DONOT EDIT - generated by diligent bots
"""
py_class_common_impl_form_command="""        if device_obj.os in %(platforms)s:
            impl_obj = %(cname_cc)sImpl()
            for command in device[device_name]:
                commands += impl_obj.format_command(command=api, params=command)
                commands += '&& '
            commands = commands[:-3]
"""
py_class_common_run ="""devices = kwarg['input_data']
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
%(impl_form_cmd)s
        else:
            device_result[device_name]['rc'] = -1
            device_result[device_name]['result'] = "No matching device OS "+ device_obj.os
            result.append(device_result)
            return result
        device_result[device_name]['command'] = commands
        try:
            %(invoke_command)s
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
"""

py_class_common_run_api ="""\"\"\"
Platforms: %(platforms)s
Usage:
%(cname_cc)s.%(cls_api)s(
    input_data = [{
        # device 1
        'dev1' : [{
            # command 1
%(params)s
        }],
    }],
)
Description:
%(cmd_desc)s
\"\"\"
return await %(cname_cc)s._run_command("%(cls_api)s", *argv, **kwarg)
"""

py_class_common_format_cmd_case = """if command in %(cmds)s:
    return self.format_%(cmd)s(command, *argv, **kwarg)

"""
py_class_common_format_cmds = """%(format_entries)s
raise NameError("Cannot find command "+command)
"""

py_class_common_format_cmd = """raise NotImplementedError
"""

py_class_common_run_cmd_case = """if command in %(cmds)s:
    return self.run_%(cmd)s(device_obj, command, *argv, **kwarg)

"""
py_class_common_run_cmds = """%(run_entries)s
print (len(command))
raise NameError("Cannot find command "+command)
"""

py_class_common_run_cmd = """raise NotImplementedError
"""

py_class_common_parse_cmd_case = """if command in %(cmds)s:
    return self.parse_%(cmd)s(command, output, *argv, **kwarg)

"""
py_class_common_parse_cmds = """%(parse_entries)s
raise NameError("Cannot find command "+command)
"""

py_class_common_parse_cmd = """raise NotImplementedError
"""

py_impl_class_common_format_cmd = """\"\"\"
%(cmd_desc)s
\"\"\"
params = kwarg["params"]
cmd = '%(cmd)s {} '.format(command)
############# Implement me ################

return cmd
"""

py_impl_class_common_run_cmd = """\"\"\"
%(cmd_desc)s
\"\"\"
############# Implement me ################

return 0,""
"""

py_impl_class_common_parse_cmd = """\"\"\"
%(cmd_desc)s
\"\"\"
parse_out = output.split(" ")
############# Implement me ################

return parse_out
"""

py_test_code_two_cmd_template_call = """
loop = asyncio.get_event_loop()
out = loop.run_until_complete(%(cname_cc)s.%(api)s(input_data = [{
    # device 1
    'test_dev1' : [{
    # command 1
%(params1)s
    },{
    # command 2
%(params2)s
    }],
}], device_obj={'test_dev1':dv1, 'test_dev2':dv2}))
print(out)
# check if the command was formed
assert 'command' in out[0]['test_dev1'].keys()
# check if the result was formed
assert 'result' in out[0]['test_dev1'].keys()
# check the rc
assert out[0]['test_dev1']["rc"] == 0
"""

py_test_code_two_dev_template_call = """
loop = asyncio.get_event_loop()
out = loop.run_until_complete(%(cname_cc)s.%(api)s(input_data = [{
    # device 1
    'test_dev1' : [{
%(params1)s
     }],
     # device 2
     'test_dev2' : [{
%(params2)s
    }],
}], device_obj={'test_dev1':dv1, 'test_dev2':dv2}))
print(out)
# check if the command was formed
assert 'command' in out[0]['test_dev1'].keys()
assert 'command' in out[1]['test_dev2'].keys()
# check if the result was formed
assert 'result' in out[0]['test_dev1'].keys()
assert 'result' in out[1]['test_dev2'].keys()
# check the rc
assert out[0]['test_dev1']["rc"] == 0
assert out[1]['test_dev2']["rc"] == 0
"""

py_test_code_template = """
dv1 = TestDevice(platform="%(platform)s")
dv2 = TestDevice(platform="%(platform)s")
loop = asyncio.get_event_loop()
out = loop.run_until_complete(%(cname_cc)s.%(api)s(input_data = [{
    # device 1
    'test_dev' : [{}],
}], device_obj={'test_dev':dv1}))
print(out)
assert 'command' in out[0]['test_dev'].keys()
assert 'result' in out[0]['test_dev'].keys()
# check the rc
assert out[0]['test_dev']["rc"] == 0
%(cases)s
"""
