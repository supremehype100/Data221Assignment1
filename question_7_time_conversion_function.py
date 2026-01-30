def seconds_to_time(seconds):
    # Validate input by ensuring time is between 0 and 24 hours
    try:
        seconds = int(seconds)
    except:
        return "Invalid input: seconds must be an integer."
    if seconds < 0 or seconds >= 86400:
        return "Invalid input: seconds must be between 0 and 86399."

    # Calculate hours, minutes, and seconds
    hours_24 = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    # Determine AM/PM and convert to 12-hour format
    period = "AM" if hours_24 < 12 else "PM"
    hours_12 = hours_24 % 12
    if hours_12 == 0:
        hours_12 = 12

    # Return formatted string
    return f"{hours_12:02d}:{minutes:02d}:{secs:02d} {period}"


