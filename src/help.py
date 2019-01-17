
Options=\
    {'i':'Input Files.',
     'w':'Generate WCET for the file imported.',
     's':'Generate ALF for every statement that fit SWEET.',
     'b':'Generate ALF for every OpenMP task.',
     'h':'Show Help.'
    }


def ShowOptions():
    if __name__ == '__main__':
        print('Please run in main module.')
    else:
        for key in Options:
            print('-'+key+' '+Options[key])