# User Interface to interact with the Local RAG Model
# Created: 2024-10-29
# By: Jacky Luong

import tkinter
import customtkinter
import pywinstyles
import os
import asyncio
from query_data import query_rag
from PIL import Image, ImageTk

# Array of all textboxes
text_boxes = []

# Font size factor when the app window is resized
font_size_factor = 30

# Font size
font_size = 30

# Background image
background_image_path = "images/AI Chat Window.png"

# Default button image
button_image_path = "images/Chat Send Button Default.png"

# Hover button image
button_image_active_path="images/Chat Send Button Active.png"

# AI icon
ai_image_icon_path="images/Bot Icon.png"

# Function to dynamically adjust font size based on window size
#
# Params
# Event event default(None)
def update_font_size(event=None):
    # Calculate a new font size based on window width
    wrap_length = max(10, int(app.winfo_width() - (app.winfo_width() / 3)))
    
    new_font_size = max(10, int(app.winfo_width() / font_size_factor))
    font_size = new_font_size
    message.configure(font=("Arial", new_font_size))

    # Update new font size on all text boxes
    for text_box in text_boxes:
        text_box.configure(font=("Arial", new_font_size), wraplength=wrap_length)

# Function to execute functions when the window is being resized
#
# Params
# Event event
def window_resize_function(event):
    # update_background_size(event)
    update_font_size(event)

# Function to change the image of the submit button when it is hovered
#
# Params
# Event event
def on_enter_submit_button(event):
    button_image_active = Image.open(button_image_active_path)
    button_photo_active = customtkinter.CTkImage(dark_image=button_image_active, size=(100, 100))
    submit_button.configure(image=button_photo_active)

# Function to change the image of the submit button back to the default image when it leave hover
#
# Params
# Event event
def on_leave_submit_button(event):
    button_image = Image.open(button_image_path)
    button_photo = customtkinter.CTkImage(dark_image=button_image, size=(100, 100))
    submit_button.configure(image=button_photo)

# Function calls query_data.query_rag() and generates a display for the user's input and the ai's input
#
# Params
# string question
# CTkTextbox question_text_box
# CTkFrame response_frame
async def query_rag_gui(question, question_text_box, response_frame):
    # Hide submit button
    submit_button.pack_forget() 

    # Retrieve answer from RAG
    response_text =  await query_rag(question)

    # User response
    user_frame = customtkinter.CTkFrame(response_frame, fg_color="#2f6888", bg_color="#2f6888")
    user_frame.pack(fill="both", expand=True, pady=10)

    wrap_length = max(10, int(app.winfo_width() - (app.winfo_width() / 2)))

    # User textbox
    user_text_box = customtkinter.CTkLabel(user_frame,  text=question, justify="right", wraplength=wrap_length)
    user_text_box.configure(state="disabled")  # Disable the text box to make it read-only
    
    # Adjust_textbox_height(user_text_box)
    user_text_box.pack(side="right", pady=10, padx=(120,70))

    # AI response
    ai_frame = customtkinter.CTkFrame(response_frame, fg_color="#2f6888", bg_color="#2f6888")
    ai_frame.pack(fill="both", expand=True, pady=10, padx=10)

    # AI Image Icon
    ai_image = Image.open(ai_image_icon_path)
    ai_photo = customtkinter.CTkImage(dark_image=ai_image, light_image=ai_image, size=(50, 50))
    ai_label = customtkinter.CTkLabel(ai_frame, width=50, height=50, image=ai_photo, text="")
    ai_label.place(x=50, y=10)

    wrap_length = max(10, int(app.winfo_width() - (app.winfo_width() / 3)))

    # AI textbox
    ai_text_box = customtkinter.CTkLabel(ai_frame, text=response_text, justify="left", wraplength=wrap_length)
    ai_text_box.configure(state="disabled")  # Disable the text box to make it read-only
    ai_text_box.pack(side="left", pady=10, padx=(120,70))

    # Clear the textbox
    question_text_box.delete(0, customtkinter.END)

    # Add generated textboxs to the textbox array
    text_boxes.append(user_text_box)
    text_boxes.append(ai_text_box)
    
    # Update fonts for textboxes
    update_font_size()

    # Show submit button
    submit_button.pack(side="right", padx=(5,30)) 

# Function executes query_rag_gui() on another thread to prevent the window from freezing
#
# Params
# string question
# CTkTextbox question_text_box
# CTkFrame response_frame
def run_query_rag(question, question_text_box, response_frame, submit_button):
    # Prevents empty inputs
    if(question == None or question.replace(" ", "") == ""):
        return

    # Check if there is a loop, if not create a new one
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # Run the query function on another thread
    if(loop != None):
        result = loop.run_in_executor(None, asyncio.run, query_rag_gui(question, question_text_box, response_frame))

customtkinter.set_default_color_theme(os.getcwd() + "/theme.json")

# App Frame
app=customtkinter.CTk()
app.geometry("720x480")
app.minsize(720, 480)
app.title("AI Chat")

app.grid_columnconfigure(0, weight=1)  # Make the single column responsive
app.grid_rowconfigure(0, weight=4)     # First row (textbox) takes 3/4 of space
app.grid_rowconfigure(1, weight=1)

# Response frame
response_frame = customtkinter.CTkScrollableFrame(app, fg_color="#2f6888", bg_color="#2f6888", scrollbar_fg_color="#173c53", scrollbar_button_color="#173c53", scrollbar_button_hover_color="#173c53")
response_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Input frame
input_frame = customtkinter.CTkFrame(app, fg_color="#2f6888", bg_color="#2f6888", height=(app.winfo_height()/4))
input_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

# User question box
message = customtkinter.CTkEntry(input_frame, width=350, height=40, text_color="white", fg_color="#2f6888", bg_color="#2f6888", placeholder_text="Type your message to AI bot here")
pywinstyles.set_opacity(message, value=0.3)
message.configure(bg_color="transparent", border_width=0) 
message.pack(side="left", fill="both", expand=True, padx=(70,5))

# Load the PNG image using PIL and resize it to fit the window
button_image = Image.open(button_image_path)

# Convert the image to a Tkinter-compatible image
button_photo = customtkinter.CTkImage(dark_image=button_image, size=(100, 100))

# Submit button
submit_button = customtkinter.CTkButton(input_frame, width=100, height=100, hover_color="grey", fg_color="grey", bg_color="grey", image=button_photo, text="", command=lambda: run_query_rag(message.get(), message, response_frame, submit_button))
pywinstyles.set_opacity(submit_button, color="grey")
submit_button.pack(side="right", padx=(5,30)) 
submit_button.bind("<Enter>", on_enter_submit_button)
submit_button.bind("<Leave>", on_leave_submit_button)

# AI default greeting
ai_frame = customtkinter.CTkFrame(response_frame, fg_color="#2f6888", bg_color="#2f6888")
ai_frame.pack(fill="both", expand=True, pady=10, padx=10)

# AI default greeting image icon
ai_image = Image.open(ai_image_icon_path)
ai_photo = customtkinter.CTkImage(dark_image=ai_image, light_image=ai_image, size=(50, 50))
ai_label = customtkinter.CTkLabel(ai_frame, width=50, height=50, image=ai_photo, text="")
ai_label.place(x=50, y=10)

# AI default greeting textbox
ai_text_box = customtkinter.CTkLabel(ai_frame, text="Hello! Ask me a question regarding Monopoly.", justify="left")
ai_text_box.configure(state="disabled")  # Disable the text box to make it read-only
ai_text_box.pack(side="left", pady=10, padx=(120,70))

# Update font size upon launch
text_boxes.append(ai_text_box)
update_font_size()

# Bind the function to window resizing
app.bind("<Configure>", window_resize_function)

app.mainloop()
