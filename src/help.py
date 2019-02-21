
Options=\
    {'i':'Input Files.',
     'w':'Generate WCET for the file imported.',
     't':'Generate ALF for every OpenMP task that fit SWEET.',
     'h':'Show Help.'
    }


def ShowOptions():
    if __name__ == '__main__':
        print('Please run in main module.')
    else:
        for key in Options:
            print('-'+key+' '+Options[key])