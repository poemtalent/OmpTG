import os
import re as r
import sys
def Delete_Note(list):
    for i in range(0,len(list)):
        string = list[i]
        note_s='/*'
        note_e='*/'
        start_p=0
        end_p=0
        start_place=string.find(note_s)
        while start_place!=-1:
            end_place=string.find(note_e,start_place)
            string=string[:start_place]+string[end_place+2:]
            start_place=string.find(note_s,end_place)
        start_place=string.find(note_s)
        while start_place!=-1:
            end_place=string.find(note_e,start_place)
            string=string[:start_place]+string[end_place+2:]
            start_place=string.find(note_s,end_place)

        list[i]=string
# lis=['{ func   { label 64 { lref 64 "Circle" } { dec_unsigned 64 0 } }   { arg_decls }   { scope    { decls     { alloc 64 "%i.0" 32 } /* Local Variable (PHI node) */      { alloc 64 "%tmp4" 32 } /* Local Variable (Non-Inlinable Instruction) */     }    { inits }    { stmts     /* --------- BASIC BLOCK bb ---------- */     { label 64 { lref 64 "Circle::bb" } { dec_unsigned 64 0 } }     /* STATEMENT Circle::bb::0      *   br label %bb1 */     { store { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } with { dec_unsigned 32 0 } }     { label 64 { lref 64 "Circle::bb::0:::1" } { dec_unsigned 64 0 } }     { jump { label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } } leaving 0 }     /* --------- BASIC BLOCK bb1 ---------- */     { label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } }     /* STATEMENT Circle::bb1::2      *   %tmp = icmp slt i32 %i.0, 100      *   br i1 %tmp, label %bb2, label %bb5 */     { switch      { s_lt 32 { load 32 { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } } { dec_unsigned 32 100 } }      { target { dec_signed 1 { minus 1 } } { label 64 { lref 64 "Circle::bb2" } { dec_unsigned 64 0 } } }      { default { label 64 { lref 64 "Circle::bb5" } { dec_unsigned 64 0 } } }     }     /* --------- BASIC BLOCK bb2 ---------- */     { label 64 { lref 64 "Circle::bb2" } { dec_unsigned 64 0 } }     /* STATEMENT Circle::bb2::0      *   br label %bb3 */     { jump { label 64 { lref 64 "Circle::bb3" } { dec_unsigned 64 0 } } leaving 0 }     /* --------- BASIC BLOCK bb3 ---------- */     { label 64 { lref 64 "Circle::bb3" } { dec_unsigned 64 0 } }     /* STATEMENT Circle::bb3::0      *   %tmp4 = add nsw i32 %i.0, 1 */     { store { addr 64 { fref 64 "%tmp4" } { dec_unsigned 64 0 } } with      { add 32 { load 32 { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } } { dec_unsigned 32 1 } { dec_unsigned 1 0 } }     }     /* STATEMENT Circle::bb3::1      *   br label %bb1 */     { label 64 { lref 64 "Circle::bb3::1" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%tmp4" } { dec_unsigned 64 0 } } } }     { label 64 { lref 64 "Circle::bb3::1:::1" } { dec_unsigned 64 0 } }     { jump { label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } } leaving 0 }     /* --------- BASIC BLOCK bb5 ---------- */     { label 64 { lref 64 "Circle::bb5" } { dec_unsigned 64 0 } }     /* STATEMENT Circle::bb5::0      *   ret void */     { return }    }   }  }']
#
# Delete_Note(lis)
# print(lis)
