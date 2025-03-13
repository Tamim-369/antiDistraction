import pyautogui
import cv2
import numpy as np
import time

def find_image_on_screen(image_path, confidence=0.8):
    """
    Search for an image on the screen once. If found, move cursor to it and return True.
    
    Parameters:
    image_path (str): Path to the template image to search for
    confidence (float): Matching confidence threshold (0.0-1.0), default 0.8
    
    Returns:
    bool: True if image is found and cursor moved, False if not found
    """
    try:
        # Load the template image
        template = cv2.imread(image_path)
        if template is None:
            raise FileNotFoundError(f"Could not load image at {image_path}")
        
        template_height, template_width = template.shape[:2]
        
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        # Convert PIL image to OpenCV format (RGB -> BGR)
        screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Perform template matching
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        # Check if the match exceeds the confidence threshold
        if max_val >= confidence:
            # Calculate center position of the matched area
            center_x = max_loc[0] + template_width // 2
            center_y = max_loc[1] + template_height // 2
            return True
        return False
    
    except Exception as e:
        print(f"Error in find_image_on_screen: {str(e)}")
        return False
    


def click_on_image(image_path, confidence=0.8):
    """
    Search for an image on the screen once. If found, move cursor to it and return True.
    
    Parameters:
    image_path (str): Path to the template image to search for
    confidence (float): Matching confidence threshold (0.0-1.0), default 0.8
    
    Returns:
    bool: True if image is found and cursor moved, False if not found
    """
    try:
        # Load the template image
        template = cv2.imread(image_path)
        if template is None:
            raise FileNotFoundError(f"Could not load image at {image_path}")
        
        template_height, template_width = template.shape[:2]
        
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        # Convert PIL image to OpenCV format (RGB -> BGR)
        screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Perform template matching
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        # Check if the match exceeds the confidence threshold
        if max_val >= confidence:
            # Calculate center position of the matched area
            center_x = max_loc[0] + template_width // 2
            center_y = max_loc[1] + template_height // 2
            # Move cursor to the center of the found image
            pyautogui.moveTo(center_x, center_y)
            pyautogui.click()
            return True
        return False
    
    except Exception as e:
        print(f"Error in find_image_on_screen: {str(e)}")
        return False
    