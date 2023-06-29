from tkinter import *

# Window dimension
window_width = 440
window_height = 660

# Generate window
window = Tk()

# Set the title
window.title('Pie Slap')

# Set the geometry
window.geometry("{}x{}".format(window_width, window_height))

# Set not able to resize
window.resizable(width=False, height=False)

# Load images
mainImage = PhotoImage(file='images/Grapefruit.png')
pieImage = PhotoImage(file='images/Pie.png')
drop1Image = PhotoImage(file='images/Drop1.png')
drop2Image = PhotoImage(file='images/Drop2.png')
drop3Image = PhotoImage(file='images/Drop3.png')

# Location of animation
pie_start = pie_start_x, pie_start_y = 0, 360
pie_end = pie_end_x, pie_end_y = 190, 250
drop1_start = drop1_start_x, drop1_start_y = 260, 215
drop1_end = drop1_end_x, drop1_end_y = 420, 175
drop2_start = drop2_start_x, drop2_start_y = 240, 145
drop2_end = drop2_end_x, drop2_end_y = 380, 35
drop3_start = drop3_start_x, drop3_start_y = 279, 323
drop3_end = drop3_end_x, drop3_end_y = 411, 456

# Resize images
mainImage = mainImage.subsample(8) # The image should be 1/8 of the original
pieImage = pieImage.subsample(8) # The image should be 1/8 of the original
drop1Image = drop1Image.subsample(8) # The image should be 1/8 of the original
drop2Image = drop2Image.subsample(8) # The image should be 1/8 of the original
drop3Image = drop3Image.subsample(8) # The image should be 1/8 of the original

# Keep track of objects
pie = None
drop1 = None
drop2 = None
drop3 = None


# Draw background
canvas = Canvas(window, width=window_width, height=window_height)
canvas.pack()
background = canvas.create_image(0, 0, anchor=NW, image=mainImage)

# Function keep track of motion
def motion(event):
    global pie, drop1, drop2, drop3
    # Reset images
    if pie:
        canvas.delete(pie)
    if drop1:
        canvas.delete(drop1)
    if drop2:
        canvas.delete(drop2)
    if drop3:
        canvas.delete(drop3)
    # Get coordinates
    x, y = event.x, event.y
    # Debug
    # print("X: ", x, " Y: ", y)
    # We can do a top to bottom version using the y coordinate as well
    # Calculate the frame index based on x position
    index = int(x // (window_width / 60))
    # Avoid out of range
    index = 0 if index < 0 else index
    index = 59 if index > 59 else index
    # Case before 30, pie flying
    if index < 30:
        pie_x = pie_start_x + int((pie_end_x-pie_start_x)/30*index)
        pie_y = pie_start_y + int((pie_end_y-pie_start_y)/30*index)
    # Case after 30, drops flying
    else:
        pie_x = pie_end_x
        pie_y = pie_end_y
        drop1_x = drop1_start_x + int((drop1_end_x-drop1_start_x)/(59-30)*(index-30))
        drop1_y = drop1_start_y + int((drop1_end_y-drop1_start_y)/(59-30)*(index-30))
        
        drop2_x = drop2_start_x + int((drop2_end_x - drop2_start_x) / (59 - 30) * (index - 30))
        drop2_y = drop2_start_y + int((drop2_end_y - drop2_start_y) / (59 - 30) * (index - 30))
        
        drop3_x = drop3_start_x + int((drop3_end_x - drop3_start_x) / (59 - 30) * (index - 30))
        drop3_y = drop3_start_y + int((drop3_end_y - drop3_start_y) / (59 - 30) * (index - 30))

        drop1 = canvas.create_image(drop1_x, drop1_y, anchor=CENTER, image=drop1Image)
        drop2 = canvas.create_image(drop2_x, drop2_y, anchor=CENTER, image=drop2Image)
        drop3 = canvas.create_image(drop3_x, drop3_y, anchor=CENTER, image=drop3Image)
    pie = canvas.create_image(pie_x, pie_y, anchor=CENTER, image=pieImage)



window.bind('<Motion>', motion)
window.mainloop()