# WCET_Generator V2.1
Generate WCET for ALF Statements based on SWEET Tool

Method:  see SWEET manual 4.14
clt : insertsort.clt provided by SWEET manual
std_hll: for 64bit

- How To Use：
>./wctg [.alf]
>chmod a+x wctg       (如果执行不了的话给wctg赋值)

The alf slices folder and wcet time table(.wct) will be generated in folder where your alf file imported.

- unspported:
    - The WCET for Every Statement including "call" replaced with ERROR

>It's only an early version and we will get ready soon.
