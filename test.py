import os.path as op

from adb import adb_commands
from adb import sign_m2crypto

print "hello"
# KitKat+ devices require authentication
signer = sign_m2crypto.M2CryptoSigner(
    op.expanduser('~/.android/adbkey'))
# Connect to the device
device = adb_commands.AdbCommands()

device.ConnectDevice(
    rsa_keys=[signer])
# Now we can use Shell, Pull, Push, etc!
print device.Shell('input tap 480 570')
#print device.Shell('touch 100 100')
