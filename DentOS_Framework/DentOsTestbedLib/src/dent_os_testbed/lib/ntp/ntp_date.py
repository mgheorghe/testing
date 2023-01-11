# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/protocol/ntp/ntp.yaml
#
# DONOT EDIT - generated by diligent bots

import pytest

from dent_os_testbed.lib.ntp.linux.linux_ntp_date_impl import LinuxNtpDateImpl
from dent_os_testbed.lib.test_lib_object import TestLibObject


class NtpDate(TestLibObject):
    """
    ntpdate - set the date and time via NTP
    ntpdate [-46bBdqsuv] [-a key] [-e authdelay] [-k keyfile] [-o version]
      [-p samples] [-t timeout] server [...]

    """

    async def _run_command(api, *argv, **kwarg):
        devices = kwarg["input_data"]
        result = list()
        for device in devices:
            for device_name in device:
                device_result = {device_name: dict()}
                # device lookup
                if "device_obj" in kwarg:
                    device_obj = kwarg.get("device_obj", None)[device_name]
                else:
                    if device_name not in pytest.testbed.devices_dict:
                        device_result[device_name] = "No matching device " + device_name
                        result.append(device_result)
                        return result
                    device_obj = pytest.testbed.devices_dict[device_name]
                commands = ""
                if device_obj.os in ["dentos", "cumulus"]:
                    impl_obj = LinuxNtpDateImpl()
                    for command in device[device_name]:
                        commands += impl_obj.format_command(command=api, params=command)
                        commands += "&& "
                    commands = commands[:-3]

                else:
                    device_result[device_name]["rc"] = -1
                    device_result[device_name]["result"] = "No matching device OS " + device_obj.os
                    result.append(device_result)
                    return result
                device_result[device_name]["command"] = commands
                try:
                    rc, output = await device_obj.run_cmd(
                        ("sudo " if device_obj.ssh_conn_params.pssh else "") + commands
                    )
                    device_result[device_name]["rc"] = rc
                    device_result[device_name]["result"] = output
                    if "parse_output" in kwarg:
                        parse_output = impl_obj.parse_output(
                            command=api, output=output, commands=commands
                        )
                        device_result[device_name]["parsed_output"] = parse_output
                except Exception as e:
                    device_result[device_name]["rc"] = -1
                    device_result[device_name]["result"] = str(e)
                result.append(device_result)
        return result

    async def set(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        NtpDate.set(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'servers':'string_list',
                        'command_options':'string',
                        'key':'string',
                        'authdelay':'float',
                        'keyfile':'string',
                        'version':'string',
                        'samples':'int',
                        'timeout':'float',
                }],
            }],
        )
        Description:
        ntpdate [-46bBdqsuv] [-a key] [-e authdelay] [-k keyfile] [-o version] [-p samples] [-t timeout] server [...]
         -4     - Force DNS resolution of following host names on the command line to the IPv4 namespace.
         -6     - Force DNS resolution of following host names on the command line to the IPv6 namespace.
         -a key - Enable the authentication function and specify the key identifier to be used for
                  authentication as the argument keyntpdate. The keys and key identifiers must match in
                  both the client and server key files. The default is to disable the authentication function.
         -B     - Force the time to always be slewed using the adjtime() system call. This is the default.
         -b     - Force the time to be stepped using the settimeofday() system call, rather than slewed (default)
                  using the adjtime() system call. This option should be used when called from a startup
                  file at boot time.
         -d     - Enable the debugging mode, in which ntpdate will go through all the steps, but not adjust
                  the local clock and using an unprivileged port. Information useful for general debugging
                  will also be printed.
         -e     - authdelay Specify the processing delay to perform an authentication function as the value
                  authdelay, in seconds and fraction (see ntpd for details). This number is usually small
                  enough to be negligible for most purposes, though specifying a value may improve timekeeping
                  on very slow CPU's.
         -k keyfile - Specify the path for the authentication key file as the string keyfile. The default
                  is /etc/ntp.keys. This file should be in the format described in ntpd.
         -o version - Specify the NTP version for outgoing packets as the integer version, which can be
                     1, 2, 3 or 4. The default is 4. This allows ntpdate to be used with older NTP versions.
         -q     - Query only – don't set the clock.
         -s     - Divert logging output from the standard output (default) to the system syslog facility.
                 This is designed primarily for convenience of cron scripts.
         -t timeout - Specify the maximum time waiting for a server response as the value timeout, in seconds
                 and fraction. The value is rounded to a multiple of 0.2 seconds. The default is 1 second,
                 a value suitable for polling across a LAN.
         -u     - Direct ntpdate to use an unprivileged port for outgoing packets. This is most useful when
                  behind a firewall that blocks incoming traffic to privileged ports, and you want to
                  synchronise with hosts beyond the firewall. Note that the -d option always uses unprivileged ports.
         -v     - Be verbose. This option will cause ntpdate's version identification string to be logged.

        """
        return await NtpDate._run_command("set", *argv, **kwarg)
