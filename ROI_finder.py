import cv2
import numpy as np
import time


def task_test(robot, image, td: DataTest):
    """
    Annotate the image with coordinate markers at regular intervals.

    Args:
        robot: The robot object.
        image: The input image to annotate.
        td (DataTest): An instance of DataTest containing test data.

    Returns:
        Tuple containing updated DataTest, text description, and Result.
    """
    if td.end_time is None:
        td.end_time = time.time() + 10

    height, width = image.shape[:2]

    for x in range(0, width, 100):
        for y in range(0, height, 100):
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
            cv2.putText(
                image,
                f'({x},{y})',
                (x + 5, y + 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.3,
                (255, 255, 255),
                1
            )

    text = f"Image size: {width}x{height}"
    return td, text, Result(True, "Finding coordinates")
