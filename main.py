from utils.gui import App
from utils.hash import calc_hash

def control():
    filename = app.get_filename()
    hash_correct = app.input_hash_correct.get()

    file_hash = calc_hash(filename)

    if(file_hash == hash_correct):
        print("Uguale")
    else:
        print("Diversi")

# ------------ Main --------------
if __name__ == "__main__":
    
    app = App()

    app.submit_control.configure(command=control)
    
    app.mainloop()