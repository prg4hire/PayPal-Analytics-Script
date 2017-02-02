

data is lists of binaries.

opcode, symbol for compiled language, stack changes

# values opcodes
opcode | symbol | stack changes | comment
---| --- | --- | --- 
0  | int |  -- X  | the next 32 bits = 4 bytes are put on the stack as a single binary.
2  | binary |  N -- L  | the next N * 8 bits are put on the stack as a single binary.


# other opcodes
opcode | symbol | stack changes | comment
---| ---   | --- | --- 
10 | print | ( Y -- X ) | prints the top element on stack
11 | crash |    |code stops execution here. Whatever is on top of the stack is the final state.


# stack opcodes
opcode | symbol | stack changes | comment
--- | --- | --- | --- 
20 | drop | X --     | will remove the top element on stack
21 | dup  | X -- X X | duplicates the top element of the stack 
22 | swap | A B -- B A| swaps the top two element of the stack
23 | tuck | a b c -- c a b |  
24 | rot  | a b c -- b c a |
25 | 2dup | a b -- a b a b |
26 | tuckn| X N -- | inserts X N-deeper into the stack.
27 | pickn| N -- X | grabs X from N-deep into the stack.

