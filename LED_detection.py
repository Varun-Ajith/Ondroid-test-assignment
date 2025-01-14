import cv2
import numpy as np
import time


def task_test(robot, image, td: DataTest):
    """
    Test to count lit LEDs.

    Args:
        robot: The robot object.
        image: The input image to process.
        td (DataTest): An instance of DataTest containing test data.

    Returns:
        Tuple containing updated DataTest, text description, and Result.
    """
    try:
        if td.end_time is None:
            td.end_time = time.time() + 10

        if len(image.shape) == 3:
            roi = image[400:500, 0:400]

            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 200, 255, 0)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )

            led_count = len(contours)

            cv2.rectangle(image, (0, 400), (400, 500), (0, 255, 0), 2)

            text = f"Number of LEDs lit: {led_count}"
            desc = f"Detected {led_count} lit LEDs"
            success = True
        else:
            text = "Invalid image format"
            desc = "Could not process image"
            success = False

    except Exception as e:
        text = f"Error: {str(e)}"
        desc = "Error in LED detection"
        success = False

    return td, text, Result(success, desc)
