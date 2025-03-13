from utils import find_image_on_screen, click_on_image
import time
if __name__ == "__main__":
    
    print(f"Starting screen analysis... Looking for image")
    print("Press Ctrl+C to stop the script")
    
    try:
        while True:
            if find_image_on_screen("./images/icon.png", confidence=0.8):
                # logging out if there is a logout button in the screen while facebook is open
                if(find_image_on_screen("./images/logoutIcon.png")):
                    # clicking on logout icon
                    click_on_image("./images/logoutIcon.png")
                print("Image found - Cursor moved to location")
                # clicking on account icon to get the logout icon
                click_on_image("./images/accountIcon.png")
            # looking if I am seeing youtube short
            if find_image_on_screen("./images/youtubeShort.png"):
                click_on_image("./images/youtube.png")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nScript stopped by user")