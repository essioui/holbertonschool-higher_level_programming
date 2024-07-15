#!/usr/bin/python3


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template should be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: attendees should be a List")
        return
    
    if not all(isinstance(x, dict) for x in attendees):
        print("Error: attendees should be a list of dictionaries")
        return
    
    # if template and attendees are empty
    if not template:
        print("Error: template is empty")
        return
    
    if not attendees:
        print("Error: attendees is empty")
        return
    
    # Process Each Attendee
    y = 1
    for attendee in attendees:
        processed_template = template

        # replace the placeholders
        for key in ["name", "event_title", "event_date", "event_location"]:
            placeholder = "{" + key + "}"
            value = attendee.get(key, "N/A")
            if not value:
                value = "N/A"
            processed_template = processed_template.replace(placeholder, value)

        filename = f"output_{y}.txt"
        try:
            with open(filename, "w") as f:
                f.write(processed_template)
                print(f"Invitation for {attendee.get('name', 'Unknown')} generated as {filename}.")
        except Exception as e:
            print(f"An error occurred while writing to {filename}: {e}")

        y += 1
