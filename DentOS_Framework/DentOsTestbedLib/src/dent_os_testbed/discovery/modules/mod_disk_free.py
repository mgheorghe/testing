# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/system/os/disk.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.discovery.Module import Module
from dent_os_testbed.lib.os.disk_free import DiskFree


class DiskFreeMod(Module):
    """
    """
    def set_disk_free(self, src, dst):
        
        for i,disk_free in enumerate(src):
            if 'filesystem' in disk_free: dst[i].filesystem = disk_free.get('filesystem')
            if 'size' in disk_free: dst[i].size = disk_free.get('size')
            if 'used' in disk_free: dst[i].used = disk_free.get('used')
            if 'available' in disk_free: dst[i].available = disk_free.get('available')
            if 'use_percentage' in disk_free: dst[i].use_percentage = disk_free.get('use_percentage')
            if 'mounted_on' in disk_free: dst[i].mounted_on = disk_free.get('mounted_on')
        
        
    async def discover(self):
        # need to get device instance to get the data from
        #
        for i, dut in enumerate(self.report.duts):
            if not dut.device_id: continue
            dev = self.ctx.devices_dict[dut.device_id]
            if dev.os == "ixnetwork" or not await dev.is_connected():
                print("Device not connected skipping disk_free discovery")
                continue
            print("Running disk_free Discovery on " + dev.host_name)
            out = await DiskFree.show(
                input_data=[{dev.host_name: [{'dut_discovery':True}]}],
                device_obj={dev.host_name: dev},
                parse_output=True
            )
            if out[0][dev.host_name]["rc"] != 0:
                print(out)
                print("Failed to get disk_free")
                continue
            if 'parsed_output' not in out[0][dev.host_name]:
                print("Failed to get parsed_output disk_free")
                print (out)
                continue
            self.set_disk_free(out[0][dev.host_name]["parsed_output"], self.report.duts[i].system.os.disk)
            print("Finished disk_free Discovery on {} with {} entries".format(dev.host_name, len(self.report.duts[i].system.os.disk)))
        
