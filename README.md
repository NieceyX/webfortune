# webfortune

webfortune is a small web application that allows the user to speak to cows.
Going to / or /fortune/ gives the user their fortune.
Going to /cowfortune/ has a cow give the user a fortune.
Going to /cowsay/<message>/ where <message> is your own message has a cow speak your message back to you.
  
# Installation
*This assumes you have Docker installed.*
  To start quickly, run `docker build -t <NAME>` , and <NAME> is the name of your docker container.
  Then, `docker run -dp <PORT>:5000 <NAME>` where <PORT> is the port you want to run it on.
  From there, go in your browser to <HOSTIP>:<PORT> and use the above routes to use it.

  When you are done, don't forget to stop your docker container by typing `docker rm -f <ID>` where <ID> is the 
    Container ID of your docker container, which you can find by typing `docker ps`.
  
