# your code goes here!
import re

class EmailAddressParser:

    def __init__(self, addresses):
        self.addresses = addresses

    
    # | => or
    def parse(self):
        pattern = re.compile(r"[, ]+")
        addresses_list = pattern.split(self.addresses)
        return sorted(set([address for address in addresses_list if "@" in address]))
