---
Title: GSoC 2025 Week 3
Date: June 8,2025
Tags: Open Source, Compiler Design
Abstract:
Week-3 Progress Report for GSoC 2025
---

## Weekly Agenda

This week I worked on implementing good syntax for dicts 
and tuples, and porting more tests from LPython. The parser 
changes however did reveal a shift/reduce conflict which we 
had missed.

We also have a close to complete port of Lists and several fully ported tests.

## Achievements

- Fully ported several tests from LPython for lists
- Implemented proper syntax for dicts, tuples

## Code Samples

After this week code like below now runs on LFortran using
LFortran specific intrinsics which can compile into llvm
and wasm. 

```f90
program lp_test

    integer :: x
    
    type(_lfortran_list(integer)) :: test_list = _lfortran_list_constant(1, 1, 1, 2)
    test_list = _lfortran_concat(test_list, _lfortran_list_constant(1, 1, 1, 2))

    call _lfortran_list_insert(test_list, 2, 3)
    call _lfortran_list_clear(test_list)

    type(_lfortran_dict(integer, integer(4))):: dict_i
    dict_i = _lfortran_dict_constant(1, 2, 2, 5, 3, 7)

    x = _lfortran_get_item(dict_i, 2)
    call _lfortran_set_item(dict_i, 3, 5)

    type(_lfortran_tuple(integer, real, character(len=:), logical)) :: t1
    t1 = _lfortran_tuple_constant(1, 2.0, "3", .true.)
    x = _lfortran_get_item(t3, 0)
end program
```

## Pull Requests

- [#7643 List intrinsics/tests - 1](https://github.com/lfortran/lfortran/pull/7653)
- [#7660 List intrinsics/tests - 2](https://github.com/lfortran/lfortran/pull/7660)
- [#7671 List intrinsics/tests - 3](https://github.com/lfortran/lfortran/pull/7671)
- [#7684 Parser changes and Tuple,Dict type](https://github.com/lfortran/lfortran/pull/7684)
- [#7698 Parser Shift/Reduce conflict resolution](https://github.com/lfortran/lfortran/pull/7698)

## Goals for next week

There has been some refactoring in the backend regarding 
how types are treated so next week I plan on transitioning
the LPython specific backend code from relying on type_code
to some other way of specifying type.

Another thing is to port remaining tests for the types
including things like list of tuples and such.
