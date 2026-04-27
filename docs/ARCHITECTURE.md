# Architecture & Design Patterns

This document outlines the engineering principles and patterns utilized in the development of `CoolCompiler`.

## 1. Design Patterns Used

### Visitor Pattern (`interpreter.py`)
- **Purpose:** Decouples the data structure (the AST) from the algorithms that operate on it (Execution logic).
- **Benefit:** Allows us to add new operations (like a Linter or a Formatter) without modifying the Node classes themselves.

### Composite Pattern (`nodes.py`)
- **Purpose:** Represents the hierarchy of the language. Both simple leaves (Numbers) and complex branches (Binary Operations) are treated as `Nodes`.
- **Benefit:** Simplifies tree traversal and allows for infinite nesting of expressions.

### Memento / State Pattern (`Environment` class)
- **Purpose:** Used in function calls to capture the "Global" state, swap to a "Local" state, and restore the original state upon function return.
- **Benefit:** Prevents variable leakage and correctly implements local scoping.

## 2. SOLID Principles Applied

- **Single Responsibility (SRP):** Each file has one job. The Lexer does not know about grammar; the Parser does not know about math; the Interpreter does not know about strings.
- **Open-Closed Principle (OCP):** The system is designed to be "Open for Extension." Adding a new feature (like a `while` loop) involves adding a new Node and a Visitor method, without breaking existing logic.
- **Dependency Inversion (DIP):** High-level execution logic relies on the `Node` abstraction rather than concrete implementations.

## 3. The Symbol Table
We implement the Symbol Table as a **Chain of Responsibility**. If a variable is not found in the current scope, the lookup request is passed to the "Parent" environment until it either finds the value or reaches the Global scope.
