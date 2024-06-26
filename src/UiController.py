import tkinter
import multiprocessing
import asyncio
from pynput import keyboard
from AutofishProcessController import autofish_process

class Ui(tkinter.Tk):
    # Creating the gui on object init
    def __init__(self):
        super().__init__()

        self.enabled = False
        self.processStarted = False
        self.keyPressed = False
        self.keybind = "z"

        # configure window
        self.title("Autofish Deepwoken")
        self.iconbitmap("Assets\Images\RawFish.ico")
       # self.geometry(f"{400}x{450}")

        self.main_frame = tkinter.Frame(self, width=400)
        #self.main_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.main_frame.pack()

        self.title_label = tkinter.Label(self.main_frame, text="Autofish made by nermer", fg="deep sky blue", font=("Helvetica", 20, "bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(30, 5))

        # Choosing bait
        self.bait_frame = tkinter.LabelFrame(self.main_frame, text="Bait")
        self.bait_frame.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="nsew")
        self.bait_radio_var = tkinter.IntVar(value=0)

        self.bait_radio_1 = tkinter.Radiobutton(master=self.bait_frame, text="None", variable=self.bait_radio_var, value=0)
        self.bait_radio_1.grid(row=0, column=2, padx=20, pady=(10, 0), sticky="w")

        self.bait_radio_2 = tkinter.Radiobutton(master=self.bait_frame, text="Chum", variable=self.bait_radio_var, value=1)
        self.bait_radio_2.grid(row=1, column=2, padx=20, pady=(0, 10), sticky="w")

        # Chest Alert
        self.chest_frame = tkinter.LabelFrame(self.main_frame, text="Chest Alert")
        self.chest_frame.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")
        self.chest_check_var = tkinter.BooleanVar(value=True)
        
        self.chest_checkbox = tkinter.Checkbutton(self.chest_frame, text="Make sound for chest?", variable=self.chest_check_var, onvalue=True, offvalue=False)
        self.chest_checkbox.grid(row=0, column=2, padx=20, pady=10, sticky="n")

        # Fishing Hotbar Selection
        self.rod_hotbar_frame = tkinter.LabelFrame(self.main_frame, text="Select Fishing Rod Slot")
        self.rod_hotbar_frame.grid(row=3, column=0, padx=20, pady=5, sticky="nsew")
        
        self.rod_spinner = tkinter.Spinbox(self.rod_hotbar_frame, from_=0, to_=9, wrap=True, state="readonly")
        self.rod_spinner.grid(row=0, column=0, padx=20, pady=10, sticky="n")

        # Activation
        self.activation_frame = tkinter.LabelFrame(self.main_frame, text="Activation")
        self.activation_frame.grid(row=4, column=0, padx=20, pady=(5, 30), sticky="nsew")

        self.keybind_button = tkinter.Button(self.activation_frame, text="Keybind: Z")
        self.keybind_button.grid(row=0, column=0, padx=(20,0), pady=10, sticky="nsew")
        
        self.keybind_label = tkinter.Label(self.activation_frame, text="(Click to change Keybind)")
        self.keybind_label.grid(row=0, column=1, padx=(20, 0), pady=10, sticky="nsew")

        self.enable_button = tkinter.Button(self.activation_frame, text="Enable!", command=self.toggle_enabled_event ,bg="RoyalBlue1", fg="snow")
        self.enable_button.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.enable_status_label = tkinter.Label(self.activation_frame, text="DISABLED", fg="red2", font=("Arial", 12, "bold"))
        self.enable_status_label.grid(row=1, column=1, padx=(20, 0), pady=10, sticky="nsew")

        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

        self.process_parallel = multiprocessing.Process(target=autofish_process, daemon=True)

    # Keyboard events
    def on_press(self, key):
        if not self.enabled or self.keyPressed: return
        if not key == keyboard.Key.enter: return
        self.keyPressed = True

        if self.processStarted:
            self.terminate_process()
        else:
            self.processStarted = True
            self.process_parallel = multiprocessing.Process(target=autofish_process, daemon=True, kwargs= {
                "bait" : self.bait_radio_var.get(), # int
                "chest_sound" : self.chest_check_var.get(), # bool
                "rod_slot" : self.rod_spinner.get() # str
            })
            self.process_parallel.start()

    def on_release(self, key):
        self.keyPressed = False
    
    # Gui button events
    def toggle_enabled_event(self):
        if self.enabled:
            self.enabled = False
            if self.processStarted: self.terminate_process()
            # enable input guis
            self.keybind_button.config(state="normal")
            self.rod_spinner.config(state="normal")
            self.chest_checkbox.config(state="normal")
            self.bait_radio_1.config(state="normal")
            self.bait_radio_2.config(state="normal")

            self.enable_status_label.config(text="DISABLED", fg="red2")
            self.enable_button.config(text="Enable!")
        else:
            self.enabled = True
            # disable input guis
            self.keybind_button.config(state="disabled")
            self.rod_spinner.config(state="disabled")
            self.chest_checkbox.config(state="disabled")
            self.bait_radio_1.config(state="disabled")
            self.bait_radio_2.config(state="disabled")

            self.enable_status_label.config(text="ENABLED", fg="green2")
            self.enable_button.config(text="Disable!")

    def terminate_process(self):
        self.processStarted = False
        self.process_parallel.terminate()
        self.process_parallel.join()