# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/network/iptables/iptables.yaml
#
# DONOT EDIT - generated by diligent bots

import pytest

from dent_os_testbed.lib.iptables.linux.linux_ip_tables_impl import LinuxIpTablesImpl
from dent_os_testbed.lib.test_lib_object import TestLibObject


class IpTables(TestLibObject):
    """
        Iptables is used to set up, maintain, and inspect the tables of IPv4 packet filter rules in
        the Linux kernel.  Several different tables may be defined.  Each table contains a number
        of built-in chains and may also contain user-defined chains.
        Each chain is a list of rules which can match a set of packets.  Each rule specifies what to
        do with a packet that matches.  This is called a `target', which may be a jump to a user-defined
        chain in the same table.
        
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
                    impl_obj = LinuxIpTablesImpl()
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
        
    async def append(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.append(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'rulenum':'int',
                        'protocol':'string',
                        'source':'ip_addr_t',
                        'destination':'ip_addr_t',
                        'match':'string',
                        'target':'string',
                        'goto':'string',
                        'iif':'string',
                        'oif':'string',
                        'fragment':'bool',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -A, --append chain rule-specification
               Append one or more rules to the end of the selected chain.  When the source and/or destination names resolve
               to more than one address, a rule will be added for each possible  address combination.
        
        -C, --check chain rule-specification
               Check whether a rule matching the specification does exist in the selected chain. This command uses the same
               logic as -D to find a matching entry, but does not alter the existing
               iptables configuration and uses its exit code to indicate success or failure.
        
        -D, --delete chain rule-specification
        -D, --delete chain rulenum
               Delete one or more rules from the selected chain.  There are two versions of this command: the rule
               can be specified as a number in the chain (starting at 1 for the  first  rule) or a rule to match.
        -I, --insert chain [rulenum] rule-specification
             Insert  one or more rules in the selected chain as the given rule number.  So, if the rule number is 1,
             the rule or rules are inserted at the head of the chain.  This is also the
             default if no rule number is specified.
        -R, --replace chain rulenum rule-specification
             Replace a rule in the selected chain.  If the source and/or destination names resolve to multiple
             addresses, the command will fail.  Rules are numbered starting at 1.
        
        """
        return await IpTables._run_command("append", *argv, **kwarg)
        
    async def check(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.check(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'rulenum':'int',
                        'protocol':'string',
                        'source':'ip_addr_t',
                        'destination':'ip_addr_t',
                        'match':'string',
                        'target':'string',
                        'goto':'string',
                        'iif':'string',
                        'oif':'string',
                        'fragment':'bool',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -A, --append chain rule-specification
               Append one or more rules to the end of the selected chain.  When the source and/or destination names resolve
               to more than one address, a rule will be added for each possible  address combination.
        
        -C, --check chain rule-specification
               Check whether a rule matching the specification does exist in the selected chain. This command uses the same
               logic as -D to find a matching entry, but does not alter the existing
               iptables configuration and uses its exit code to indicate success or failure.
        
        -D, --delete chain rule-specification
        -D, --delete chain rulenum
               Delete one or more rules from the selected chain.  There are two versions of this command: the rule
               can be specified as a number in the chain (starting at 1 for the  first  rule) or a rule to match.
        -I, --insert chain [rulenum] rule-specification
             Insert  one or more rules in the selected chain as the given rule number.  So, if the rule number is 1,
             the rule or rules are inserted at the head of the chain.  This is also the
             default if no rule number is specified.
        -R, --replace chain rulenum rule-specification
             Replace a rule in the selected chain.  If the source and/or destination names resolve to multiple
             addresses, the command will fail.  Rules are numbered starting at 1.
        
        """
        return await IpTables._run_command("check", *argv, **kwarg)
        
    async def delete(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.delete(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'rulenum':'int',
                        'protocol':'string',
                        'source':'ip_addr_t',
                        'destination':'ip_addr_t',
                        'match':'string',
                        'target':'string',
                        'goto':'string',
                        'iif':'string',
                        'oif':'string',
                        'fragment':'bool',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -A, --append chain rule-specification
               Append one or more rules to the end of the selected chain.  When the source and/or destination names resolve
               to more than one address, a rule will be added for each possible  address combination.
        
        -C, --check chain rule-specification
               Check whether a rule matching the specification does exist in the selected chain. This command uses the same
               logic as -D to find a matching entry, but does not alter the existing
               iptables configuration and uses its exit code to indicate success or failure.
        
        -D, --delete chain rule-specification
        -D, --delete chain rulenum
               Delete one or more rules from the selected chain.  There are two versions of this command: the rule
               can be specified as a number in the chain (starting at 1 for the  first  rule) or a rule to match.
        -I, --insert chain [rulenum] rule-specification
             Insert  one or more rules in the selected chain as the given rule number.  So, if the rule number is 1,
             the rule or rules are inserted at the head of the chain.  This is also the
             default if no rule number is specified.
        -R, --replace chain rulenum rule-specification
             Replace a rule in the selected chain.  If the source and/or destination names resolve to multiple
             addresses, the command will fail.  Rules are numbered starting at 1.
        
        """
        return await IpTables._run_command("delete", *argv, **kwarg)
        
    async def insert(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.insert(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'rulenum':'int',
                        'protocol':'string',
                        'source':'ip_addr_t',
                        'destination':'ip_addr_t',
                        'match':'string',
                        'target':'string',
                        'goto':'string',
                        'iif':'string',
                        'oif':'string',
                        'fragment':'bool',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -A, --append chain rule-specification
               Append one or more rules to the end of the selected chain.  When the source and/or destination names resolve
               to more than one address, a rule will be added for each possible  address combination.
        
        -C, --check chain rule-specification
               Check whether a rule matching the specification does exist in the selected chain. This command uses the same
               logic as -D to find a matching entry, but does not alter the existing
               iptables configuration and uses its exit code to indicate success or failure.
        
        -D, --delete chain rule-specification
        -D, --delete chain rulenum
               Delete one or more rules from the selected chain.  There are two versions of this command: the rule
               can be specified as a number in the chain (starting at 1 for the  first  rule) or a rule to match.
        -I, --insert chain [rulenum] rule-specification
             Insert  one or more rules in the selected chain as the given rule number.  So, if the rule number is 1,
             the rule or rules are inserted at the head of the chain.  This is also the
             default if no rule number is specified.
        -R, --replace chain rulenum rule-specification
             Replace a rule in the selected chain.  If the source and/or destination names resolve to multiple
             addresses, the command will fail.  Rules are numbered starting at 1.
        
        """
        return await IpTables._run_command("insert", *argv, **kwarg)
        
    async def replace(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.replace(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'rulenum':'int',
                        'protocol':'string',
                        'source':'ip_addr_t',
                        'destination':'ip_addr_t',
                        'match':'string',
                        'target':'string',
                        'goto':'string',
                        'iif':'string',
                        'oif':'string',
                        'fragment':'bool',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -A, --append chain rule-specification
               Append one or more rules to the end of the selected chain.  When the source and/or destination names resolve
               to more than one address, a rule will be added for each possible  address combination.
        
        -C, --check chain rule-specification
               Check whether a rule matching the specification does exist in the selected chain. This command uses the same
               logic as -D to find a matching entry, but does not alter the existing
               iptables configuration and uses its exit code to indicate success or failure.
        
        -D, --delete chain rule-specification
        -D, --delete chain rulenum
               Delete one or more rules from the selected chain.  There are two versions of this command: the rule
               can be specified as a number in the chain (starting at 1 for the  first  rule) or a rule to match.
        -I, --insert chain [rulenum] rule-specification
             Insert  one or more rules in the selected chain as the given rule number.  So, if the rule number is 1,
             the rule or rules are inserted at the head of the chain.  This is also the
             default if no rule number is specified.
        -R, --replace chain rulenum rule-specification
             Replace a rule in the selected chain.  If the source and/or destination names resolve to multiple
             addresses, the command will fail.  Rules are numbered starting at 1.
        
        """
        return await IpTables._run_command("replace", *argv, **kwarg)
        
    async def list(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.list(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'chain':'string',
                        'rulenum':'int',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -L, --list [chain]
         List all rules in the selected chain.  If no chain is selected, all chains are listed. Like every other
         iptables command, it applies to the specified table  (filter  is  the  default), so NAT rules get listed by
          iptables -t nat -n -L
          Please note that it is often used with the -n option, in order to avoid long reverse DNS lookups.
          It is legal to specify the -Z (zero) option as well, in which case the chain(s) will be atomically listed
          and zeroed.  The exact output is affected by the other arguments given. The exact rules are suppressed
          until you use iptables -L -v  or iptables-save(8).
        
        -S, --list-rules [chain]
         Print all rules in the selected chain.  If no chain is selected, all chains are printed like iptables-save.
         Like every other iptables command, it applies to the  specified  table (filter is the default).
        
        -F, --flush [chain]
         Flush the selected chain (all the chains in the table if none is given).  This is equivalent to deleting
         all the rules one by one.
        
        -Z, --zero [chain [rulenum]]
         Zero  the  packet and byte counters in all chains, or only the given chain, or only the given rule in a chain.
         It is legal to specify the -L, --list (list) option as well, to see the counters immediately before they are
         cleared. (See above.)
        
        """
        return await IpTables._run_command("list", *argv, **kwarg)
        
    async def list_rules(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.list_rules(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'chain':'string',
                        'rulenum':'int',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -L, --list [chain]
         List all rules in the selected chain.  If no chain is selected, all chains are listed. Like every other
         iptables command, it applies to the specified table  (filter  is  the  default), so NAT rules get listed by
          iptables -t nat -n -L
          Please note that it is often used with the -n option, in order to avoid long reverse DNS lookups.
          It is legal to specify the -Z (zero) option as well, in which case the chain(s) will be atomically listed
          and zeroed.  The exact output is affected by the other arguments given. The exact rules are suppressed
          until you use iptables -L -v  or iptables-save(8).
        
        -S, --list-rules [chain]
         Print all rules in the selected chain.  If no chain is selected, all chains are printed like iptables-save.
         Like every other iptables command, it applies to the  specified  table (filter is the default).
        
        -F, --flush [chain]
         Flush the selected chain (all the chains in the table if none is given).  This is equivalent to deleting
         all the rules one by one.
        
        -Z, --zero [chain [rulenum]]
         Zero  the  packet and byte counters in all chains, or only the given chain, or only the given rule in a chain.
         It is legal to specify the -L, --list (list) option as well, to see the counters immediately before they are
         cleared. (See above.)
        
        """
        return await IpTables._run_command("list_rules", *argv, **kwarg)
        
    async def flush(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.flush(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'chain':'string',
                        'rulenum':'int',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -L, --list [chain]
         List all rules in the selected chain.  If no chain is selected, all chains are listed. Like every other
         iptables command, it applies to the specified table  (filter  is  the  default), so NAT rules get listed by
          iptables -t nat -n -L
          Please note that it is often used with the -n option, in order to avoid long reverse DNS lookups.
          It is legal to specify the -Z (zero) option as well, in which case the chain(s) will be atomically listed
          and zeroed.  The exact output is affected by the other arguments given. The exact rules are suppressed
          until you use iptables -L -v  or iptables-save(8).
        
        -S, --list-rules [chain]
         Print all rules in the selected chain.  If no chain is selected, all chains are printed like iptables-save.
         Like every other iptables command, it applies to the  specified  table (filter is the default).
        
        -F, --flush [chain]
         Flush the selected chain (all the chains in the table if none is given).  This is equivalent to deleting
         all the rules one by one.
        
        -Z, --zero [chain [rulenum]]
         Zero  the  packet and byte counters in all chains, or only the given chain, or only the given rule in a chain.
         It is legal to specify the -L, --list (list) option as well, to see the counters immediately before they are
         cleared. (See above.)
        
        """
        return await IpTables._run_command("flush", *argv, **kwarg)
        
    async def zero(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.zero(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'chain':'string',
                        'rulenum':'int',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -L, --list [chain]
         List all rules in the selected chain.  If no chain is selected, all chains are listed. Like every other
         iptables command, it applies to the specified table  (filter  is  the  default), so NAT rules get listed by
          iptables -t nat -n -L
          Please note that it is often used with the -n option, in order to avoid long reverse DNS lookups.
          It is legal to specify the -Z (zero) option as well, in which case the chain(s) will be atomically listed
          and zeroed.  The exact output is affected by the other arguments given. The exact rules are suppressed
          until you use iptables -L -v  or iptables-save(8).
        
        -S, --list-rules [chain]
         Print all rules in the selected chain.  If no chain is selected, all chains are printed like iptables-save.
         Like every other iptables command, it applies to the  specified  table (filter is the default).
        
        -F, --flush [chain]
         Flush the selected chain (all the chains in the table if none is given).  This is equivalent to deleting
         all the rules one by one.
        
        -Z, --zero [chain [rulenum]]
         Zero  the  packet and byte counters in all chains, or only the given chain, or only the given rule in a chain.
         It is legal to specify the -L, --list (list) option as well, to see the counters immediately before they are
         cleared. (See above.)
        
        """
        return await IpTables._run_command("zero", *argv, **kwarg)
        
    async def new_chain(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.new_chain(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'chain':'string',
                        'target':'string',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -N, --new-chain chain
         Create a new user-defined chain by the given name.  There must be no target of that name already.
        -X, --delete-chain [chain]
         Delete the optional user-defined chain specified.  There must be no references to the chain.
         If there are, you must delete or replace the referring rules before the chain can be deleted.
         The chain must be empty, i.e. not contain any rules.  If no argument is given, it will attempt
         to delete every non-builtin chain in the table.
        
        -P, --policy chain target
         Set the policy for the built-in (non-user-defined) chain to the given target.  The policy target
         must be either ACCEPT or DROP.
        
        -E, --rename-chain old-chain new-chain
         Rename the user specified chain to the user supplied name.  This is cosmetic, and has no effect
         on the structure of the table.
        
        """
        return await IpTables._run_command("new_chain", *argv, **kwarg)
        
    async def policy(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.policy(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'chain':'string',
                        'target':'string',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -N, --new-chain chain
         Create a new user-defined chain by the given name.  There must be no target of that name already.
        -X, --delete-chain [chain]
         Delete the optional user-defined chain specified.  There must be no references to the chain.
         If there are, you must delete or replace the referring rules before the chain can be deleted.
         The chain must be empty, i.e. not contain any rules.  If no argument is given, it will attempt
         to delete every non-builtin chain in the table.
        
        -P, --policy chain target
         Set the policy for the built-in (non-user-defined) chain to the given target.  The policy target
         must be either ACCEPT or DROP.
        
        -E, --rename-chain old-chain new-chain
         Rename the user specified chain to the user supplied name.  This is cosmetic, and has no effect
         on the structure of the table.
        
        """
        return await IpTables._run_command("policy", *argv, **kwarg)
        
    async def rename_chain(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        IpTables.rename_chain(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'table':'string',
                        'chain':'string',
                        'target':'string',
                        'options':'undefined',
                }],
            }],
        )
        Description:
        -N, --new-chain chain
         Create a new user-defined chain by the given name.  There must be no target of that name already.
        -X, --delete-chain [chain]
         Delete the optional user-defined chain specified.  There must be no references to the chain.
         If there are, you must delete or replace the referring rules before the chain can be deleted.
         The chain must be empty, i.e. not contain any rules.  If no argument is given, it will attempt
         to delete every non-builtin chain in the table.
        
        -P, --policy chain target
         Set the policy for the built-in (non-user-defined) chain to the given target.  The policy target
         must be either ACCEPT or DROP.
        
        -E, --rename-chain old-chain new-chain
         Rename the user specified chain to the user supplied name.  This is cosmetic, and has no effect
         on the structure of the table.
        
        """
        return await IpTables._run_command("rename_chain", *argv, **kwarg)
        
