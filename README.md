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


```bash
vagrant@ubuntu-focal:~/AirBnB_clone$ ./console.py
(hbnb) help
```
`Documented commands (type help <topic>):
========================================

EOF  all  create  destroy  help  printf  quit  show  update`

```bash
(hbnb)
(hbnb) help quit
```
`Quit command to exit the program`

```bash
(hbnb)
(hbnb)
(hbnb) quit
```


```bash
(hbnb) all MyModel
```

** class doesn't exist **

```bash
(hbnb) show BaseModel
```
**instance id missing**

```bash
(hbnb) show BaseModel My_First_Model
```

**no instance found**

```bash
(hbnb) create BaseModel
```
**49faff9a-6318-451f-87b6-910505c55907**


```bash
(hbnb) all BaseModel
```

**["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]**

```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
```
**[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}**

```bash
(hbnb) destroy
```
**class name missing**

```bash
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
```

**[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}**

```bash
(hbnb) create BaseModel
```

**2dd6ef5c-467c-4f82-9521-a772ea7d84e9**

```bash
(hbnb) all BaseModel
```

**["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]**

```bash
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
```

**no instance found**
(hbnb) 
```
