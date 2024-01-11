#!/usr/bin/python3
'''
This module houses a function that solves a lockboxes puzzle.
'''


def canUnlockAll(boxes):
    '''
    The functions return true or false is all the boxes can be opened or not.
    '''

    unlocked_boxes = [0]

    if len(boxes) > 1:
        for box in unlocked_boxes:
            for key in boxes[box]:
                if key not in unlocked_boxes and key < len(boxes):
                    unlocked_boxes.append(key)

        return len(unlocked_boxes) == len(boxes)
    return True
