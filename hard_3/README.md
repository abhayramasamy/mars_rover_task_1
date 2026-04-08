# Behaviour Tree construction

In this Hard Problem 3 we construct a Behaviour tree for a system(rover), that basically that takes decisions for the rover in various cases, in different battery levels and also helps in navigating obstacles.

## Whats a behaviour tree?
**Small note:** <br/>
A behavior tree is a mathematical model of plan execution used in computer science, robotics, control systems and video games. They describe switchings between a finite set of tasks in a modular fashion. They are able to construct and take complex decisions in different scenarios by just simple tasks.

Its often a pretty standard diagramatic notation used in robotics to descibe control system's decision mkaing process.

Also there are tools available that like behaviour_tree.cpp behaviour_tree3.js that can directly transalate the decision tree directly to code easier, faster and safer to be readily used in robotic systems easily integrable with ROS

## question 1, battery checker:
1) This consists of a fallback node that tests each every child node and return status.
2) No problem if battery is above safe levels.
3) if Battery is not critically low but less than ideal, turn off unnecessary systems
4) if battery is critically low, rush to base.

## question 2, navigation:
1) while you move a distance, check for obstacles next (sequential)
2) if no obstacles no problem, else check for the size of the obstacle (fallback node)
3) if the size of the obstacle was small, navigate around it.
4) if the size was large try checking for a path available around it in the map, else bscktrack.

## Learning take aways:
- Got exposed to behaviour tree methods and tools and its essence in Robotics.
- studied and learnt to construct an extremely basic behaviour tree.