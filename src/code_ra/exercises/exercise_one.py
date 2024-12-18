from code_ra.utils.functions import *

def check_answer_one():

    exp_funcs = ["print", "print"]

    for exp in exp_funcs:
        trace = func_calls.get()

        if (trace is None) or (trace.name is not exp):
            print_fail(f"Did you call {exp}? Try again.")
            break

        print_ok(f"Found {exp}.")
    
    print_ok(f"Task Complete. Great job!")