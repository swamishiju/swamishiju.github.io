---
Title: GSoC 2025 Week 4
Date: June 15,2025
Tags: Open Source, Compiler Design
Abstract:
Week-2 Progress Report for GSoC 2025
---

## Weekly Agenda

This was mostly spent refactoring the backend code and 
improving the test coverage for the new types.

## Achievements

- Fully ported several tests from LPython for dicts
- Fully ported all tests from LPython for tuples
- Simplified syntax for dicts, tuples
- Refactored back-end code

## Code Samples

This week's work didn't introduce a ton of new syntax 
changes other than taking the new types out of the type intrinsic.

```f90
program lp_test

    _lfortran_list(integer)                                 :: test_list 
    _lfortran_dict(integer, real)                           :: test_dict
    _lfortran_set(integer)                                  :: test_set
    _lfortran_tuple(integer, _lfortran_tuple(integer))      :: test_tuple

end program
```

## Pull Requests

- [#7763 Implemented tests for new syntax](https://github.com/lfortran/lfortran/pull/7763)
- [#7799 Refactored function names](https://github.com/lfortran/lfortran/pull/7799)
- [#7807 Ported tuple tests](https://github.com/lfortran/lfortran/pull/7807)
- [#7813 Ported dict tests](https://github.com/lfortran/lfortran/pull/7813)

## Goals for next week

A main goal for next week is implementing Union types
into LFortran frontend so that we can extensively test 
it. This would go hand in hand with the introduction 
on python types and help us make sync significantly easier.
