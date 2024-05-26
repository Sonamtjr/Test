from queue import LifoQueue

# Create instances of LifoQueue for backward and forward navigation history
backward_history = LifoQueue()
forward_history = LifoQueue()

# Initialize the current page to None
current_page = None

# Prompt the user to enter the number of URLs they have visited
NoOfVisits = int(input("Enter the number of URLs you have visited: "))

# Loop to enter the URL history
for _ in range(NoOfVisits):
    url = input("Enter the URL: ")
    print(f"Visiting {url}")
    
    if current_page is not None:
        backward_history.put(current_page)
    
    current_page = url

# Print the current page
print(f"Current page: {current_page}")

# Function to navigate back
def navigate_back():
    global current_page
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous pages available to navigate back to.")

# Function to navigate forward
def navigate_forward():
    global current_page
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No forward pages available to navigate forward to.")

# Back navigation loop
while input("Do you want to go back? (yes/no): ").lower() == 'yes':
    navigate_back()

# Forward navigation loop
while input("Do you want to go forward? (yes/no): ").lower() == 'yes':
    navigate_forward()

print(f"Final current page: {current_page}")
