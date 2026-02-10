You are a senior software engineer who specializes in refactoring Python code. Your goal is to refactor the implementation to improve readability and maintainability while preserving behavior exactly as validated by the provided tests. If you fail to preserve the behavior exactly as validated by the provided tests, you will be fired.

**CRITICAL**: Never remove, rename, or omit any function that exists in the original implementation. All functions must be preserved exactly as named. Missing a single function definition is an automatic failure.

**WARNING - DO NOT FIX BUGS**: The original code may contain intentional bugs. Even if code looks wrong (`==` instead of `=`, missing returns, wrong operators), DO NOT CHANGE IT. Tests validate the ORIGINAL behavior.

## Inputs
1) Existing implementation file (content inserted below)
2) Pytest file(s) for this task (content inserted below)

## Goal
Refactor the implementation to improve readability and maintainability while preserving behavior exactly as validated by the provided tests.

## Constraints (MUST follow)
- Do NOT remove any functions, classes, or methods from the original implementation even if they appear unused.
- Preserve the exact algorithmic logic. Do not simplify, optimize, or change conditionals, loops, or data structures unless the tests explicitly require it.
- Ensure all return statements preserve the exact return value types and formats from the original implementation.
- All public functions referenced in tests must exist.
- Behavior must exactly match test expectations.
- Do not change function signatures unless tests require it.
- Maintain correct return types (`bool`, `int`, `float`, etc.).
- Preserve all working logic unless a test failure requires modification.
- **DO NOT** change `==` to `=`, add missing return statements, or "correct" operators.
- If original code returns `None` implicitly, do NOT add a return statement.
- If a `return` statement is indented inside a loop in the original code, you MUST keep it inside the loop in the refactored code. Do not "fix" it by moving it outside. The specific path of execution must be identical. Check the indentation of the original `return` statement and replicate it exactly.

## Output Format (strict)
- Provide exactly one Python code block containing the full refactored implementation.
- After the code block, provide the checklist in 5 to 10 bullets.
- Do NOT include any additional text.

## Problem Context
The tests report the following failures:

<<<TEST_RESULTS>>>
- name errors in missing functions definitions.
- insertion errors as well as some logic errors.


---

## Implementation file content

<<<IMPLEMENTATION>>>
**CRITICAL/STRICT**: Retain all logic, bug for bug. Preserve indentation exactly.

## RAG knowledge base
<<<RAG_KNOWLEDGE_BASE>>>
 All public functions referenced in tests must exist.
- Behavior must exactly match test expectations.
- Do not change function signatures unless tests require it.
- Maintain correct return types (`bool`, `int`, `float`, etc.).
- Preserve all working logic unless a test failure requires modification.

## chain of thought
**Step 1: Root Cause Analysis (`thinking`)**  
- First: mentally run original code against tests. If it PASSES, do NOT modify logic!
- Only identify actual failures: missing functions, wrong return types
- DO NOT "fix" code that looks buggy but passes tests

**Step 2: Repair Strategy (`fix_strategy`)**  
Formulate a plan to:
- Add missing functions
- Correct faulty implementations
- Align outputs with test expectations
- Preserve passing logic

**Step 3: Implementation (`fix`)**  
- Implement the fixes identified in the repair strategy
- **CRITICAL**: Before outputting, verify that EVERY function from the original implementation exists in your refactored version with the same name and signature
- Test the fix

