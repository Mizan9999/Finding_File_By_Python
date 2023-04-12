import os
import psutil


def disk_no():

    disk_have = []
    for disk in psutil.disk_partitions():
        if disk.fstype:
            have = disk.device[:3]
            disk_have.append(str(have))
    return disk_have


