# Reinforcement Learning

## Info

Students have to provide access to a GitHub repository containing the code and reproducible results. Submit the link by email: 

to: emailAddr1, emailAddr2
Subject: RL Project Submission [Last Name]

The project is an individual work.
There are no constraints on the technology. You can use the gymnasium environment or any other framework for modeling environments and agents. Focus of the project is to evaluate the student understanding of the problems and the project discussion will include questions about theory starting from the proposed project. Generally speaking, the project proposals are just ideas that can be modified or just taken as suggestions for developing your own objectives.
Usage of AI coding assistants is allowed, but you are ultimately responsible for the submitted code.
Project presentations are expected to last about 10 minutes. Slides/notebooks are not mandatory but are appreciated. No need to submit anything in advance apart from the code link.

## Task description

Project 8: Museum Heist (project ID PG-2)

**Main Focus** stochastic policies, policy gradient

**Scientific Objective** the project investigates the challenges related to strategic environments that require the use of stochastic policies.

**Problem Description** A thief is trying to steal a specific painting from an art museum. A security camera is located in the correspondence of each exhibition room, but the security guard in the control room can only watch one video feed at a time. Once per minute, an algorithm selects the next location to show on the screen. Simultaneously, the thief can move to a nearby room or stay in the same room. The thief starts from an unknown initial room, has to reach an unknown target room (the one with the painting they want to steal) and go back to the initial room in order to escape. The thief has a map of the museum and is also in radio contact with a hacker who knows the current active security camera. The episode ends if the surveillance algorithm selects the room currently occupied by the thief, or if it selects the target room after the painting has been stolen, but the thief has already escaped.

**Tasks**
1. Model the environment as a gridworld, where each cell represents a room and nearby cells communicate through a door unless otherwise specified. Try different museum topologies by inserting “walls” between cells.
2. Model the policy of the adversary (thief) as follows: at each round the adversary computes the shortest path to the target room using the modified costs defined below, then moves to the next cell in the shortest path. The modified cost to move to any neighboring room is 1+𝛃*2^{-(n-1)}, where n is the number of rounds since the room was last selected by the surveillance algorithm and 𝛃 is a “prudence” constant. After stealing the painting, the thief’s new target becomes the initial room.
3. Model the surveillance algorithm as an agent that selects a room at each round, using a stateless tabular **Softmax policy**: each action (room) has a real parameter θ(a) and the action probability is proportional to exp(θ(a)/𝛕), where 𝛕>0 is a scalar temperature.
4. Train the surveillance agent using a **policy gradient** method of choice on repeated episodes (“heists”) and devise a way to evaluate the agent’s performance.
5. Visualize how the learned action probability is distributed across the rooms (e.g. using a heatmap). Discuss how the museum topology, policy temperature, and the thief’s prudence affect the action distribution.

**Challenging Variants**
Make the adversary also adaptive, for example by making the prudence parameter 𝛃 learnable.
Make the policy state-dependent by modeling an “alert” state carrying information on whether a missing artwork has been detected by the guard and in which room.
