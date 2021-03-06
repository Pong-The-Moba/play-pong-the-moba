pong-the-moba playtest instructions
==================
Welcome to the pong-the-moba Alpha Playtest! Thanks for helping us out.


###SHORT AND SWEET <3
    1. Grab this repository (zip or clone) and unpack it. <br>
    2. Double click on server.jar to run it. (There's now a server on localhost)<br>
    3. Open a client.jar and type in localhost and hit go. <br>
    4. Open another client.jar on another computer (or on same computer if no playmate). <br>
    5. Enter the inward facing IP address of the computer with the server in it. <br>
    6. Click Go. <br>

If opening jars isn't working, try to open up a command line, navigate to the directory, and run 

```
java -jar server.jar
java -jar client.jar 
```

If you're on linux, you may need additional argument for the client:<br>

```
java -Djava.library.path=. -jar client.jar 
```


Currently, our Images happen to be in CYMK (that's changing soon), so it may not load correctly on Linux. 

###LONG VERSION

<b> Getting Started </b>

Warning, this a game meant to be played by 2 people (and 2 computers). Although it is possible to play on your own by opening two clients on the same machine, it may not be as much fun :smile:.

Start by either downloading the zip file or cloning the repository. Cloning will speed up the download if you participate in any later playtests, but the choice is yours. The zip download can be found as a button on the right pane of the repo's home screen (supposedly). or [here](https://github.com/Pong-The-Moba/play-pong-the-moba/archive/production.zip)

While the download goes, find out the local ip address of the player who will run the server for your game. Currently, the game is played peer-to-peer, which means until some witchcraft happens, it can only be played by LAN. :scream:

<b> Running the Game </b>

Once that completes, open the directory produced and run server.jar. Then, both players should run Client.jar. If you see a black popup window asking for an IP address, you're doing it right.

If you don't see this screen, check to make sure your Java version is current, that you haven't removed the jar from the directory, and that you have execute permissions on the jar. If all of these are the case or if you're stuck, send us an email saying what you saw.

<b> Running entering the IP Address of the server</b><br>
Now, both players should enter the IP address of the server. The player running the server can also enter localhost or 127.0.0.1. Then, hit enter or click go. If your internet is bad, you'll see a crash here. Most likely, you're entering the wrong ip address – possibly a public-facing address. Double check that, then send us an email saying what you saw.

<b> How to get your IP Address </b><br>
If you are familiar with command line for your OS:
try typing in ipconfig or ifconfig and see what the local ip address is (normally starts with 192.168.--). 

Otherwise, on OSX - open up network preferences from the icon top right (wifi icon). There should be an ip address in the window that opens up that likewise starts with 192.168.--.

On Windows, click the network icon lower right in task bar and try to get to the details through properties or status menu of your current internet connection. You're also looking for a 192.168.--.

<b>Controls </b>

Hopefully, you're now in the game. The controls are:
up/down: up, down. Amazing.
Left/right: rotate paddle counter/clockwise.
Space: Shoot laser
Q: Explosive paddle.

The teal bars behind the paddles are mana. The big numbers in the middle are the score. The red and blue line wandering around the middle of the game is the ball serve machine – when you score, the ball will pop out of it.

Thank you for your time and effort! Please fill out the survey  [here](https://docs.google.com/forms/d/11MTeljkYPyR6gCuLSyL629C09zqxlYAtPfdsPPqZDT0/viewform?usp=send_form)

The code is designed to be friendly to new designers making small contributions. If you're interested, send us an email.

<b> Contact us! </b><br>
jtbooth1@gmail.com<br>
sihrc.c.lee@gmail.com
