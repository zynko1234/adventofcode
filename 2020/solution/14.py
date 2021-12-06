import util
from constants import COMMA, EMPTY_STRING, BASE_AND, BASE_OR

# Replacement strings.
MASK_STR = 'mask = '
MEM_STR_L = 'mem['
MEM_STR_R = '] = '

def solve(in_list):
    norm_list = normalize_input_A(in_list)
    ansA = util.sum_list(populate_memory_a(norm_list))
    
    ansB = populate_memory_b(norm_list)

    return ansA, ansB

def normalize_input_A(in_list: list):
    out_list = []

    for i in range(len(in_list)):
        
        # A new mask is found, overwrite the old one.
        if "mask" in in_list[i]:
            tmp_and = list(BASE_AND)
            tmp_or = list(BASE_OR)
            tmp_str = in_list[i].replace(MASK_STR, EMPTY_STRING)

            for j in range(len(tmp_str)):
                if tmp_str[j] == '0':
                    tmp_and[j] = '0'
                elif tmp_str[j] == '1':
                    tmp_or[j] = '1'

            # Change the mask contents.
            tmp_mask = Mask(EMPTY_STRING.join(tmp_and), EMPTY_STRING.join(tmp_or), tmp_str)

        # A new memory address and value are found, compound them with the
        # current mask, and append that to the output.
        elif "mem" in in_list[i]:
            tmp_str = in_list[i].replace(MEM_STR_L, EMPTY_STRING)
            tmp_str = tmp_str.replace(MEM_STR_R, COMMA)
            add_val = tmp_str.split(COMMA)
            out_list.append(AddrChange(tmp_mask, add_val[0], add_val[1]))

    return out_list

def get_max_addr(in_list: list):
    out_max = 0
    
    for entry in in_list:
        if entry.the_addr > out_max:
            out_max = entry.the_addr
        
    return out_max

def get_max_all_masked_addr(in_list: list):
    out_max = 0

    for entry in in_list:
        entry_max = entry.get_max_mask_addr()

        if out_max < entry_max:
            out_max = entry_max
    
    return out_max

def count_addr(in_list: list):
    out_count = 0
    
    for entry in in_list:
        out_count += entry.get_mask_addr_count()
    
    return out_count

def populate_memory_a(in_list: list):
    out_list = [0] * (get_max_addr(in_list) + 1)
    
    for i in range(len(in_list)):
        mask_val = in_list[i].get_computed_val()
        out_list[in_list[i].the_addr] = mask_val

    return out_list

def populate_memory_b(in_list: list):
    addMachine = AddrMachine()

    for i in range(len(in_list)):
        overwrite_value = in_list[i].the_value
        masked_addrs = in_list[i].get_computed_adds()

        for j in range(len(masked_addrs)):
            addMachine.change_val(masked_addrs[j], overwrite_value)

    return addMachine.sum_all_values()

def generate_float_masks(in_add: str):
    INDEX_NOT_FOUND = -1
    out_list = []    

    index = in_add.find('X')

    # Base case.
    if index == INDEX_NOT_FOUND:
        conv_add = int('0b{0}'.format(in_add), 2)
        out_list.append(conv_add)

    # Recursion case.
    else:
        # Recursion path split for floating X as 1
        tmp_add = util.replace_char(in_add, index, '1')
        out_list = out_list + generate_float_masks(tmp_add)

        # Recursion path split for floating X as 0
        tmp_add = util.replace_char(in_add, index, '0')
        out_list = out_list + generate_float_masks(tmp_add)

    return out_list

class Mask(object):
    def __init__(self, in_and, in_or, in_orig):
        self.the_and = int('0b{0}'.format(in_and), 2)
        self.the_or = int('0b{0}'.format(in_or), 2)
        self.the_orig = str(in_orig)

class AddrChange(object):

    def __init__(self, in_mask: Mask, in_addr, in_value):
        self.the_mask = in_mask
        self.the_addr = int(in_addr)
        self.the_value = int(in_value)
        self.the_masked_addrs = self.get_computed_adds()
        return

    def get_addr(self):
        return self.the_addr
    
    def get_computed_val(self):
        # OR mask then AND mask.
        new_value = (self.the_value | self.the_mask.the_or)
        new_value = (new_value & self.the_mask.the_and)
        return new_value

    def get_computed_adds(self):
        out_adds = []
        floating_adds = generate_float_masks(self.the_mask.the_orig)

        for entry in floating_adds:
            tmp_add = (self.the_addr | entry)
            out_adds.append(tmp_add)

        return out_adds

    def get_max_mask_addr(self):
        out_max = 0

        for entry in self.the_masked_addrs:
            if entry > out_max:
                out_max = entry
        
        return out_max

    def get_mask_addr_count(self):
        return len(self.the_masked_addrs)

    
class AddrVal(object):
    def __init__(self, in_addr = 0, in_value = 0):
        self.the_addr = in_addr
        self.the_value = in_value
    
    def set_val(self, in_value):
        self.the_value = in_value

    def set_addr(self, in_addr):
        self.the_addr = in_addr

class AddrMachine(object):
    def __init__(self):
        self.the_machine = []
    
    def change_val(self, in_addr, in_value):
        exists = False

        for i in range(len(self.the_machine)):
            if self.the_machine[i].the_addr == in_addr:
                self.the_machine[i].the_value = in_value
                exists = True

        if exists is not True:
            self.the_machine.append(AddrVal(in_addr, in_value))
    
    def sum_all_values(self):
        out_sum = 0

        for entry in self.the_machine:
            out_sum += entry.the_value

        return out_sum
