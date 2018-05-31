from fabric.api import local

def test():
    local("cd tools")
    local("adb shell")
