#!/usr/bin/env python3
"""Access keys in a dictionary with the dict.get() method"""

def main():
    """runtime function"""

    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}
    ## display the entire dictionary
    print(switch)

    ##prove that switch is indeed a dictionary
    print(type(switch))

    ##display parts of the dictionary
    print(switch["hostname"]) 
    print(switch"ip"])

    print("first test - .get()")
    print(switch.get("lynx"))

    print("second test - .get()")
    print(switch.get("lynx","The Key is in another castle!"))

    print("third test - .get()")
    printSwitch.get("version"))

