- [Course](https://frontendmasters.com/courses/programming-language/)
- [Repo](https://github.com/stevekinney/dropbear)
- [Slides](https://static.frontendmasters.com/resources/2019-05-31-build-your-own-programming-language/programming-language.pdf)
- **Compiler**: something that higher -> low level language
- Stages of compiler

1. Parsing: source code -> representation of that code (which can actually be 2 stages)
2. Transformation: source code -> transformation to what compiler wants it to do
3. Generation: transformed representation -> new string of code

- Interpreter: runs the code
- Scheme vs java / python has little keywords, 8 syntactic forms

## Parsing

1. Lexical analysis = lexing = take the big string of code and turn it into tokens
   1. Ex. (add 1 2 (subtract 6 3))) <- numbers, add/sub, ( and ) are each tokens
2. Syntactic analysis:

Lexing

1. Accept string of code
2. Create variable for tracking position, cursor
3. Make array of tokens
4. Write a while loop that iterates through source code input
5. Check each token to see if it matches types
6. Add to array of tokens

AST: https://www.twilio.com/blog/abstract-syntax-trees

Next

- https://astexplorer.net/

1. Lexing: turned code into tokens
2. REPL - evaluate expressions, looking up identifiers, able to run the code now

- What if we wanted to transpile this language?
- Generation = parsing in reverse
- Transpile = into another language, showed dropbear to javascript
-

```js

```
