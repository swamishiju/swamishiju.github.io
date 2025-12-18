---
Title: GSoC 2025 Week 6
Date: June 29,2025
Tags: Open Source, Compiler Design
Abstract:
Week-6 Progress Report for GSoC 2025
---

## Weekly Agenda

This week was focused on Union type features. 
First was to implement the access syntax for Union types
and to do a refactor of the ASR structure of Union types.

The access was quick to implement. However, the ASR refactor
encountered a major blocker: it depends on the StructType 
refactor PR. As of the time of this report, the Union type
PR remains in draft status.

## Achievements

- Implemented Union type access
- Union ASR type refactor

## Code Samples

```f90
program lp_test
    type:: test_type
        integer :: x
        real    :: y
    end type

    type(test_type)  :: test_union

    ! Memory value of pi
    test_union%x = 1078530011 

    ! Doesn't currently support direct operations
    x = test_union%y
    if ( abs(x - 3.141593) > eps ) error stop

end program
```
            
## Pull Requests

- [#7935 Union access implemented](https://github.com/lfortran/lfortran/pull/7935)
- [#7966 Union ASR Refactor](https://github.com/lfortran/lfortran/pull/7966)

## Goals for next week

The main goal for next week is get accessing Union elements 
so we robustly test if the memory allocation is proper and
supporting pythonic types inside union.

Other goals include things like fixing failing tests in 
LPython after sync and trying to completely remove the 
reliance on typecodes.
