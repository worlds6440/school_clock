from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
import datetime
import time

# Setup font to use
font_time = ImageFont.truetype(FredokaOne, 80)
font_message = ImageFont.truetype(FredokaOne, 40)

# Setup display to use (takes a few seconds)
inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.BLACK)

def is_time_between(begin_time, end_time, check_time=None):
    """ If check time is not given, default to current UTC time """
    check_time = check_time or datetime.datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

def get_message(cur_time):
    """ Return a string message based
        upon the current time """
    message = ""
    if is_time_between(datetime.time(8,30), datetime.time(9,0), cur_time):
        message = "Breakfast"

    elif is_time_between(datetime.time(9,0), datetime.time(9,30), cur_time):
        message = "Screen Time"
    elif is_time_between(datetime.time(9,30), datetime.time(10,0), cur_time):
        message = "School Work"

    elif is_time_between(datetime.time(10,0), datetime.time(10,30), cur_time):
        message = "Snack / Play Time"
    elif is_time_between(datetime.time(10,30), datetime.time(11,0), cur_time):
        message = "Busy Play"

    elif is_time_between(datetime.time(11,0), datetime.time(11,30), cur_time):
        message = "School Work"
    elif is_time_between(datetime.time(11,30), datetime.time(12,0), cur_time):
        message = "Busy Play"

    elif is_time_between(datetime.time(12,0), datetime.time(12,30), cur_time):
        message = "Lunch Time"
    elif is_time_between(datetime.time(12,30), datetime.time(13,0), cur_time):
        message = "Walk"

    elif is_time_between(datetime.time(13,0), datetime.time(13,30), cur_time):
        message = "Busy Play"
    elif is_time_between(datetime.time(13,30), datetime.time(14,0), cur_time):
        message = "School Work"

    elif is_time_between(datetime.time(14,0), datetime.time(14,30), cur_time):
        message = "Snack / Play Time"
    elif is_time_between(datetime.time(14,30), datetime.time(15,0), cur_time):
        message = "Screen Time"

    elif is_time_between(datetime.time(15,0), datetime.time(15,30), cur_time):
        message = "School Work / Busy Play"
    elif is_time_between(datetime.time(15,30), datetime.time(16,0), cur_time):
        message = "Busy Play"

    elif is_time_between(datetime.time(16,0), datetime.time(16,30), cur_time):
        message = "Free Time"
    elif is_time_between(datetime.time(16,30), datetime.time(17,0), cur_time):
        message = "Free Time"

    return message

# Loop indefinitely
killed = False
while not killed:
    print("Displaying Time")

    # Get current time to display on screen
    time_now = datetime.datetime.now()
    time_now_str = time_now.strftime("%H:%M")
    date_now_str = time_now.strftime("%d/%m/%Y")

    # Display time on screen by creating
    # a new image and drawing the text into it
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)

    screen_quarters = inky_display.HEIGHT / 4

    # Display the time top left
    w, h = font_time.getsize(time_now_str)
    x = (inky_display.WIDTH / 3) - (w / 2)
    y = screen_quarters - (h / 2)
    draw.text((x, y), time_now_str, inky_display.BLACK, font_time)

    message = get_message(time_now.time())
    w, h = font_message.getsize(message)
    x = (inky_display.WIDTH / 2) - (w / 2)
    y = (inky_display.HEIGHT - screen_quarters) - (h / 2)
    draw.text((x, y), message, inky_display.RED, font_message)

    inky_display.set_image(img)
    inky_display.show()

    # Sleep 60 seconds (adjusted to take accound
    # of how long it took to update display
    time_diff = (datetime.datetime.now() - time_now)
    time.sleep(60 - time_diff.total_seconds())
