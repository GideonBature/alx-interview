#!/usr/bin/python3
"""Python Lockboxes
"""


def canUnlockAll(boxes):
    """Checks for every box
    args:
        boxes: List
    return:
        Boolean
    """
    open_boxes = [0]
    visited_boxes = {0}

    while open_boxes:
        current_box = open_boxes.pop(0)

        for key in boxes[current_box]:
            if key < len(boxes) and key not in visited_boxes:
                visited_boxes.add(key)
                open_boxes.append(key)

    return len(visited_boxes) == len(boxes)
