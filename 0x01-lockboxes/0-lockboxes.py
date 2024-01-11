#!/usr/bin/python3

"""
- Write a method that determines if all the boxes can be opened.
- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- Assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened. """
    opened_boxes = [0]
    for key in opened_boxes:
        for box in boxes[key]:
            if box not in opened_boxes and box < len(boxes):
                opened_boxes.append(box)
    if len(opened_boxes) == len(boxes):
        return True
    return False
