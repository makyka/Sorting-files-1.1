from tkinter import *
from tkinter import filedialog, messagebox
import shutil
import os

def move_files():
    directory = filedialog.askdirectory(title='Open a folder')  # Specify the directory where the files are located
    if directory:
            # Создание новой папки в папке назначения
            new_folder_path = os.path.join(directory, "New Folder")
            os.mkdir(new_folder_path)
    if directory:
        # Get the list of files in the directory
        files = os.listdir(directory)
        destination_folder = filedialog.askdirectory(title='Select a folder')

        # Prompt the user to enter a step value
        step = int(step_entry.get())

        if destination_folder:
            for index in range(0, len(files), step):
                # Using slices to get a sublist of files
                files_to_move = files[0: :+step]

                for file in files_to_move:
                    # Get the full path of the file
                    file_path = os.path.join(directory, file)
                    # Get the new path for the file in the destination folder
                    new_file_path = os.path.join(new_folder_path, file)

                    # Check if the destination file already exists
                    if os.path.exists(new_file_path):
                        # Rename the file by appending "(1)", "(2)", etc. to the filename
                        base_name, extension = os.path.splitext(file)
                        new_base_name = base_name
                        counter = 1
                        while os.path.exists(os.path.join(new_folder_path, new_base_name + extension)):
                            new_base_name = base_name + f"({counter})"
                            counter += 1

                        # Update the new file path with the new filename
                        new_file_path = os.path.join(new_folder_path, new_base_name + extension)
                    # Move the file to the destination folder
                    shutil.move(file_path, new_folder_path)

                    # Display a notification
                    field.insert(1.0, "Files were successfully moved to the new folder!")

root = Tk()
root.title("Sorting files 1.1")
root.geometry("300x300+700+200")
root.configure(bg="#6495ED")
root.resizable(False, False)

# Create a label and entry for the step value
step_label = Label(root, text="Enter a step value:")
step_label.pack(padx=10, pady=10)

step_entry = Entry(root)
step_entry.pack(padx=10, pady=10)

# Create a button to initiate the file moving process
move_button = Button(root, text="Move Files", command=move_files)
move_button.pack(padx=10, pady=10)
field = Text(root, width=30, height=10, font=('Arial', 10), bg="#4B0082", fg="#FFFACD")
field.pack(padx=20, pady=6)

root.mainloop()
