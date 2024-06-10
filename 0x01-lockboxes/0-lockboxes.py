#!/usr/bin/python3
'''A module for working with lockboxes.
Start with the first box (box 0).
Use a queue to keep track of boxes to be checked for keys.
Keep a set of opened boxes.
For each box, add its keys to the queue
if the corresponding box hasn't been opened yet.
'''


def canUnlockAll(boxes):
    '''
    Checks if all the boxes in a list of boxes containing the keys
    '''
    if not boxes:
        return False

    n = len(boxes)
    opened = set()
    to_open = [0]  # Start with the first box

    while to_open:
        current_box = to_open.pop()
        if current_box not in opened:
            opened.add(current_box)
            # Add keys found in the current box to the list of boxes to open
            for key in boxes[current_box]:
                if key < n and key not in opened:
                    to_open.append(key)

    # will return true if set equels to n
    return len(opened) == n
