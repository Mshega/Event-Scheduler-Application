# Description

This application allows users to create, view, edit, and delete events using a simple command-line interface. Each event consists of a title, description, date, and time. The application uses an in-memory data structure to store the events.

## Features

### 1. Create Events:
- Add new events with title, description, date, and time.
### 2. View Events: 
- List all events sorted by date and time, or view a specific event by date.
### 3. Edit Events:
- Modify the details of an existing event.
### 4. Delete Events: 
- Remove an event by its date.

## Requirements
### Data Storage
- Store events in a simple in-memory structure (e.g., a list).
### Event Creation
- Function to add a new event with title, description, date, and time.
- Validate that the date and time are in proper formats (e.g., YYYY-MM-DD for date, HH
for time).
### Listing Events
- Function to display all events, sorted by date and time.
- Each event should display all its details.
### Deleting Events
- Function to delete an event based on the date.
- If the event does not exist, display an appropriate message.

## User Interface
- Simple text-based interface in the command line.
- Provide options to create, view, edit, and delete events.
## Evaluation Criteria
- Code Quality: Readability, use of functions/classes, and adherence to Pythonic principles.
- Functionality: All features work as described.
- Error Handling: Gracefully handles invalid inputs and errors.
- Efficiency: Uses efficient algorithms and data structures where applicable.
## Installation and Setup
### 1. Clone the Repository:

```bash
git clone <repository-url>
cd <repository-directory>
```
### 2. Open the Project in VS Code:
- Check code under event_scheduler_application.py file
### 3. Run the Application:
```bash
python event_scheduler_application.py
```
## Usage
### Creating an Event
- Run the application.
- Select the CREATE option.
- Enter the title, description, date (YYYY-MM-DD), and time (HH
) for the event.
### Viewing Events
- Run the application.
- Select the VIEW option.
- Choose to view ALL events or a specific event by entering its date.
### Editing an Event
- Run the application.
- Select the EDIT option.
- Enter the date of the event you want to edit.
- Enter the new title, description, date, and time for the event.
### Deleting an Event
- Run the application.
- Select the DELETE option.
- Enter the date of the event you want to delete.
## Code Structure
The application is implemented in a single file: event_scheduler_application.py. It contains the following components:

- Event Class: Represents an event with attributes for title, description, date, and time, along with accessor and mutator methods.
- Utility Functions: Functions for date and time validation, insertion sort for sorting events, and binary search for finding events.
- Main Functions: Functions for creating, viewing, editing, and deleting events.
- Main Loop: The main program loop that provides a text-based interface for user interaction.
## Example Usage
### 1. Creating an Event:
```pt
Insert CREATE to add an event, VIEW to view event/s, DELETE to delete an/or event/s, EDIT to modify an event
Insert: CREATE
Title: Meeting
Date (YYYY-MM-DD): 2024-06-15
Description: Team meeting
Time (HH:MM): 14:00
Event created.
```
### 2. Viewing All Events:
```pt
Insert CREATE to add an event, VIEW to view event/s, DELETE to delete an/or event/s, EDIT to modify an event
Insert: VIEW
Insert ALL to view all events, or ONE to view one event
Insert: ALL
Title: Meeting Description: Team meeting Date: 2024-06-15 Time: 14:00
```
### 3. Editing an Event:
```pt
Insert CREATE to add an event, VIEW to view event/s, DELETE to delete an/or event/s, EDIT to modify an event
Insert: EDIT
Please enter date of the event you wish to edit: 2024-06-15
Edit title: Updated Meeting
Edit description: Updated team meeting
Edit date: 2024-06-16
Edit time: 15:00
Event edited successfully.
```
### 4. Deleting an Event:
```pt
Insert CREATE to add an event, VIEW to view event/s, DELETE to delete an/or event/s, EDIT to modify an event
Insert: DELETE
Please enter date of the event you wish to delete: 2024-06-15
Event deleted successfully.
```
## Conclusion
This application provides a simple and effective way to manage events through a command-line interface. It demonstrates good practices in Python programming, including data validation, sorting algorithms, and user interaction handling.
