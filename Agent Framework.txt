# Import library 
import random # Import random library which generates random numbers

# Define Agent Class
class Agent:
    
    # Create agents and add to list
    def __init__ (self, environment, agents): # Passes variables into a list to link to other objects

        self.x = random.randint(0,99) # Set starting x co-ordinate to somewhere between 0 and 99
        self.y = random.randint(0,99) # Set starting y co-ordinate to somewhere between 0 and 99
        self.environment = environment # Set the environment (field)
        self.store = 0 # Creates a store of food for each agent (sheep) to in eat method
        self.agents = agents # Used in share with neighbours method
      
    
    def move (self): # Create a method to make the agents move
         
        if random.random() < 0.5: # If random number is less than 0.5
            self.y = (self.y + 1) % 100 # Add 1 to x co-ordinate
        else: # If random number is not less than 0.5
            self.y = (self.y - 1) % 100 # Subtract 1 from x co-ordinate

        if random.random() < 0.5: # If random number is more than 0.5
            self.x = (self.x + 1) % 100 # Add 1 to y co-ordinate
        else: # If random number is not less than 0.5
            self.x = (self.x - 1) % 100 # Subtract 1 from y co-ordinate
            
    def eat(self): # Create a method to make the agents (sheep) eat 
    
        if self.environment[self.y][self.x] > 10: # If the environment (field) is more than 10
            self.environment[self.y][self.x] -= 10 # Minus 10 from the environment (field)
            self.store += 10 # Add 10 to agents store (sheeps stomach)
   
    
    def distance_between(self, agent): # Define distance and work out distance between two sheep
       
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5  # Pythagoras Theorem
    
    
    def share_with_neighbours(self, neighbourhood): # Create method for agents (sheep) to share with others
        
        for agent in self.agents:
            dist = self.distance_between(agent) # Create variable dist and assign it the difference between two agents (sheep)
            if dist <= neighbourhood: # If the distance is less than the neighbourhood, and the agents (sheep) are in eachothers neighbourhoods
                sum = self.store + agent.store # Sum the two agents (sheep) food stores
                average = sum /2 # Divide the sum by two to get the average
                self.store = average # Give one agent (sheep) the average food store
                agent.store = average # And give the other agent (sheep) the average food store
            # print("sharing " + str(dist) + " " + str(ave))

   