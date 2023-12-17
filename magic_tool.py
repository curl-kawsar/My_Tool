from tkinter import *
import cv2
from PIL import ImageTk
from PIL import Image
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import tkinter as tk
import screen_brightness_control as sbc
import pyautogui
import sys
import time
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk
import pandas as pd
import webbrowser
import pywhatkit as kit
import tkinter.simpledialog


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login With Your Account")
        self.root.geometry("320x250+600+250")
        self.root.configure(bg='#2E2E2E')

        title=Label(self.root,text="    SIGN IN",padx=10,compound=LEFT,font=("Goudy Old Style",40,"bold"),bg = "#222A35",fg="Yellow",anchor="w").place(x=0,y=0,relwidth=1)
        self.label_username = Label(root, text="Username:")
        self.label_password = Label(root, text="Password:")
        self.entry_username = Entry(root)
        self.entry_password = Entry(root, show="*")

        self.label_username.place(x=50,y=88)
        self.entry_username.place(x=120,y=90)
        self.label_password.place(x=50,y=120)
        self.entry_password.place(x=120,y=120)

        self.login_button = Button(root, text="Login", command=self.login)
        self.login_button.place(x=135,y=160)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Define admin credentials
        admin_username = "a"
        admin_password = "a"  # Change this to your admin password

        if username == admin_username and password == admin_password:
            tkinter.messagebox.showinfo("Login", "Login Successful!")
            self.root.destroy()  # Close the login window
            app = MagicTool()
            app.run()  # Open the main application window
        else:
            tkinter.messagebox.showerror("Login Error", "Invalid username or password")




class MagicTool:
    def set_background(self):
        background_image = Image.open('ai.jpg')
        background_photo = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(self.root, image=background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.image = background_photo

    
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tool By Kawsar")
        self.root.geometry("780x750+200+50")
        self.root.configure(bg='#2E2E2E')
        self.set_background()
        
        
        title=Label(self.root,text="   Magic Tools Version 1.1",padx=10,compound=LEFT,font=("Goudy Old Style",48,"bold"),bg = "#222A35",fg="Yellow",anchor="w").place(x=0,y=0,relwidth=1)
        dev=Label(self.root,text="Developed by Kawsar",font=("Times New Roman",30,"bold"),bg = "#222A35",fg="White",).place(x=0,y=80,relwidth=1)
        des=Label(self.root,text="You Must Have a Camera To use this Tool",font=("Calibri (Body)",14),bg = "#FFD966",fg="Black").place(x=0,y=131,relwidth=1)

        # Volume = Label(self.root, text="Control Your Volume",font=("times new roman",18),bg = "#007ACC",fg="White",relief=RAISED).place(x = 50,y=220)
        # Brightness = Label(self.root, text="Control Your Brightness",font=("times new roman",18),bg = "#F16334",fg="White",relief=RAISED).place(x = 50,y=355)
        # Screenshot = Label(self.root, text="Take a Screenshot",font=("times new roman",18),bg="#E67E22", fg="white",relief=RAISED).place(x = 50,y=480)



        button_width = 270
        button_height = 60

        self.button1 = tk.Button(self.root, font=('Arial', 24), activebackground="#007ACC", text="Volume Control", relief=RIDGE, cursor="hand2", bg="#007ACC", fg="Black", command=self.volume_control)
        self.button1.place(x=190, y=240, anchor=tk.CENTER, width=button_width, height=button_height)

        self.button2 = tk.Button(self.root, font=('Arial', 24), activebackground="#C71585", relief=RIDGE, cursor="hand2", text="Brightness Control", bg="#C71585", fg="white", command=self.brightness_control)
        self.button2.place(x=190, y=350, anchor=tk.CENTER, width=button_width, height=button_height)

        self.button3 = tk.Button(self.root, font=('Arial', 24), activebackground="#9400D3", relief=RIDGE, cursor="hand2", text="Screenshot", bg="#9400D3", fg="black", command=self.take_screenshot)
        self.button3.place(x=190, y=460, anchor=tk.CENTER, width=button_width, height=button_height)

        self.button4 = tk.Button(self.root, font=('Arial', 24), activebackground="#800000", relief=RIDGE, cursor="hand2", text="Mouse Control", bg="#800000", fg="white", command=self.mouse_control)
        self.button4.place(x=190, y=570, anchor=tk.CENTER, width=button_width, height=button_height)
        
        
        self.button5 = tk.Button(self.root, font=('Arial', 24), activebackground="#25D366", relief=RIDGE, cursor="hand2", text="WP Automation", bg="#25D366", fg="Black",command=self.whatsapp_automation)
        self.button5.place(x=585, y=240, anchor=tk.CENTER, width=button_width, height=button_height)

        self.button6 = tk.Button(self.root, font=('Arial', 24), activebackground="#C71585", relief=RIDGE, cursor="hand2", text="Virtual Mouse", bg="#C71585", fg="white")
        self.button6.place(x=585, y=350, anchor=tk.CENTER, width=button_width, height=button_height)

        self.button7 = tk.Button(self.root, font=('Arial', 24), activebackground="#9400D3", relief=RIDGE, cursor="hand2", text="Location Finder", bg="#9400D3", fg="black")
        self.button7.place(x=585, y=460, anchor=tk.CENTER, width=button_width, height=button_height)

        self.button8 = tk.Button(self.root, font=('Arial', 24), activebackground="#800000", relief=RIDGE, cursor="hand2", text="BruteForce", bg="#800000", fg="white")
        self.button8.place(x=585, y=570, anchor=tk.CENTER, width=button_width, height=button_height)
        
        
        # ========= Icons ========
        image = Image.open('gt.png')
        img = image.resize((70,70))
        self.email_icon = ImageTk.PhotoImage(img)
        
        image2 = Image.open('facebook.png')
        img2 = image2.resize((70,70))
        self.setting = ImageTk.PhotoImage(img2)
        
        
        
        title=Label(self.root,image=self.email_icon,padx=10,compound=LEFT,font=("Goudy Old Style",30,"bold"),fg="white",anchor="w").place(x=10,y=670)
        github = Button(self.root,text="GITHUB",font=("times new roman",20,"bold"),bg="#00B0F0",activebackground="#00B0F0",fg="black",cursor="hand2",command=self.github_window).place(x=100,y=685)
        
        
        title=Label(self.root,image=self.setting,padx=10,compound=LEFT,font=("Goudy Old Style",30,"bold"),fg="white",anchor="w").place(x=497,y=670)
        github = Button(self.root,text="FACEBOOK",font=("times new roman",20,"bold"),bg="#00B0F0",activebackground="#00B0F0",fg="black",cursor="hand2",command=self.facebook_window).place(x=590,y=685)
    
    
    #----- Github----------
    def github_window(self):
        github_link = "https://github.com/curl-kawsar"
        webbrowser.open_new(github_link)     
    #----- Facebook ------
    def facebook_window(self):
        facebook_link = "https://facebook.com/python.kawsar"
        webbrowser.open_new(facebook_link)  
    #------------------------------------
    def run(self):
        self.root.mainloop()

    def volume_control(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            tkinter.messagebox.showerror("Camera Error", "Failed to open the camera.")
            return

        mpHands = mp.solutions.hands
        hands = mpHands.Hands()
        mpDraw = mp.solutions.drawing_utils

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        volMin, volMax = volume.GetVolumeRange()[:2]

        while True:
            ret, img = cap.read()

            if not ret:
                tkinter.messagebox.showerror("Camera Error", "Failed to grab a frame.")
                break

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)

            lmList = []
            if results.multi_hand_landmarks:
                for handlandmark in results.multi_hand_landmarks:
                    for id, lm in enumerate(handlandmark.landmark):
                        h, w, _ = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                    mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

            if lmList != []:
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]

                cv2.circle(img, (x1, y1), 4, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 4, (255, 0, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

                length = hypot(x2 - x1, y2 - y1)

                vol = np.interp(length, [15, 220], [volMin, volMax])
                print(vol, length)
                volume.SetMasterVolumeLevel(vol, None)

            cv2.imshow('Volume Control', img)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def brightness_control(self):
        cap = cv2.VideoCapture(0)

        mpHands = mp.solutions.hands
        hands = mpHands.Hands()
        mpDraw = mp.solutions.drawing_utils

        while True:
            success, img = cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)

            lmList = []
            if results.multi_hand_landmarks:
                for handlandmark in results.multi_hand_landmarks:
                    for id, lm in enumerate(handlandmark.landmark):
                        h, w, _ = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                    mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

            if lmList != []:
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]

                cv2.circle(img, (x1, y1), 4, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 4, (255, 0, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

                length = hypot(x2 - x1, y2 - y1)

                bright = np.interp(length, [15, 220], [0, 100])
                print(bright, length)
                sbc.set_brightness(int(bright))

            cv2.imshow('Brightness Control', img)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                break

    def take_screenshot(self):
        self.root.destroy()
        print("Taking a screenshot...\n")
        time.sleep(1)
        myScreenshot = pyautogui.screenshot()
        file_name = asksaveasfilename(confirmoverwrite=False, defaultextension='.png')
        myScreenshot.save(file_name)
        sys.exit(0)
        
        
        
        
    def whatsapp_automation(self):
        root = tk.Tk()
        root.geometry("400x250")
        root.title("WhatsApp Automation")

        notice_label = tk.Label(root, text="Enter time in 24-hour format and Number With Country Code", font=("Arial", 10, "italic"), fg="blue")
        notice_label.pack(pady=5)

        
        phone_number_label = tk.Label(root, text="WP number:", font=("Arial", 10, "bold"), bg="#FFD700")
        phone_number_label.place(x= 40,y = 50)

        message_label = tk.Label(root, text="Your message:", font=("Arial", 10, "bold"), bg="#00FF00")
        message_label.place(x = 40,y= 100)

        time_label = tk.Label(root, text="Time (HH:MM):", font=("Arial", 10, "bold"), bg="#FF5733")
        time_label.place(x = 40,y= 150)

        
        phone_number = tk.Entry(root, bg="#FFFF99")
        phone_number.place(x= 180,y = 50)

        message = tk.Entry(root, bg="#99FF99")
        message.place(x= 180,y = 100)

        time_str = tk.Entry(root, bg="#FFCCCB")
        time_str.place(x= 180,y = 150)

        
        ok_button = tk.Button(root, text="Send Message", command=lambda: self.send_whatsapp_message(root, phone_number.get(), message.get(), time_str.get()), bg="#007ACC", fg="white", font=("Arial", 12))
        ok_button.place(x= 150,y = 190)
        
        
        self.success_label = tk.Label(root, text="", font=("Arial", 10, "bold"), fg="green")
        self.success_label.pack(pady=5)

        root.mainloop()

    def send_whatsapp_message(self, root, phone_number, message, time_str):
        root.destroy()
        if phone_number and message and time_str:
            try:
                time_parts = time_str.split(":")
                if len(time_parts) == 2:
                    hours, minutes = map(int, time_parts)
                    kit.sendwhatmsg(phone_number, message, hours, minutes)
                    print("WhatsApp message sent successfully!")
                else:
                    print("Invalid time format. Please use HH:MM format.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        else:
            print("Input fields cannot be empty.")


    def run(self):
        self.root.mainloop()
        
        
        
    def mouse_control(self):
        # Initialize MediaPipe Hands module
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()

        # Constants for screen resolution (adjust as needed)
        SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

        # Create a function to move the mouse cursor
        def move_mouse(x, y):
            mapped_x = int(x * SCREEN_WIDTH)
            mapped_y = int(y * SCREEN_HEIGHT)
            pyautogui.moveTo(mapped_x, mapped_y)

        # Open the webcam
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                continue

            # Flip the frame horizontally for natural movement (optional)
            frame = cv2.flip(frame, 1)

            # Convert the BGR image to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame to detect hands
            results = hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Get the landmarks for the hand
                    index_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                    # Get the x and y coordinates of the index finger tip
                    x, y = index_finger_landmark.x, index_finger_landmark.y

                    # Move the mouse cursor based on finger position
                    move_mouse(x, y)

            # Display the frame
            cv2.imshow('Hand Gesture Mouse Control', frame)

            # Exit the loop when 'q' is pressed
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        # Release the camera and close all windows
        cap.release()
        cv2.destroyAllWindows()
        
    
    
    

if __name__ == "__main__":
    root = Tk()
    login_window = LoginWindow(root)
    root.mainloop()