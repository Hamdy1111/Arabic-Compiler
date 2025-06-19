# Arabic Programming Language Compiler

## Description
Designed and developed a custom compiler for an Arabic-script programming language to support Arabic-speaking beginners in learning programming. The compiler implements core phases including lexical analysis, syntax parsing, and semantic validation using Python. It features a user-friendly GUI built with Tkinter that supports Arabic script and displays error messages after code execution. The project is focused on educational use, combining accessibility with fundamental compiler design principles.

## Features
- Lexical analysis, syntax parsing, and semantic validation for Arabic keywords
- Intuitive GUI with Arabic script support
- Error display with descriptive messages
- Optimized for educational use, enabling beginners to learn programming in their native language

## Example Code Snippets

### Variable Declaration
```arabic
متغير ك = 10;
متغير x = 10;
```

### Conditional Statement
```arabic
اذا (x > 5) {
    x = x + 1;
}
```

### Loop Statement
```arabic
طالما (x < 10) { x = x + 1; }
```

### Combined Example
```arabic
متغير x = 10;
اذا (x > 5) {
    x = x + 1;
    طالما (x < 10) { x = x + 1; }
}
```

### More Examples
```arabic
اذا (ك > 5) {
    ك = ك + 1;
}

طالما (x < 10) { x = x + 1; }

طالما (x <= 10) { x = x + 1; }
```

### Incorrect Syntax (Examples that produce errors)
```arabic
طالما (x < 10) x = x + 1;    // ERROR: Missing braces
طالما (x =< 10) { x = x + 1; } // ERROR: Invalid operator
```

## Impact
✔ Increased accessibility for non-English-speaking learners.
✔ Demonstrates NLP and compiler design principles in Python.

## Developer | Tools
- **Language:** Python
- **GUI:** Tkinter
- **Compiler Phases:** Lexical Analysis, Syntax Parsing, Semantic Validation 
