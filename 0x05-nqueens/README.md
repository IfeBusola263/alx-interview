## N Queens Challenge
Usage:
```
nqueens N
```
If the user called the program with the wrong number of arguments, they get;
```
Usage: 'nqueens N', followed by a new line, and exit with the status 1
```
N must be an integer greater or equal to 4, if N is not an integer, user gets;
```
'N must be a number', followed by a new line, and exit with the status 1
```
If N is smaller than 4, they get
```
N must be at least 4, followed by a new line, and exit with the status 1
```

The program prints every possible solution to the problem one solution per line.
Solutions are not in a specific order, only importing the sys module.
