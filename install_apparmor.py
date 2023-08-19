#!/usr/bin/python3

#We would like to use subprocess module to install apparmor and its related utilities
import subprocess

packages = ['apparmor', 'apparmor-utils', 'apparmor-profiles']

for package in packages:
    try:
        subprocess.run(['apt', 'install','-y', package], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) #we are redirecting output to /dev/null and error to standard output.
        print(package + " installed successfully.")
    except:
        print("Error installing " + package + " .Please check.")
