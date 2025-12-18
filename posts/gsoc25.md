---
Listed
Title: GSoC 2025
Date: Aug 19,2025
Tags: Open Source, Compiler Design
Abstract:
I was a part of the Google Summer of Code 2025 Program, contributing
to the LPython project under the ***Python Software Foundation***.
This post serves as a comprehensive collection of my weekly progress
updates, key milestones, challenges overcome, and the final work
report, documenting my GSoC journey.
---

# Google Summer of Code 2025 Final Report

**Student**: Swaminath Shiju <br/> 
**Project**: Expanding OOP capabilities of LPython for porting common CPython modules <br/> 
**Organisation**: Python Software Foundation <br/> 
**Mentor**: [Ondřej Čertík](https://github.com/certik) <br/> 
**Weekly Reports**: [Link to weekly reports](#/blog/weekly_report_79e0f75229)


## Abstract

The original goal was to enhance LPython’s object-oriented 
programming (OOP) capabilities by implementing dunder methods
and supporting non-dataclass imports. However, due to significant
updates in LPython and its shared backend with LFortran, the
project scope was revised during the bonding period in consultation
with my mentor.

The revised objective focused on implementing Python-style container
types (lists, sets, dictionaries, and tuples) in LFortran’s frontend 
and runtime. This effort improved test coverage for Python-specific
backend components, ensured smoother synchronization with LPython’s
libasr backend, and supported a major synchronization cycle.

The project spanned frontend syntax, backend code generation, and
data structure intrinsics.

## Table of Contents

- Final Deliverables
- Timeline Summary
- Current State
- List of Contributions (PRs)
- Future Work
- Learnings
- Acknowledgements

## Final Deliverables

- Implemented and stabilized Python-like container types (list, set, dict, tuple) in LFortran’s frontend and runtime.
- Refactored backend to reduce reliance on deprecated mechanisms and prepared for string/struct changes.
- Introduced and iterated on Union types: syntax, access, and ASR refactor.
- Improved C backend behavior (string arguments, dict copy) and enabled robust unsigned integer support.
- Unblocked and synchronized LPython with latest libasr changes; restored integration tests.

## Timeline Summary

|Week                    |Key Achievements                                    |
|------------------------|----------------------------------------------------|
|Week 01<br/>[25/5-1/6]  |<ul><li>Initial list/set syntax implementation</li> <li>First tests in frontend &amp; runtime</li></ul>|
|Week 02<br/>[1/6-8/6]   |<ul><li>Improved syntax for lists and sets</li> <li>Added for tests to update backend</li></ul>|
|Week 03<br/>[8/6-15/6]  |<ul><li>Fully ported several LPython List tests</li> <li>Proper syntax for dicts and tuples implemented</li></ul>|
|Week 04<br/>[15/6-22/6] |<ul><li>Completely ported all tuple tests &amp; several list tests </li> <li>Simplified syntax for LP types</li> <li>Backend refactoring</li></ul>|
|Week 05<br/>[22/6-29/6] |<ul><li>Fixed string-type keys in dict type</li> <li>Exposed Union type in LF frontend</li> <li>Optimized list.pop</li> <li> Refactored backed for less reliance on create_gep, typecode </li> <li>Successfully merged a month long sync PR for LPython</li></ul>|
|Week 06<br/>[29/6-6/7]  |<ul><li>Implemented Union type access</li> <li>Union ASR type refactor</li></ul>|
|Week 07<br/>[6/7-13/7]  |<ul><li>Fixed Unsigned integer properly in libasr</li> <li>Made progress towards having C-introp working in LP</li></ul>|
|Week 08<br/>[13/7-20/7] |<ul><li> Began work on fixing more complicated bugs in post sync LP</li></ul>|
|Week 09<br/>[20/7-27/7] |<ul><li>Uint in LF frontend</li> <li>Test coverage for Uint</li></ul>|
|Week 10<br/>[27/7-3/8]  |<ul><li>Uncommented several Integration tests in LP</li> <li>Union refactor</li> <li>Fixed list regression after string refactor</li> </ul>|
|Week 11<br/>[3/8-10/8]  |<ul><li> Began work on large scale LP sync after struct and string refactors in LF backend</li></ul>|
|Week 12<br/>[10/8-17/8] |<ul><li>Finishied sync to a large extent</li> <li>Fixed Dict regression after string refactor</li></ul>|

## Current State

- LPython’s continuous integration (CI) supports approximately 200 tests with the latest libasr backend.
- Ported all tuple tests and nearly all list, set, and dictionary tests to LFortran. Most tests affected by the backend string refactoring broke. I fixed list tests and all but one dictionary test fixed.
- Adapted the LPython frontend to align with recent backend refactoring efforts.

## List of Contributions (PRs)

- [#7419 List implementation](https://github.com/lfortran/lfortran/pull/7419)
- [#7459 Misc PR towards compiling toml-f](https://github.com/lfortran/lfortran/pull/7459)
- [#7462 Set implementation](https://github.com/lfortran/lfortran/pull/7462)
- [#7529 More List intrinsics](https://github.com/lfortran/lfortran/pull/7529)
- [#7594 Improved syntax](https://github.com/lfortran/lfortran/pull/7594)
- [#7621 Simple dict implementation](https://github.com/lfortran/lfortran/pull/7621)
- [#7643 List intrinsics/tests - 1](https://github.com/lfortran/lfortran/pull/7653)
- [#7660 List intrinsics/tests - 2](https://github.com/lfortran/lfortran/pull/7660)
- [#7671 List intrinsics/tests - 3](https://github.com/lfortran/lfortran/pull/7671)
- [#7684 Parser changes and Tuple,Dict type](https://github.com/lfortran/lfortran/pull/7684)
- [#7698 Parser Shift/Reduce conflict resolution](https://github.com/lfortran/lfortran/pull/7698)
- [#7763 Implemented tests for new syntax](https://github.com/lfortran/lfortran/pull/7763)
- [#7799 Refactored function names](https://github.com/lfortran/lfortran/pull/7799)
- [#7807 Ported tuple tests](https://github.com/lfortran/lfortran/pull/7807)
- [#7813 Ported dict tests](https://github.com/lfortran/lfortran/pull/7813)
- [#7873 Misc fixes for tuple types](https://github.com/lfortran/lfortran/pull/7873)
- [#7896 Implemented support for string key in dict type](https://github.com/lfortran/lfortran/pull/7896)
- [#7898 Optimized list pop](https://github.com/lfortran/lfortran/pull/7898)
- [#7901 Refactored backend for less reliance on typecodes](https://github.com/lfortran/lfortran/pull/7901)
- [#7909 Exposed the Union type to LFortran](https://github.com/lfortran/lfortran/pull/7909)
- [#7912 Refactored backend for less reliance on create_gep](https://github.com/lfortran/lfortran/pull/7912)
- [#7935 Union access implemented](https://github.com/lfortran/lfortran/pull/7935)
- [#7966 Union ASR Refactor](https://github.com/lfortran/lfortran/pull/7966)
- [#8002 LP type - argument handling in C backend](https://github.com/lfortran/lfortran/pull/8002)
- [#8011 C backend dict-copy fix](https://github.com/lfortran/lfortran/pull/8011)
- [#8034 Support unsigned integer in LF](https://github.com/lfortran/lfortran/pull/8034)
- [#8037 Proper handling of string argument in C backend](https://github.com/lfortran/lfortran/pull/8037)
- [#8055 Unsigned int print fix](https://github.com/lfortran/lfortran/pull/8055)
- [#8132 Fixing list regression after string refactor](https://github.com/lfortran/lfortran/pull/8132)
- [#8149 Uint frontent](https://github.com/lfortran/lfortran/pull/8149)
- [#8301 Sync](https://github.com/lfortran/lfortran/pull/8301)
- [#8359 Fix for dict regression](https://github.com/lfortran/lfortran/pull/8359)
- [#2840 Syncing LPython to latest libasr](https://github.com/lcompilers/lpython/pull/2840)
- [#2862 Fixed unsigned integer tests](https://github.com/lcompilers/lpython/pull/2862)
- [#2863 String arguments fix](https://github.com/lcompilers/lpython/pull/2863)
- [#2866 Sync](https://github.com/lcompilers/lpython/pull/2866)

## Future Work

- Complete LPython synchronization to achieve approximately 300 passing tests, integrating LFortran-specific features as tests to prevent backend changes from breaking LPython.
- Implement dunder methods and non-dataclass imports in LPython, aligning with the original project goals.
- Begin porting additional CPython standard library modules to LPython.
- Benchmark performance using Advent of Code 2025 challenges.

## Learnings

- Before I started committing to the project I had little to no experience with the LLVM toolchain - but along the course of the project I have picked up a good amount of LLVM fundamentals to begin exploring on my own.
- I've learnt how to use tools like lldb to help debug large complex projects
- I've also learnt how to effectively communicate with other open-source contributors in the community.
- With my college semester starting in the final 3–4 weeks of the program, I developed effective time management skills to balance academic responsibilities and project commitments.
- Git version control, bison, flex, conda, mambda etc

## Acknowledgements

Thanks to my mentor Ondřej Čertík, the LFortran/LPython community, and PSF GSoC coordinators for accepting me into this program and providing guidance and reviews throughout the project.
