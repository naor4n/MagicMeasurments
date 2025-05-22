import tkinter as tk


class Conversions:
    def __init__(self):
        pass

    def convert(self, input_text):
        pass

    def scale(self, input_text):
        pass


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x900')
        self.root.title("Magic Measurements")

        self.conversions = Conversions()

        self.label = tk.Label(root, text="Start baking!", font=("Arial", 18), padx=20, pady=20)
        self.label.pack(pady=20)

        self.textbox = tk.Text(root, height=15, font=("Arial", 12))
        self.textbox.pack()

        self.buttonframe = tk.Frame(root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        convert_button = tk.Button(self.buttonframe, text="Convert", font=("Arial", 12), padx=20, pady=20, command=self.conversions.convert(self.textbox.get("1.0", tk.END)))
        convert_button.grid(row=0, column=0, sticky="ew")

        scale_button = tk.Button(self.buttonframe, text="Scale", font=("Arial", 12), padx=20, pady=20, command=self.conversions.scale(self.textbox.get("1.0", tk.END)))
        scale_button.grid(row=0, column=1, sticky="ew")

        self.buttonframe.pack(pady=20)


def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()



