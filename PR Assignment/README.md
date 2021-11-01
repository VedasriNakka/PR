# pattern-recognition-assignment
This project holds the group assignments of the Patttern Recognition course 33082/63082 at the university of Fribourg of the group_1.

Group members: Moro Palma Loris, Vedasri Nakka, Mirko Bristle, Alexandra Kovacs, Michael Brunner

## general setup
1. create virtual environment with python 3.9 as interpreter for running this repo. 
2. make sure pip is installed and run ``` pip install pip-tools```


## update/install packages
1. write the package in the requirements.in file (eg. ```echo $YOUR_NE_PACKAGE_NAME >> requirements.in```)
2. run ```pip-compile```  (for mor info see: [pip-tools](https://github.com/jazzband/pip-tools))
3. install packages ```pip install -r requirements.txt```

## handy notes
 - convert to jupyter to pdf: ```sudo jupyter nbconvert --to pdf 02_MNIST/Serie_02a.ipynb ``
