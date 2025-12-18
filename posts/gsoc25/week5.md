---
Title: GSoC 2025 Week 5
Date: June 22,2025
Tags: Open Source, Compiler Design
Abstract:
Week-5 Progress Report for GSoC 2025
---

## Weekly Agenda

This week was spent refactoring the old backend for the
python types to have less reliance on functionality that 
we plan to phase out like the type_code design and the
create_gep function. This would make the backend more robust
and support the new type changes being worked on for LFortran.

I also parallelly started work on Union types as part of my 
original proposal.

## Achievements

- Some misc fixes in tuple backend
- Fixed support string type keys for dicts
- Heavily optimized list pop
- Exposed union type to LFortran frontend
- Refactored backed for less reliance on create_gep, typecode
- Successfully merged a month long sync PR for LPython

## Code Samples

```f90
program lp_test

    integer :: x
    _lfortran_tuple(integer, integer)                                                :: t1
    _lfortran_tuple(integer, integer)                                                :: t2
    _lfortran_tuple(_lfortran_tuple(integer, integer),_lfortran_tuple(integer, integer), &
      _lfortran_tuple(integer, integer),_lfortran_tuple(integer, integer))           :: t3

    _lfortran_dict(_lfortran_tuple(integer, integer), _lfortran_tuple(real, real))   :: d1

    t1 = _lfortran_tuple_constant(-1, -2)
    t2 = _lfortran_tuple_constant(-3, -4)
    t3 = _lfortran_tuple_constant(t1, t2, t1, t2)

    if ( .not. _lfortran_eq(_lfortran_get_item(t3, 0), t1) ) error stop


    type:: test_type
        integer :: x
        real    :: y
    end type

    _lfortran_union_type :: test_type1 
        integer :: x
        real    :: i
        type(test_type) :: y
    end _lfortran_union_type


    _lfortran_union_type :: test_type2 
        integer :: x
        real    :: i
        type(test_type) :: y
    end _lfortran_union_type


    type(test_type) :: t_ty
    type(test_type1) :: t_ty1
    type(test_type2) :: t_ty2

end program
```
            

## Optimization Benchmark

Test Code
```f90
program test
    implicit none
    _lfortran_list(integer):: x
    integer:: i, g
        do i = 1, 100000
    call _lfortran_list_append(x, i)
    end do

    do i = 1, 100000
        g = _lfortran_pop(x, 0)
    end do
end program test
```
 
```sh
#! bin/bash
# Pre-optimization

time lfortran test.f90
# 17.23s
time lfortran test.f90 --fast
# 0.91s


# Post-optimization

time lfortran test.f90
# 0.93s
time lfortran test.f90 --fast
# 0.92s
```

## Pull Requests

- [#7873 Misc fixes for tuple types](https://github.com/lfortran/lfortran/pull/7873)
- [#7896 Implemented support for string key in dict type](https://github.com/lfortran/lfortran/pull/7896)
- [#7898 Optimized list pop](https://github.com/lfortran/lfortran/pull/7898)
- [#7901 Refactored backend for less reliance on typecodes](https://github.com/lfortran/lfortran/pull/7901)
- [#7909 Exposed the Union type to LFortran](https://github.com/lfortran/lfortran/pull/7909)
- [#7912 Refactored backend for less reliance on create_gep](https://github.com/lfortran/lfortran/pull/7912)
- [#2840 Syncing LPython to latest libasr](https://github.com/lcompilers/lpython/pull/2840)

## Goals for next week

The main goal for next week is get accessing Union elements 
so we robustly test if the memory allocation is proper and
supporting pythonic types inside union.

Other goals include things like fixing failing tests in 
LPython after sync and trying to completely remove the 
reliance on typecodes.
