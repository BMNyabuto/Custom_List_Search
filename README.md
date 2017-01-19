# Custom_List_Search
Custom_List_Search includes a customised binary search operation in an in-built List structure in Python 2.7.  

#Getting Started
	Custom_List_Search requires a python environment in order to run. In case you do not have python installed in your device, you can download it > https://www.python.org/downloads/
	After your installing and setting up your python environment, open the file with a text editor(prefferebaly: Idle) and then run it.

#Basic Structure
	Custom_List_Search contains one class: BinarySearch, which inherits from the in-built List data structure in Python and initialises it based on the parameters provided.
	After iniatialising this class, the user can then search for the presence of an element across the list created, whereby a dictionary is returned containing the number of
	times the binary search method iterated to find the element alongside its index in the list.

#How to Use
	The function: The BinarySearch Class in Custom_List_Search is a python command line program. The following are some examples that will help you get familiar with its operation.

	1. Initiate the function by importing it into python shell.
			i.e. from Custom_List_Search import BinarySearch.
		
	2. Define two variables: a for the length of array, b for the difference between the elements to be initialised.
			For example, >>> one_to_twenty = BinarySearch(20,1)
						 >>> two_to_forty = BinarySearch(20,2)
					 
	3. Search for an element by paasing the value to be found:
			>>> one_to_twenty.search(16)
			>>> two_to_forty.search(30)

#Python version
	Created in python version 2.7.12