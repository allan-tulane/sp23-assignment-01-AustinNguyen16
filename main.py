"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
        return x
    else:
        a = foo(x-1)
        b = foo(x-2)
        return a + b

def longest_run(mylist, key):
    ### TODO
    current = 0
    highest = 0
    for num in mylist:
        if num == key:
            current += 1
            if current >= highest:
                highest = current
            elif num != key:
                current = 0
        return highest


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    def longest_run_recursive(mylist, key):
    if len(mylist) == 0:
        return 0
    elif len(mylist) == 1:
        if mylist[0] == key:
            return 1
        else:
            return 0
    else:
        mid = len(mylist) // 2
        left = longest_run_recursive(mylist[:mid],key)
        right = longest_run_recursive(mylist[mid:],key)
        left_val = 0
        right_val = 0
        for i in range(mid-1, -1, -1):
            if mylist[i] == key:
                left_val += 1
            else:
                break
        for i in range(mid, len(mylist)):
            if mylist[i] == key:
                right_val += 1
            else:
                break
        total_val = left_val + right_val
        return max(left, right, total_val)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


