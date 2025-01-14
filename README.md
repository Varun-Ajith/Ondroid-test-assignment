# LED Detection Project - Ondroid Test Assignment

This project implements an LED detection system using an ESP32 controller board connected to a 10-segment digital LED strip. The system consists of two main components:
- C++ code running on the ESP32 to control the LED segments
- Python code using OpenCV to detect and count lit LED segments through video feed

## Hardware Setup

### Components
- ESP32 Controller Board
- 10-segment Digital LED Strip

### Pin Configuration
| ESP32 Pin | LED Segment |
|-----------|-------------|
| 27 | 1 |
| 25 | 2 |
| 33 | 3 |
| 21 | 4 |
| 26 | 5 |
| 23 | 6 |
| 22 | 7 |
| 12 | 8 |
| 19 | 9 |
| 13 | 10 |

## Code Implementation

### C++ (ESP32) Code
The C++ code controls the LED strip by:
1. Initializing all pins as outputs in `setup()`
2. Sequentially lighting up each LED in `loop()`
3. Creating a "moving light" effect with 200ms delay between transitions

```cpp
const uint8_t l = 10;
uint8_t pins[l] = {
    27,//1
    25,//2
    33,//3
    21,//4
    26,//5
    23,//6
    22,//7
    12,//8
    19,//9
    13 //10
};
```

### Python (OpenCV) Code
The Python code analyzes the video feed to count lit LEDs:
1. Defines Region of Interest (ROI) for the LED strip
2. Converts image to grayscale
3. Applies threshold to detect bright spots
4. Uses contour detection to count lit LEDs
5. Provides real-time LED count updates

Key features:
- ROI coordinates: `[400:500, 0:400]`
- Threshold value: 200
- 10-second verification period
- Error handling for invalid images
- Visual debugging with rectangle overlay

## Output Format
The system provides real-time updates in the format:
```
Number of LEDs lit: X
```
Where X represents the count of currently lit LEDs (typically 0, 1, or occasionally 2 during transitions).

## Dependencies
- C++: Arduino IDE for ESP32
- Python: OpenCV (cv2), NumPy
- Hardware: ESP32 board, 10-segment LED strip

## Testing
The code has been tested with:
- Sequential LED lighting pattern
- Real-time video feed processing
- Various lighting conditions
- Error handling scenarios

The system successfully:
- Detects when no LEDs are lit (0)
- Tracks single lit LEDs (1)
- Catches brief transitions between LEDs (2)
- Completes verification after 10 seconds

## Contributing
This project is part of the Ondroid test assignment. For modifications or improvements, please create a pull request with:
1. Clear description of changes
2. Test results
3. Any updates to documentation

