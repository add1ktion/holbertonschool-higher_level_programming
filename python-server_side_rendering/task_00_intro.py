#!/usr/bin/python3
"""
Create a Python function that generates personalized invitation files from a
template with placeholders and a list of objects. Each output file should be
named sequentially, starting from 1. You will also implement specific error
handling for various edge cases.
"""

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input type: template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input type: attendees should be a list of dictionaries.")
        return
    
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for i, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"

            content = content.replace(f"{{{key}}}", str(value))
        
        with open(f"output_{i}.txt", "w") as file:
            file.write(content)
