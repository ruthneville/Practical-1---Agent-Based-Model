# Practical-1---Agent-Based-Model

<h1> ReadMe </h1>

<h2> Introduction </h2><br>
A repository for code related to Practical 1 for the module GEOG5995M. The code is written using Python 3 in the IUD Spyder.

<h2> Contents </h2>

<p> This project contans two models, two associated agent frameworks and a file to run the environment. One model is successful in that it is able to produce an animation that models of the movement of the agent (sheep). The other model is an unsucessful attempt at the GUI practical.  </p>

<h4> <a href="https://github.com/ruthneville/Practical-1-Agent-Based-Model/blob/main/in.txt"> File to Run the Environment </a> </h4>

<h3> Final Successful Model </h3> 

  <li> <a href="https://github.com/ruthneville/Practical-1-Agent-Based-Model/blob/main/Agent%20Framework.py">  AgentFramework.Py </a> <br>
  Defines the Agent class that is used in the model.
  <br>
  <li> <a href="https://github.com/ruthneville/Practical-1-Agent-Based-Model/blob/main/Final%20Model%20-%20Animation%20Practical.py"> FinalModel - AnimationPractical.Py </a> <br>
   Sets up and runs the model and produces an animation of agent behaviour in the environment.<br>

<h3> Attempt at GUI Practical </h3>

  <li> <a href="https://github.com/ruthneville/Practical-1-Agent-Based-Model/blob/main/AgentFrameworkAttempt.py"> AgentFrameworkAttempt.py </a><br>
  Defines the Agent class that is used in the model.
  <br>
  <li> <a href="https://github.com/ruthneville/Practical-1-Agent-Based-Model/blob/main/FinalPracticalAttempt(GUI).py"> FinalPracticalAttempt(GUI).py </a><br>
   Sets up and attempts to run the model but fails to produce an animation inside of a GUI. An error occurs at line 105 which states "local variable 'animation' is assigned to but never used".

<h2> How To Run and What to Expect </h2>
<li> Copy the model code into one workbook in Spyder and the agent framework code into another, making sure that these are saved in the same directory.</li>
<li> Save the in.txt (environment) file to the same area. </li>
<li> Type "%matplot qt" in the console to ensure the animation will run in a pop out window as it may not run in the console.
<li> At present the model is set up to have 20 agents(sheep) which move randomly within the environment (field), 'eating' as they go. The model is set to iteratate 100 times. This can be changed by the user is desired.</li>
<li> Run the model, the ABM will be produced and it is expected that an animation of the agents (sheep) moving and eating the 100 x 100 environment (field) should appear. The agents (sheep) are marked by white hexagons with a black border. </li>

<h2> License </h2>

MIT license in repository.
