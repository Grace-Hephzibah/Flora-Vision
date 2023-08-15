import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ImageViewerApp:
    def __init__(self, root, image_dir):
        self.root = root
        self.root.title("Image Viewer App")
        
        self.image_dir = image_dir
        self.image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]
        self.current_image_index = 0
        
        self.image_label = tk.Label(root)
        self.image_label.pack()
        
        self.load_image(self.current_image_index)
        
        self.root.bind('<Return>', self.show_next_image)
        self.root.bind('<Shift_L>', self.mark_outlier)
    
    def load_image(self, index):
        if 0 <= index < len(self.image_paths):
            image_path = self.image_paths[index]
            image = Image.open(image_path)
            image = image.resize((400, 300), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        else:
            messagebox.showinfo("End of Images", "No more images to display.")
            self.root.quit()
    
    def show_next_image(self, event):
        self.current_image_index += 1
        self.load_image(self.current_image_index)
    
    def mark_outlier(self, event):
        if 0 <= self.current_image_index < len(self.image_paths):
            current_image_name = os.path.basename(self.image_paths[self.current_image_index])
            with open("outliers.txt", "a") as f:
                f.write(self.image_dir + "/" + current_image_name + "\n")
            self.current_image_index += 1
            self.load_image(self.current_image_index)

if __name__ == "__main__":
    root = tk.Tk()
    
    parent_dir = ['test/'] #, 'train/', 'valid/']
    classes = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
    list_dir = []
    for par in parent_dir:
        for class_val in classes:
            list_dir.append(par + class_val)

    print(list_dir)

    app = ImageViewerApp(root, list_dir[0])

    for index, image_dir in enumerate(list_dir[1:]):
        root.mainloop()
        print("Task : ", index+1, " ", image_dir, "Done!")
    
    print("Success!")