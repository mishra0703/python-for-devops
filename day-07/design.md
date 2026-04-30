# Day 07 – Thinking Before Coding (DevOps Mindset)


### We took Day-06 python file to analyze it and understand how to work on it properly

---

###  - What is the problem?

**Problem**  : We don't know about how to convert python to a CLI (Command Line Interface) , means running a python file but more like a script by giving command line arguments 
`python file.py --file Input_file --out Output_file`
- So we have to first learn it what it is and how it can be used 
- Then we have to use it in our code 

---

###  - What input does it need?

**Input** : The script need a log file and output filename as input through arguments , also if we want to add any other argument we have to give that input as well like filtering ERROR only or WARNING only lines etc.. 

---

###  - What output should it give?

**Output** : On terminal and in a file it should give the same output which is a summary report of a log file that gives summary of how many errors/warnings and other messages we got in that log file but , our main focus is to learning `argparse` what it is and how it can be used if we learn correctly then only we get the output  

---

###  - What steps are involved?

**Steps** :  
- As we don't know about the tool we have to use or never studied about this. So, first of all we should read the Readme.md file thoroughly so that we can see the hints or any suggestions about how to explore about the tool we need to use 
- If we didn't get anything from that file then we will google about it like "how to convert a python file to CLI" , we will get the name of the library we have to use and then we can go to the docs to read about it more and understand it better
- Then we will see some examples related to it and try to understand it more and more 
- Then we will do some practice by using it , even by copy pasting the code but we will try to understand it step by step like which step does what thing and then what happend everything about it 
- Then we will use it in our main code and try to run it , if we will get errors we will try to debug it using `pdb` library and if still we face issues only then we will take the code to claude or gpt and try to know our mistakes 
- Then we will fix our issues in the code and get the success by running the file properly and getting the desired output   