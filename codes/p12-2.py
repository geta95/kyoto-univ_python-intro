import tkinter as tk
import tkinter.filedialog
import math

root = tk.Tk()
root.withdraw()
filename = tkinter.filedialog.asksaveasfilename()
root.destroy()

if filename:
    pass
else:
    print("No file specified")
    exit()

cycles = 2
steps = 1000
harmonics = 5
try:
    with open(filename, 'w') as file:
        for i in range(steps):
            angle_in_degree = 360*cycles*i/steps
            angle = math.radians(angle_in_degree)
            s = str(angle_in_degree)
            w = 0
            for j in range(1, harmonics+1):
                w += math.sin(angle*j)/j
                s = s + ", " + str(w)
            print(s)
            file.write(s+"\n")
        print("Writing to file " + filename + " is finished")
except IOError:
    print("Unable to open file")
