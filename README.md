# Reinforcement Learning

## General information and objectives

The project is an individual work. There are no constraints on the technology. 
You can use the gymnasium environment or any other framework for modeling environments and agents. 

Focus of the project is to evaluate the student understanding of the problems and 
the project discussion will include questions about theory starting from the proposed project. 

Project presentations are expected to last about 10 minutes. 
Slides/notebooks are not mandatory but are appreciated. 
No need to submit anything in advance apart from the code link.

## Task description

### Project 8: Museum Heist (project ID PG-2)

***Main Focus*** 

stochastic policies, policy gradient

***Scientific Objective***

the project investigates the challenges related to strategic environments that require the use of stochastic policies.

***Problem Description*** 

A Thief is trying to steal a specific painting from an art museum. 

A security camera is located in the correspondence of each exhibition room, 
but the security guard in the control room can only watch one video feed at a time.
Once per round, an algorithm selects the next location to show on the screen. 

Simultaneously, the Thief can **move to a nearby room** or **stay in the same room**. 
The Thief starts from an unknown initial room, has to reach an unknown target room 
(the one with the painting they want to steal) and go back to the initial room in order to escape.
The Thief has a map of the museum and is also in radio contact with a Hacker who knows the current active security camera.

The episode ends if:
- the surveillance algorithm selects the room currently occupied by the Thief,
- or the Thief escapes with the painting (if it selects the target room after the painting has been stolen, but the Thief has already escaped).

***Tasks***

- [x] Model the environment as a gridworld, where each cell represents a room and nearby cells communicate through a door unless otherwise specified. 
Try different museum topologies by inserting “walls” between cells.

- [x] Model the policy of the adversary (Thief) as follows: 
  - at each round the adversary computes the shortest path to the target room using the modified costs defined below; 
  - then moves to the next cell in the shortest path or stays in the same cell, if he cannot move 
  (The modified cost to move to any neighboring room is **1+𝛃*2^{-(n-1)}**), 
  where **n is the number of rounds since the room was last selected by the surveillance algorithm** and **𝛃 is a “prudence” constant**. 
  - After stealing the painting, the Thief’s new target becomes the initial room.

- [x] Model the surveillance algorithm as an Agent that selects a room at each round, 
using a stateless tabular **Softmax policy**: each action (room) has a real parameter **θ(a)** and the action probability 
is proportional to **exp(θ(a)/𝛕)**, where **𝛕>0 is a scalar temperature**.

- [ ] Train the surveillance Agent using a **policy gradient** method of choice on repeated episodes (“heists”) 
and devise a way to evaluate the Agent’s performance.

- [x] Visualize how the learned action probability is distributed across the rooms (e.g. using a heatmap). 
- [ ] Discuss how the museum topology (try different ones), policy temperature, and the Thief’s prudence affect the action distribution.

~~**Challenging Variants**~~

- ~~[ ] Make the adversary also adaptive, for example by making the prudence parameter 𝛃 learnable.~~
- ~~[ ] Make the policy state-dependent by modeling an “alert” state carrying information on whether a missing artwork 
has been detected by the guard and in which room.~~

## Submission information

Students have to provide access to a GitHub repository containing the code and reproducible results. 
Submit the link by email: 

to: emailAddr1, emailAddr2

Subject: RL Project Submission [Last Name]
