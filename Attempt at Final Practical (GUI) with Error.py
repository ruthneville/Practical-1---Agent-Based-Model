# Import libraries 
import random # Import a random number generator 
import tkinter
import matplotlib
# change the backend to render as associated with TkInter
matplotlib.use('TkAgg')
import matplotlib.pyplot # Import plotting software
import matplotlib.animation # Import animation software 
import agentframework # Import the Agent Class
import csv # Import software to open csv files
import requests
import bs4


# Set random numbers to be the same every time the model is run
random.seed(0)


# Create the environment (field)
# Call in CSV file
f = open('in.txt') #Open CSV 


# Set up the agents, these features can be changed
num_of_agents = 20 # The number of agents (sheep)
num_of_iterations = 50 # The number of times the model runs
neighbourhood = 5 # The proximity of agents (sheep) to share resources with
agents = [] # Create a list for the Agents
environment = [] # Create empty environment list 

# scraping x and y data
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

# Set the parameters for the animation
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0, 0, 1, 1])


# Read in the environment 
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
# Shift environment into a 2.D list
for row in reader:
    rowlist = []
# Add each value to rowlist
    for value in row:
        rowlist.append(value)
# Attach rowlist to environment
    environment.append(rowlist)
# Close the file
f.close()


# Create a line of code to convince self that agentframeowrk file is connected
a = agentframework.Agent(environment, agents)
# print(a.x, a.y)


#Loop through and create the agents and append information about environment and other agents
# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    
    
# Animating the model
# Create the update function
def update(frame_number):
    
    fig.clear() # Clear figure
    global carry_on
    
# Activate the agents (sheep)
# for j in range(num_of_iterations):
#     # Modify loop to shuffle and re-organise list of agents
#     random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
# add new sharing with neighbours method
        agents[i].share_with_neighbours(neighbourhood)
        

            
# Model visualisation
# Plot all agents onto a scatterplot
    matplotlib.pyplot.xlim(0, 100) # Set x axis to 0 - 100
    matplotlib.pyplot.ylim(0, 100) # Set y axis to 0 - 100
    matplotlib.pyplot.title("Final Model - Sheep Grazing in a Field") # Give scatterplot title 'Final Model'
    matplotlib.pyplot.ylabel("Environment (Field)") # Name y axis 'Environment (Grass)'
    matplotlib.pyplot.xlabel("Environment (Field)") # Name x axis 'Environment (Grass)'
    # matplotlib.pyplot.legend(["Sheep"], loc = "upper center") tried to add a legend but it would not work, just came up with blank square
    matplotlib.pyplot.imshow(environment) # plot to environment (grass)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color="white",  # plot the agents with markers with the colour white
                                  edgecolor="black", marker="H", s=60) # with black edges, shaped like hexagons (close to sheep?), and at size 60
  
       
# function that will run model
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat = False, frames=num_of_iterations)
    # here I receive an error that says local variable 'animation' is assigned to but never used
    canvas.draw()
    
# Build main window for the GUI
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Make the menu
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()
