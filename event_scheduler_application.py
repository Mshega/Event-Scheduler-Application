import unittest

class Event:
    
    def __init__(self, event_title, event_description, event_date, event_time):
        
        self.event_title = event_title
        self.event_description = event_description
        self.event_date = event_date
        self.event_time = event_time
    
    ''' arrangers ''' 
    def set_event_title(self, title):
        self.event_title = title
        
    def set_event_description(self, description):
        self.event_description = description
    
    def set_event_date(self, date):
        self.event_date = date
    
    def set_event_time(self, time):
        self.event_time = time
        
    ''' accessors '''
    def get_event_title(self):
        return self.event_title
    
    def get_event_description(self):
        return self.event_description
    
    def get_event_date(self):
        return self.event_date
    
    def get_event_time(self):
        return self.event_time
    
    ''' Compares two events and returns 1 if the first event is greater, 0 if they are equal, and -1 if the first event is less '''
    def compare_dates(self, other_event):
        this_date = self.get_event_date()
        other_date = other_event.get_event_date()
        
        this_date_parts = this_date.split("-")
        other_date_parts = other_date.split("-")
        
        ''' Examine the differences in years, months, and days '''
        if int(this_date_parts[0]) == int(other_date_parts[0]):
            
            if int(this_date_parts[1]) == int(other_date_parts[1]):
                
                if int(this_date_parts[2]) == int(other_date_parts[2]):
                    return 0
                
                elif int(this_date_parts[2]) > int(other_date_parts[2]):
                    return 1
                
                else:
                    return -1
            
            elif int(this_date_parts[1]) > int(other_date_parts[1]):
                return 1
            
            else:
                return -1
            
        elif int(this_date_parts[0]) > int(other_date_parts[0]):
            return 1
        
        else: 
            return -1


    def display_event(self):
        print("Title: " + self.event_title + " " + "Description: " + self.event_description + "  " + "Date: " + self.event_date + " " + "Time: " + self.event_time)
        

global event_collection
event_collection = []  
    
global valid_time
global valid_date
global valid_title



def insertion_sort(event_collection):
    n = len(event_collection)
      
    if n <= 1:
        return
 
    for i in range(1, n):
        key = event_collection[i]  
        j = i-1
        while j >= 0 and key.compare_dates(event_collection[j]) == -1:  
            event_collection[j+1] = event_collection[j] 
            j -= 1
        event_collection[j+1] = key   

def binary_search(val, array, start, end):
    if start < end:
     
        mid = (start + end) // 2
    
 
        # If element is present at the middle itself
        if array[mid].compare_dates(val) == 0:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif array[mid].compare_dates(val) == 1:
            return binary_search(val, array, start, mid - 1)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(val, array, mid+1, end)
     
    else:    
        return -1
    
    
    
def validate_time(time):
    
    if len(time) == len("HH:MM"):
        time_list = time.split(":")
        time_format = "HH:MM".split(":")
        
        if len(time_format) == len(time_list):
            
            if len(time_format[0]) == len(time_list[0]) and len(time_format[1]) == len(time_list[1]):
                
                if time_list[0].isnumeric() and time_list[1].isnumeric():
                    return True
                 
                else:
                    return False
            
            else:
                return False
        
        else:
            return False
        
            
def validate_date(date):
    ''' Check length of date '''
    if len(date) == len("YYYY-MM-DD"):
    
        date_list = date.split("-")
        format_list = "YYYY-MM-DD".split("-")
    
        if len(date_list) == len(format_list):
            
            if len(date_list[0]) == len(format_list[0]) and len(date_list[1]) == len(format_list[1]) and len(date_list[2]) == len(format_list[2]):
                
                if date_list[0].isnumeric() and date_list[1].isnumeric() and date_list[2].isnumeric:
                    
                    return True
                
                else:
                    return False
            
            else:
                return False
            
        else:
            return False
    
        
  
def create_event(): 
        
    ''' Adding event information '''
    
        
    ''' Verify the existence of the title '''
    event_title = input("Title: ")
    
    ''' Validity of the date format '''
    event_date = input("Date (YYYY-MM-DD): ")
    while not validate_date(event_date):
        event_date = input("Enter date format (YYYY-MM-DD): ")
    
        
    event_description = input("Description: ")
    
            
    ''' Validity of the time format '''    
    event_time = input("Time (HH:MM): ")
    while not validate_time(event_time):
        event_time = input("Enter time format (HH:MM): ")
        
    ''' Appending an event to the list '''
    event_collection.append(Event(event_title, event_description, event_date, event_time))
    insertion_sort(event_collection)
    
    print("\nEvent created.\n")
        
        
def view_event():
    view_prompt = input("Insert ALL to view all events, or ONE to view one event\nInsert: ")
        
    if view_prompt.upper() == "ALL":
        for event in event_collection:
            event.display_event()
                
    elif view_prompt.upper() == "ONE":
        event_date = input("Please enter date of event: ")
        
        while not validate_date(event_date):
            event_date = input("Enter date format (YYYY-MM-DD):")  
            
        event = binary_search(Event("", "", event_date, ""), event_collection, 0, len(event_collection))
        
        if event == -1:
            print("Event not found.")
        else:
            event_collection[event].display_event()
    else:
        print("Incorrect option.")
            
def delete_event():
    delete_date = input("Please enter date of the event you wish to delete: ")
    
    while not validate_date(delete_date):
        delete_date = input("Enter date format (YYYY-MM-DD):")
        
    index = binary_search(Event("", "", delete_date, ""), event_collection, 0, len(event_collection))
    
    if index == -1:
        print("Event not found.")
    
    else:
        event_collection.remove(event_collection[index])
        print("Event deleted successfully.\n")
        
def edit_event():
    event_date = input("Please enter date of the event you wish to edit: ")
    
    ''' Validity of the date format '''
    while not validate_date(event_date):
        event_date = input("Enter date format (YYYY-MM-DD): ")    
        
    index = binary_search(Event("", "", event_date, ""), event_collection, 0, len(event_collection))
    
    if index == -1:
        print("Event does not exist.")
        
    new_title = input("Edit title: ")
    new_description = input("Edit description: ")
        
    new_date = input("Edit date: ")
    while not validate_date(new_date):
        new_date = input("Enter date format (YYYY-MM-DD): ")
            
    new_time = input("Edit time: ")
    while not validate_time(new_time):
        new_time = input("Enter time format (HH:MM): ")
            
    event_collection[index].set_event_title(new_title)
    event_collection[index].set_event_description(new_description)
    event_collection[index].set_event_date(new_date)
    event_collection[index].set_event_time(new_time)
    
    event_collection[index].display_event()
    insertion_sort(event_collection)
    print("Event edited successfully.")
        
def main():   
    while True:
        prompt = input("Insert CREATE to add an event, VIEW to view event/s, DELETE to delete an/or event/s, EDIT to modify an event\nInsert: ")
            
        if prompt.upper() == "CREATE":
            create_event()
                
        elif prompt.upper() == "VIEW":
            view_event()
                
        elif prompt.upper() == "DELETE":
            delete_event()
                
        elif prompt.upper() == "EDIT":
            edit_event()
                
        else:
            print("Please choose one of the given options.\n")

if __name__ == '__main__':
    main()
