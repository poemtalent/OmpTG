import os
import re as r
import sys
# lis=['{ func   { label 64 { lref 64 "Circle" } { dec_unsigned 64 0 } }   { arg_decls }   { scope    { decls     { alloc 64 "%i.0" 32 }       { alloc 64 "%tmp4" 32 }      }    { inits }    { stmts          { label 64 { lref 64 "Circle::bb" } { dec_unsigned 64 0 } }          { store { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } with { dec_unsigned 32 0 } }     { label 64 { lref 64 "Circle::bb::0:::1" } { dec_unsigned 64 0 } }     { jump { label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } } leaving 0 }          { label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } }          { switch      { s_lt 32 { load 32 { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } } { dec_unsigned 32 100 } }      { target { dec_signed 1 { minus 1 } } { label 64 { lref 64 "Circle::bb2" } { dec_unsigned 64 0 } } }      { default { label 64 { lref 64 "Circle::bb5" } { dec_unsigned 64 0 } } }     }          { label 64 { lref 64 "Circle::bb2" } { dec_unsigned 64 0 } }          { jump { label 64 { lref 64 "Circle::bb3" } { dec_unsigned 64 0 } } leaving 0 }          { label 64 { lref 64 "Circle::bb3" } { dec_unsigned 64 0 } }          { store { addr 64 { fref 64 "%tmp4" } { dec_unsigned 64 0 } } with      { add 32 { load 32 { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } } { dec_unsigned 32 1 } { dec_unsigned 1 0 } }     }          { label 64 { lref 64 "Circle::bb3::1" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%tmp4" } { dec_unsigned 64 0 } } } }     { label 64 { lref 64 "Circle::bb3::1:::1" } { dec_unsigned 64 0 } }     { jump { label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } } leaving 0 }          { label 64 { lref 64 "Circle::bb5" } { dec_unsigned 64 0 } }          { return }    }   }  }']
def getFunction_declaration(list):
    dict={}
    for i in range(0,len(list)):
        string = list[i]
        note_e='label'
        start_place=string.find(note_e)
        start_place=string.find(note_e,start_place+4)
        end_place=0
        for j in range(0,start_place):
            if string[start_place-j]=='{':
                end_place=start_place-j
                break
        note_namel='"'
        start_p=string.find(note_namel)
        end_p=string.find(note_namel,start_p+1)
        note_name=string[start_p+1:end_p]
        dict[note_name] = string[0:end_place]
        list[i] = string[end_place:]

    return dict

# print(getFunction_declaration(lis))
# print(lis)
