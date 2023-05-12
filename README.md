Banker's Algorithm: Resource Allocation and Deadlock Avoidance

This Python program implements the Banker's Algorithm, a resource allocation and deadlock avoidance algorithm used in operating systems. The algorithm checks if granting a resource 
request will leave the system in a safe state. If the request can be granted and the system remains in a safe state, the algorithm returns a safe sequence of processes.

The program uses numpy for matrix operations and PySimpleGUI for creating a graphical user interface (GUI) to input the required data.

## Dependencies

- Python 3.6 or later
- NumPy
- PySimpleGUI

To install the dependencies, run:

```shell
#pip install numpy PySimpleGUI

## Features

- Input fields for the number of resources, total resources, available resources, and number of processes.
- Input fields for specifying the current allocation matrix and maximum need matrix.
- Input fields for specifying the process requesting resources and the resources requested.
- Determines if the request can be granted and displays the safe sequence if the request is granted.
- Error messages for invalid input.



Example:

Number of resources: 4
Total resources: 6 5 7 6
Available resources: 3 1 1 2
Number of processes: 3
Current allocation (one row per process):
1 2 2 1
1 0 3 3
1 2 1 0
Maximum need (one row per process):
3 3 2 2
1 2 3 4
1 3 5 0
Process requesting resources: 0
Resources requested: 0
Expected output:
The request can be granted.
Safe sequence: 0,1,2
