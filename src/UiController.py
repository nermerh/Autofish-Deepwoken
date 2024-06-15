from tkinter import *
from pynput import keyboard

class Ui():

    def __init__(self):
        pass

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
    