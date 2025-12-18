---
Title: GSoC 2025 Week 1
Date: May 25,2025
Tags: Open Source, Compiler Design
Abstract:
Week-1 Progress Report for GSoC 2025
---

## Introduction

Hey everyone, this is the first of my GSoC'25 blog posts 
while working under LPython: PSF summarizing my weekly work.

Huge thanks to my mentor @certik for being extremely supportive

## Weekly Agenda

The backend of LPython referred to as `libasr` is shared
with LPython's sister project LFortran which is more actively
developed and significantly better tested. Occasionally contributors
to the LPython project need to sync each libasr in the past when 
they were seperate which was an extremely tedious task.

Now we have updated the workflow to use a submodule pointing to 
the LFortran repo which makes it much easier keep LPython's frontend
compliant with the backend.

My original plan was to make LPython functional after the last sync but there was a blocker since LFortran is having major changes to its string type in the backend. So as that is going on I'm going to be implementing python specific data-types like list, set, etc which are present in the backend but not tested for LLVM > 16. Prior to the GSoC acceptance I had fixed these data types for LLVM < 16 after the sync, but we only found out there bugs for higher LLVM version after exposing them in LFortran because of the better test coverage.


## Achievements

- Exposed specific List, Set types to the LFortran frontend
- Fixed bugs that were highlighted from better testing
- Implemented simple related builtins as intrinsics

## Code Samples

Code like below now runs on LFortran using LFortran specific intrinsics which can compile into llvm and wasm.

```f90
program lp_list

    integer :: x
    
    type(_lfortran_list_integer) :: test_list 
    call _lfortran_list_append(test_list, 1)
    x = _lfortran_len(test_list)

    test_list = _lfortran_list_constant(1, 2, 3, 4)

    type(_lfortran_set_integer) :: test_set 
    test_set = _lfortran_set_constant(1, 2, 3, 4, 4, 5, 4, 10)
    call _lfortran_set_add(test_set, 1)         
    x = _lfortran_len(test_set)
    if (x /= 7) error stop

    test_set = _lfortran_set_constant(1, 2, 3, 4)
    call _lfortran_set_add(test_set, -50)
    ! Add other intrinsics later
end program
```
            

## Pull Requests

- [#7419 List implementation](https://github.com/lfortran/lfortran/pull/7419)
- [#7459 Misc PR towards compiling toml-f](https://github.com/lfortran/lfortran/pull/7459)
- [#7462 Set implementation](https://github.com/lfortran/lfortran/pull/7462)
