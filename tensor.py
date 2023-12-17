from tkinter import Tk, Label, Entry, Button
class WhatsAppWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Automation")
        self.root.geometry("400x200")

        Label(root, text="WhatsApp Number:").pack()
        self.whatsapp_number_entry = Entry(root)
        self.whatsapp_number_entry.pack()

        Label(root, text="Message:").pack()
        self.message_entry = Entry(root)
        self.message_entry.pack()

        Label(root, text="Hour (0-23):").pack()
        self.hour_entry = Entry(root)
        self.hour_entry.pack()

        Label(root, text="Minute (0-59):").pack()
        self.minute_entry = Entry(root)
        self.minute_entry.pack()

        send_button = Button(root, text="Send WhatsApp Message", command=self.send_whatsapp_message)
        send_button.pack()

    def send_whatsapp_message(self):
        whatsapp_number = self.whatsapp_number_entry.get()
        message = self.message_entry.get()
        hour = int(self.hour_entry.get())
        minute = int(self.minute_entry.get())

        try:
            pywhatkit.sendwhatmsg(whatsapp_number, message, hour, minute)
            print("WhatsApp message sent successfully!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
