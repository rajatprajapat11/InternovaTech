import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

from organizer import organize
from duplicate import find_duplicates
from undo import undo_last_operation
from utils import get_statistics

# -----------------------------
# Window Setup
# -----------------------------

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Smart File Organizer Pro")

app.geometry("1050x700")

app.resizable(False, False)

selected_folder = ""

# -----------------------------
# Functions
# -----------------------------

def browse_folder():

    global selected_folder

    folder = filedialog.askdirectory()

    if folder:

        selected_folder = folder

        folder_entry.delete(0, "end")

        folder_entry.insert(0, folder)

        status_label.configure(text="Folder Selected")

        # update_statistics()


# def update_statistics():

#     global selected_folder

#     if selected_folder == "":
#         return

#     stats = get_statistics(selected_folder)

#     stats_label.configure(
#         text=f"""
# 📊 Total Files : {stats['Total']}

# 🖼 Images      : {stats['Images']}
# 📄 Documents   : {stats['Documents']}
# 🎬 Videos      : {stats['Videos']}
# 🎵 Music       : {stats['Music']}
# 📦 Archives    : {stats['Archives']}
# 💻 Programs    : {stats['Programs']}
# 📁 Others      : {stats['Others']}
# """
#     )


def organize_files():

    global selected_folder

    if selected_folder == "":

        messagebox.showerror("Error", "Please select a folder.")

        return

    moved = organize(selected_folder)

    organized_label.configure(
        text=f"Organized : {moved}"
    )

    progress.set(1)

    status_label.configure(text="Organization Completed")

    messagebox.showinfo(
        "Done",
        f"{moved} files organized."
    )


def duplicate_files():

    global selected_folder

    if selected_folder == "":

        messagebox.showerror("Error", "Please select a folder.")

        return

    duplicates, size = find_duplicates(selected_folder)

    duplicate_label.configure(
        text=f"Duplicates : {len(duplicates)}"
    )

    messagebox.showinfo(
        "Duplicate Scan",
        f"{len(duplicates)} duplicate files found."
    )


def undo():

    restored = undo_last_operation()

    organized_label.configure(
        text="Organized : 0"
    )

    progress.set(0)

    status_label.configure(text="Undo Completed")

    messagebox.showinfo(
        "Undo",
        f"{restored} files restored."
    )


def view_logs():

    if not os.path.exists("activity.log"):
        messagebox.showinfo("Logs", "No activity log found.")
        return

    log_window = ctk.CTkToplevel(app)

    log_window.title("Activity Log")

    log_window.geometry("800x500")

    textbox = ctk.CTkTextbox(log_window)

    textbox.pack(fill="both", expand=True, padx=20, pady=20)

    with open("activity.log", "r", encoding="utf-8") as file:
        textbox.insert("1.0", file.read())

    textbox.configure(state="disabled")


# -----------------------------
# Sidebar
# -----------------------------

sidebar = ctk.CTkFrame(app, width=220)

sidebar.pack(side="left", fill="y")

title = ctk.CTkLabel(
    sidebar,
    text="SMART\nFILE\nORGANIZER",
    font=("Arial",28,"bold")
)

title.pack(pady=30)

ctk.CTkButton(
    sidebar,
    text="📜 View Logs",
    command=view_logs,
    width=180
).pack(pady=10)

ctk.CTkButton(
    sidebar,
    text="📂 Browse Folder",
    command=browse_folder,
    width=180
).pack(pady=10)

ctk.CTkButton(
    sidebar,
    text="📁 Organize Files",
    command=organize_files,
    width=180
).pack(pady=10)

ctk.CTkButton(
    sidebar,
    text="🔍 Find Duplicates",
    command=duplicate_files,
    width=180
).pack(pady=10)

ctk.CTkButton(
    sidebar,
    text="↩ Undo",
    command=undo,
    width=180
).pack(pady=10)

# -----------------------------
# Main Area
# -----------------------------

main = ctk.CTkFrame(app)

main.pack(fill="both", expand=True)

heading = ctk.CTkLabel(
    main,
    text="Dashboard",
    font=("Arial",30,"bold")
)

heading.pack(pady=20)

folder_entry = ctk.CTkEntry(
    main,
    width=650,
    height=40,
    placeholder_text="Choose Folder..."
)

folder_entry.pack()

stats = ctk.CTkFrame(main)

stats.pack(pady=25)

organized_label = ctk.CTkLabel(
    stats,
    text="Organized : 0",
    font=("Arial",20)
)

organized_label.pack(pady=10)

duplicate_label = ctk.CTkLabel(
    stats,
    text="Duplicates : 0",
    font=("Arial",20)
)

duplicate_label.pack(pady=10)

progress = ctk.CTkProgressBar(
    main,
    width=600
)

progress.pack(pady=25)

progress.set(0)

status_label = ctk.CTkLabel(
    main,
    text="Ready",
    font=("Arial",18)
)

status_label.pack()

app.mainloop()