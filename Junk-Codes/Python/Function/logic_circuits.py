def or_gate(a, b):
    if a == True or b == True:
        return True
    else:
        return False


def and_gate(a, b):
    if a == True and b == True:
        return True
    else:
        return False


def not_gate(a):
    if a == True:
        return False
    else:
        return True


def xor_gate(a, b):
    if a != b:
        return True
    else:
        return False


def nand_gate(a, b):
    if a == False or b == False:
        return True
    else:
        return False


def nor_gate(a, b):
    if a == True or b == True:
        return False
    else:
        return True


def xnor_gate(a, b):
    if a == b:
        return True
    else:
        return False
