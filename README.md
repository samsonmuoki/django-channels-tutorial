# django-channels-tutorial
A simple websockets chat application using Django Channels

This a simple chat server, where you can join an online room,
post messages to the room, and have others in the same room
see those messages immediately.

In this tutorial we will build a simple chat server. It will have two pages:

    An index view that lets you type the name of a chat room to join.
    A room view that lets you see messages posted in a particular chat room.

The room view will use a WebSocket to communicate with the Django server and
listen for any messages that are posted.

