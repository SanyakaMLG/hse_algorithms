from stack_vs_queue.my_stack import Stack

def is_valid_seq(pushed: list, popped: list) -> bool:
    s = Stack()
    push_index = 0
    
    for popped_el in popped:
        while s.empty() or s.peek() != popped_el:
            if push_index == len(pushed):
                return False
            s.push(pushed[push_index])
            push_index += 1

        s.pop()

    return push_index == len(pushed)
        