# Rule-Engine-with-AST

## Features
1.Dynamic Rule Creation: Use AST to parse and create conditional rules.
2.Rule Combination: Combine multiple rules into a single AST to minimize redundant checks.
3.Rule Evaluation: Evaluate user data against created rules.
4.Error Handling: Validate input rule strings and handle missing or incorrect data attributes gracefully.
5.Modifiable Rules: Extend rules by adding or modifying existing rule logic.

### System Requirements
Python 3.8+ (Compatible with Python 3.14)
ast and json (standard Python libraries)

## Running the Project
1.Open the project in VS Code.
2.Run the rule.py file or copy the provided code into your Python environment.

# Example rule creation and evaluation
rule1 = "((age > 30 and department == 'Sales') or (age < 25 and department == 'Marketing')) and (salary > 50000 or experience > 5)"
rule2 = "((age > 30 and department == 'Marketing')) and (salary > 20000 or experience > 5)"
combined_ast = combine_rules([rule1, rule2])
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
print(evaluate_rule(combined_ast, data))  # Expected output: True


### API Design
1. create_rule(rule_string)
Input: A string representing a rule.
Output: A Node object representing the AST for the rule.
2. combine_rules(rules)
Input: A list of rule strings.
Output: A combined AST root node.
3. evaluate_rule(node, data)
Input:
node: The root node of the AST.
data: A dictionary containing user attributes.
Output: True if the user data matches the rule, otherwise False

## Database Design
Choice of Database
Postgres or SQLite is recommended for storing rules and user data.
Schema Design
Table 1: rules
id (INT, Primary Key)
rule_text (TEXT)
ast_json (JSON)
Table 2: users
id (INT, Primary Key)
age (INT)
department (VARCHAR)
salary (INT)
experience (INT)

## Contribution Guidelines
Fork the repository.
Create a new feature branch.
Submit a pull request with appropriate descriptions.
Follow PEP8 coding standards.
Include test cases for any new features or bug fixes.

## Additional Fields:
Error Handling: Explained how the system handles invalid rule strings and missing user data.
Contribution Guidelines: How to contribute and what coding standards to follow.
Future Improvements: Ideas for extending the system beyond the current scope, such as adding support for user-defined functions or optimizing the AST further.
License: Information about the licensing for the project.

# Output
True

