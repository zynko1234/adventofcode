import sys

def solve(in_list):
    sys.setrecursionlimit(pow(2, 11))    
    digest_list = digest_input(in_list)

    ansA = count_jolt(digest_list)
    
    ansB = calculate_perms(digest_list)

    return ansA, ansB

def digest_input(in_list):
    out_list = []
    out_list.append(0)

    for entity in in_list:
        out_list.append(int(entity))
    
    out_list.append(max(out_list) + 3)
    return sorted(out_list)

def count_jolt(in_list):    
    in_list
    last_element = (len(in_list) - 1)
    one_jolts = 0
    three_jolts = 0

    # Calculate jolt diff betwen all successive adapters.
    for i in range(len(in_list)):
        if i is not last_element:
            diff = abs(in_list[i] - in_list[i+1])
            if diff == 1:
                one_jolts += 1
            elif diff == 3:
                three_jolts += 1

    return three_jolts * one_jolts

def calculate_perms(in_list):
    tree_root = AdaptTree(0)

    for i in range(len(in_list)):
        tree_root.insert(in_list[i])
    
    total_count = tree_root.count_leaves(max(in_list))
    
    return total_count


class AdaptTree(object):

    def __init__(self, in_value):
        self.branches = []
        self.value = in_value
        return
    
    def insert(self, in_value):
        if self.value is not None:
            diff = abs(self.value - in_value)
            greater = (self.value < in_value)

            if greater and ((diff < 4) and (diff > 0)):
                tmp = AdaptTree(in_value)
                self.branches.append(tmp)
                for curr_branch in self.branches:
                    curr_branch.insert(in_value)
            else:
                for curr_branch in self.branches:
                    curr_branch.insert(in_value)
                self.prune()
        return
                
    def prune(self):
        rem_list = []
        for i in range(len(self.branches)):
            if self.branches[i].shallow_branch_count() == 0:
                rem_list.append(self.branches[i])
            
        for cut_tree in rem_list:
            self.branches.remove(cut_tree)
        return

    def count_leaves(self, term_value, counter = 0):
        copy_counter = counter

        if self.value == term_value:
            copy_counter += 1
        else:
            for entity in self.branches:
                copy_counter = entity.count_leaves(term_value, copy_counter)
        return copy_counter

    def shallow_branch_count(self):
        return len(self.branches)

