---
Title: GSoC 2025 Week 2
Date: June 1,2025
Tags: Open Source, Compiler Design
Abstract:
Week-2 Progress Report for GSoC 2025
---

## Weekly Agenda

The string changes were still happening so a lot work wasn't
done on the LPython frontend, I continued exposing the data
types to the frontend.

A major target for this week was implementing better syntax
and removing the specific hard coded types like
_lfortran_list_integer to better more extensible syntax 
like _lfortran_list(integer).

A major roadblock I faced this week was making the dict 
syntax proper. The changes I made to the parser for list, 
set were relatively minor which I could implement with minimal 
knowledge in Yacc. The dict syntax and tuple which I intend 
to implement next week is much harder to implement and requires
I think bigger changes to the grammar.

## Achievements

- Implemented better syntax for the new declarations
- Implemented declaration for all supported types
- Implemented more intrinsics for lists
- Implemented specific dict type

## Code Samples

After this week code like below now runs on LFortran using
LFortran specific intrinsics which can compile into llvm and
wasm. As an almost immediate benifit of the workflow changes 
nested list could be simply used without any changes to frontend 
or backend.

```f90
program lp_list

    integer :: x
    
    type(_lfortran_list(integer)) :: test_list 
    type(_lfortran_list(real)) :: test_list_1
    type(_lfortran_list(real(4))) :: test_list_2

    call _lfortran_list_reverse(test_list)
    x = _lfortran_list_count(test_list, 4)

    type(_lfortran_set(integer)) :: test_set 
    
    ! Nested lists
    type(_lfortran_list(_lfortran_list(integer))) :: test_nested_list
    type(_lfortran_list(integer)) :: test_list_3 = _lfortran_list_constant(10, 10, 10)


    call _lfortran_list_append(test_nested_list, 
                    _lfortran_list_constant(1, 0, 1, 12, 15, 15))
    call _lfortran_list_append(test_list_3, 16)
    call _lfortran_list_append(test_nested_list, test_list_3)

    x = _lfortran_get_item(_lfortran_get_item(x, 0), 1)


    ! Dicts 
    type(_lfortran_test_dict):: dict_i  ! dict[integer, integer]
    dict_i = _lfortran_dict_constant(1, 2, 2, 5, 3, 7)
    x = _lfortran_len(dict_i)
    x = _lfortran_get_item(dict_i, 2)

    call _lfortran_set_item(dict_i, 3, 5)

    type(_lfortran_test_dict_r):: dict_r ! dict[integer, real]
end program
```
            
## Pull Requests

- [#7529 More List intrinsics](https://github.com/lfortran/lfortran/pull/7529)
- [#7594 Improved syntax](https://github.com/lfortran/lfortran/pull/7594)
- [#7621 Simple dict implementation](https://github.com/lfortran/lfortran/pull/7621)

## Goals for next week

My main goal for next week is going to be implementing
proper syntax and typing for dicts and making all the data
structures usable and function arguments.

Once that is done we can faithfully port almost all LPython 
tests for them into LFortran.
