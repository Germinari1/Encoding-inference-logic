# Logical Sentence Representation and Model Checking

This project provides classes and functions for representing and evaluating logical sentences, as well as performing model checking to determine if a given knowledge base entails a query. This repository also provides some examples of usage of the classes.

## Classes

1. **Sentence** (Abstract Base Class):
  - Defines the common interface for representing logical sentences.
  - Provides methods for evaluating the sentence, generating its formula, and retrieving its symbols.

2. **Symbol**:
  - Represents a propositional symbol in a logical sentence.
  - Supports evaluation, formula generation, and symbol retrieval.

3. **Not**:
  - Represents the negation of a logical sentence.
  - Inherits from `Sentence` and provides methods for evaluation, formula generation, and symbol retrieval.

4. **And**:
  - Represents the conjunction (logical AND) of multiple logical sentences.
  - Inherits from `Sentence` and provides methods for evaluation, formula generation, and symbol retrieval.

5. **Or**:
  - Represents the disjunction (logical OR) of multiple logical sentences.
  - Inherits from `Sentence` and provides methods for evaluation, formula generation, and symbol retrieval.

6. **Implication**:
  - Represents the implication (logical IF-THEN) between two logical sentences.
  - Inherits from `Sentence` and provides methods for evaluation, formula generation, and symbol retrieval.

7. **Biconditional**:
  - Represents the biconditional (logical IF-AND-ONLY-IF) between two logical sentences.
  - Inherits from `Sentence` and provides methods for evaluation, formula generation, and symbol retrieval.

## Functions

1. **model_check(knowledge, query)**:
  - Checks if the given knowledge base entails the query.
  - Uses a recursive algorithm to explore all possible models and determine entailment.

## Usage

1. Create logical sentences using the provided classes (`Symbol`, `Not`, `And`, `Or`, `Implication`, `Biconditional`).
2. Combine these sentences to form a knowledge base and a query.
3. Call the `model_check` function with the knowledge base and query to determine if the knowledge base entails the query.

Example:

```python
# Create logical sentences
A = Symbol("A")
B = Symbol("B")
C = Symbol("C")
knowledge = And(Implication(A, B), Implication(B, C))
query = C

# Check if knowledge base entails query
result = model_check(knowledge, query)
print(result)  # Output: True
