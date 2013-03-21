Slaves
======

Classes for multiprocessing calculations

Author: Yuzhanin Denis (CthulhuDen@gmail.com)

Usage: first, import slaves.py.
Then you can create objects of slaves.slaves type initializing them with number of processes for this particular task and function.
Then you will be able to start work of slaves, pause, resume or terminate it.
Also you can add them job (slaves.put(data)) and retrieve results (slaves.get()).
The point is - your slaves (when active) wait for you jobs, take it and apply function which they were initialized with to this data, then putting results in outgoing queue.
