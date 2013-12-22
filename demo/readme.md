Notes on concepts covered in demo programs
============================================

1) Sequential Instructions
 - example: custom.py line 34-40.
 -- In order to make the robot move forward for a certain amount of time, need to stop the motors first in case the robot was already moving in an arbitrary direction,
 then set the motors to be moving forward, wait the given amount of time, then stop the motors. Sequential instructions to achieve a desired effect
 
2) Making decisions
 - example: custom.py line 97.
 -- If clause determines what the robot does based on the acquired reading from the ultrasonic sensor

3) Looping
 - example1: custom.py line 61.
 -- Repeat an action a certain number of times, in this case repeat the 'snap jaw' sequence of instructions i times
 - example2: custom.py line 86.
 -- Monitoring state information, repeatedly executing code until a condtion is met, in this case when both touch sensors are pressed (meaning the legs have synced up)

4) Library/API
 - custom.py lines 4 and 5 imports a bunch of stuff, which is used throughout the code. The robot API allows the programmer to control the robot by making
 API calls coupled with regular familiar programming statements. This is how most programs interact with hardware/internet/software services nowadays: an API
 is exposed, and the programmer uses that to write logic that utilises what's behind the API.

5) Abstraction
 - ie abstracting raw code into logical, callable, reusable units, in the case of this program by defining functions. Abstraction is a fundamental principle in
 programming, which people have said is all about "managing complexity".
 - In custom.py, the main program logic is achieved in 20 lines of code between line 95
 and line 115, and this is enabled by abstracting long raw sequences of motor/sensor commands into logical functions (line 21-93). The use of logical functions not only
 reduces the size of the actual program logic code block, but makes it much easier to read, discuss and reason around the logic.
 
Key idea here I guess is that custom.py is a considerably complete program example, and you can write non-robot programs for "practical" applications
and they would look quite like this program - same control structures, same abstraction mechanisms, just probably using different API calls and different
algorithms.