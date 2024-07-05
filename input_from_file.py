h_file = None

def init_file(filename):
    global h_file
    h_file = open("./inputs/{0}.txt".format(filename), "r")

def input():
    return h_file.readline().rstrip()

# from input_from_file import init_file, input
# init_file("")