# WCET_Generator V2.1
Generate WCET for ALF Statements based on SWEET Tool

## Method
- details see SWEET manual 4.14

## Requirement
- python (version 3+)
- sweet

## File Resource
clt : insertsort.clt provided by SWEET manual
std_hll: for 64bit (see SWEET manual)

## How To Use：
> ./wctg [.alf]

Remember to give "wctg" permission to execute. 
> chmod a+x wctg

- The alf slices folder and wcet time table(.wct) will be generated in folder where your alf file imported.

- unspported:
    - The WCET for Every Statement including "call" replaced with ERROR

## It's only an early version and we will get ready soon.
