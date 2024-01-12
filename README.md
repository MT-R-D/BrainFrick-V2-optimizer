# BrainFrick V2 optimizer

## Explanation

BrainFrick is a fictional language that was based upon the popular esoteric language "Brainfuck", the point of BrainFrick was to have an imaginary language to test and write an optimizer that takes raw BrainFrick code and generates shorter, simpler code that achieves the same result.
Because of the simple nature of BrainFrick, writing the optimizer was a simple task, now we decided to expand the original idea which lead us to designing a new version of BrainFrick and the task of creating an optimizer for BrainFrick V2, as we decided to call it.

## Syntax

Unlike BrainFrick V1 the syntax of BrainFrick V2 does not borrow a lot from "Brainfuck", but the overall idea of having a buffer which the code manipulates still remains.

### The Buffer

The buffer now can be manipulated from any point in the code in the following manner:

[i] represents the slot i in the buffer.

### Operations

(+) add value to slot.

(-) subtract value from slot.

(*) multiply value of slot.

(/) divide slot by value.

(=) assign value to slot.

## Result

The current method calculates the overall change for every slot affected and replaces all actions on a slot with one assignment operator with the final value of teh slot after running the code.
