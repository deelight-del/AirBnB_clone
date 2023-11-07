## AIRBnB clone part 1.

### THE PROJECT.

This project is a collaboration project issued by
ALX/Holberton towards being completely formed as a
seasoned software engineer. It involves the implementation
of the **ALX higher level programming** concepts that involves
Object Oriented Programming with Python. In this project we will
be putting to use the several concepts around data abstraction, data
encapusalation, information hiding and other OOP terms as we use Python
to build a storage engine to storing persistent objects of different
classes, and we build a corresponding console as a play ground for the
built `storage engine`.

### THE CONSOLE (THE COMMAND INTERPRETER).

The console is a single use command line interface that we built to carry out
specific functions and methods that are peculiar to our `storage engine`.
We will be able to create, update and destroy different instances of the 
different classes that we build.
It will also be able to execute bash commands using the special `!` symbol before the command.

```bash
! echo commmand
```


The console built inherits from the Python `cmd.Cmd` class.
#### How to start the console.

The following code are workable on a UNIX machine - Implement the variant of the code based on the 
instruction, using your machine specific syntax.


1. Clone the repository to your machine.

```bash
git clone <address>
```

2. Change into cloned repository.
```bash
cd AirBnB_clone
```

3. Run the console.py script.
```bash
./console.py
```

OR USE

```bash
python -m console.py
```

#### EXAMPLES.
...
