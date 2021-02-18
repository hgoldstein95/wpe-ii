# WPE-II Outline

## Papers

1. A Functional Abstraction of Typed Contexts, O. Danvy and A. Filinski
2. Comprehending Monads, Wadler

## Thesis

Delimited continuations and monads are closely connected abstractions: they can solve many of the
same programming problems, and their meta-theories intersect in non-trivial ways.

- Closely connected
  - Programming
    - First-class continuations can implement common monads
    - Monads can capture continuations
  - Meta-theory
    - The CBV translation of a simply-typed lambda calculus into the continuation monad yields the
      standard (and extended?) continuation-passing style translation
    - Both continuations and monads are powerful tools for reasoning about non-trivial denotational
      semantics

## Outline

- Introduction
- Notation
- Danvy and Filinski
- Wadler
- Connection
  - Programming
  - Meta-theory
- Conclusion

## Introduction Outline

- Set up delimited continuations and monads with an example
- What are delimited continuations?
  - Continuations historically
  - Shift/reset (intro Danvy and Filinski)
- What are monads?
  - Monads historically
  - Monad comprehensions (intro Wadler)
- Both delimited continuations and monads are useful for programming (unpack example from before)
- Contributions / outline
  - Explain WPE-II
  - Present thesis
