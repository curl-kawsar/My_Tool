    def whatsapp_automation(self):
        # Create a colorful and attractive input dialog
        root = tk.Tk()
        root.geometry("400x250")  # Adjust the size as needed
        root.title("WhatsApp Automation Input")

        # Create a notice label with a different color and font
        notice_label = tk.Label(root, text="Enter time in 24-hour format and Number With Country Code", font=("Arial", 10, "italic"), fg="blue")
        notice_label.pack(pady=5)

        # Create labels with colorful backgrounds and different fonts
        phone_number_label = tk.Label(root, text="Recipient's phone number:", font=("Arial", 10, "bold"), bg="#FFD700")
        phone_number_label.place(x= 200,y = 150)

        message_label = tk.Label(root, text="Your message:", font=("Arial", 10, "bold"), bg="#00FF00")
        message_label.pack(pady=5)

        time_label = tk.Label(root, text="Time (HH:MM):", font=("Arial", 10, "bold"), bg="#FF5733")
        time_label.pack(pady=5)

        # Create entry fields with colorful backgrounds
        phone_number = tk.Entry(root, bg="#FFFF99")
        phone_number.pack(pady=5)

        message = tk.Entry(root, bg="#99FF99")
        message.pack(pady=5)

        time_str = tk.Entry(root, bg="#FFCCCB")
        time_str.pack(pady=5)

        # Create a colorful and styled OK button
        ok_button = tk.Button(root, text="OK", command=lambda: self.send_whatsapp_message(root, phone_number.get(), message.get(), time_str.get()), bg="#007ACC", fg="white", font=("Arial", 12))
        ok_button.pack(pady=10)

        root.mainloop()

    def send_whatsapp_message(self, root, phone_number, message, time_str):
        root.destroy()
        if phone_number and message and time_str:
            try:
                # Convert time_str to hours and minutes
                time_parts = time_str.split(":")
                if len(time_parts) == 2:
                    hours, minutes = map(int, time_parts)
                    kit.sendwhatmsg(phone_number, message, hours, minutes)  # Send the WhatsApp message
                    print("WhatsApp message sent successfully!")
                else:
                    print("Invalid time format. Please use HH:MM format.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        else:
            print("Input fields cannot be empty.")

