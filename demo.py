import sys

def function_1():
    print('hi 1')

def function_2():
    print('hi 2')
def main(args):
    print("Arguments passed to the script:", args)            
    for i in args:
        print(i)
    if(args[0]=='a'):
        function_1()
if __name__ == "__main__":    
    main(sys.argv[1:])
