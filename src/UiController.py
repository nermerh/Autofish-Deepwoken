import tkinter

class Ui(tkinter.Tk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Autofish Deepwoken")
        self.iconbitmap("Assets\Images\RawFish.ico")
        self.geometry(f"{400}x{400}")

        self.main_frame = tkinter.Frame(self, width=140)
        self.main_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.title_label = tkinter.Label(self.main_frame, text="Autofish made by nermer", fg="deep sky blue", font=("Helvetica", 20, "bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Choosing bait
        self.bait_frame = tkinter.LabelFrame(self.main_frame, text="Bait")
        self.bait_frame.grid(row=1, column=0, padx=20, pady=(20, 5), sticky="nsew")
        self.bait_radio_var = tkinter.IntVar(value=0)

        self.bait_radio_1 = tkinter.Radiobutton(master=self.bait_frame, text="None", variable=self.bait_radio_var, value=0)
        self.bait_radio_1.grid(row=0, column=2, padx=20, pady=10, sticky="n")

        self.bait_radio_2 = tkinter.Radiobutton(master=self.bait_frame, text="Chum", variable=self.bait_radio_var, value=1)
        self.bait_radio_2.grid(row=1, column=2, padx=20, pady=10, sticky="n")

        # Chest Alert
        self.chest_frame = tkinter.LabelFrame(self.main_frame, text="Chest Alert")
        self.chest_frame.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")
        self.chest_check_var = tkinter.BooleanVar(value=True)
        
        self.chest_checkbox = tkinter.Checkbutton(self.chest_frame, text="Make sound for chest?", variable=self.chest_check_var, onvalue=True, offvalue=False)
        self.chest_checkbox.grid(row=0, column=2, padx=20, pady=10, sticky="n")

        # Fishing Hotbar Selection
        self.rod_hotbar_frame = tkinter.LabelFrame(self.main_frame, text="Select Fishing Rod Slot")

    # Proccess

    # Initially create guis elements
    def _initialize(self):
        r = 0

        root = self.root
        root.title("Autofish Deepwoken")
        root.iconbitmap("Assets\Images\RawFish.ico")
        root.resizable(0, 0)

        titleLabel = Label(root, text="Autofish made by nermer", fg="deep sky blue", font=("Helvetica", 12, "bold"))
        titleLabel.pack(padx=10, pady=(15, 0))

        mainFrame = Frame(root)
        mainFrame.pack(padx=10, pady=10)

        baitFrame = LabelFrame(mainFrame, text="Bait", padx=5, pady=5)
        r+=1
        baitFrame.grid(row=0, column=0, sticky="nsew", pady=5)

        self._makeBaitButtons(baitFrame)

        chestFrame = LabelFrame(mainFrame, text="Chest Alert")
        r+=1
        chestFrame.grid(row=1, column=0, sticky="nsew", pady=5)

        self._makeChestButtons(chestFrame)

        rodFrame = LabelFrame(mainFrame, text="Rod Hotbar Slot", padx=5, pady=5)
        r+=1
        rodFrame.grid(row=2, column=0, sticky="nsew", pady=5)

        self._makeFishingRodHotbarButton(rodFrame)

        activationFrame = LabelFrame(mainFrame, text="Activation", padx=5, pady=5)
        r+=1
        activationFrame.grid(row=3, column=0, sticky="nsew", pady=5)

        self._makeActivationButtons(activationFrame)

    # Set Up Frames
    def _makeBaitButtons(self, baitFrame):
        baitR1 = Radiobutton(baitFrame, text="None", variable=self.baitVal, value=1)
        baitR1.grid(row=0, column=0, padx=5, pady=5, sticky="snsew")
        baitR1.select()

        baitR2 = Radiobutton(baitFrame, text="Chum", variable=self.baitVal, value=2)
        baitR2.grid(row=1, column=0, padx=5, pady=5, sticky="snsew")

    def _makeChestButtons(self, chestFrame):
        checkBox = Checkbutton(chestFrame, text="Make sound for chest?", variable=self.chestSoundVal, onvalue=True, offvalue=False)
        checkBox.grid(row=0, column=0, padx=5, pady=5, sticky="snsew")

    def _makeFishingRodHotbarButton(self, rodFrame):
        rodButton = Spinbox(rodFrame, from_=0, to_=9, wrap=True, state="readonly")
        rodButton.grid(row=0, column=0, padx=5, pady=5, sticky="snsew")
        self.RodSpinbox = rodButton

    def _makeActivationButtons(self, activationFrame):
        keybindButton = Button(activationFrame, text="Keybind: Z")
        keybindButton.grid(row=0, column=0, padx=5, pady=5, sticky="snsew")

        enableButton = Button(activationFrame, text="Enable", command=self.OnEnabledButtonPressed)
        enableButton.grid(row=1, column=0, padx=5, pady=5, sticky="snsew")
        self.enabledButton = enableButton

        statusLabel = Label(activationFrame, text="Disabled", fg="red", font=("Arial", 12, "bold"))
        statusLabel.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.statusLabel = statusLabel
    