import re

def ethereumtrue(ethereumaddress):
    if not isinstance(ethereumaddress, str):
        return False
    conditioncheck = re.match(r'^0x[0-9a-fA-F]{40}$', ethereumaddress)

    return bool(conditioncheck)
check2=ethereumtrue("0x17BcaBd1F23e25B5FB31446F851e4644eE8F90b0")
print(check2)
