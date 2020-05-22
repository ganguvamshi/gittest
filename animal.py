from __future__ import print_function
import os
import sys

def snake():
    print("Hsssss..")
    

def dog():
    print("Bow Bow..")
    
def cat():
    print("Meeeoww..")
    
def main(type):
    if type=="dog":
        dog()
    elif type =="cat":
        cat()
    elif type=="snake":
        snake()
    else:
        print("Hello")


if __name__=="__main__":
    if len(sys.argv) !=2:
        sys.exit("python %s animalname"%(sys.argv[0]))
    type=sys.argv[1].rstrip()
    main(type)