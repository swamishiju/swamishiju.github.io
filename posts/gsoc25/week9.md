---
Title: GSoC 2025 Week 9
Date: July 20,2025
Tags: Open Source, Compiler Design
Abstract:
Week-9 Progress Report for GSoC 2025
---

## Weekly Agenda

This week I worked on getting the LFortran struct
and string refactors to sync with LPython. I also
implemented a basic uint test in LFortran.

## Achievements

- Uint in LF frontend
- Test coverage for Uint

## Code Samples

```f90
program lp_test
    implicit none

    type(uint) :: x
    x = 1

    do i = 1, 30
        x = x * _lfortran_uint(2)
        y = y * 2
        if ( x < _lfortran_uint(0) ) error stop 
        if ( y < 0 )  error stop 
    end do

    x = x * _lfortran_uint(2)
    if ( x < _lfortran_uint(0) ) error stop 
    x = x * _lfortran_uint(2)
    if ( x /= _lfortran_uint(0) ) error stop 
end program
```
            
## Pull Requests

- [#8132 Fixing list regression after string refactor](https://github.com/lfortran/lfortran/pull/8132)
- [#8149 Uint frontent](https://github.com/lfortran/lfortran/pull/8149)

## Goals for next week

Continue the LPython sync
