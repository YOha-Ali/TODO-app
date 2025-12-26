# Data Model for Todo Console App

## Task Entity

This entity represents a single to-do item in the application.

### Fields

-   `id` (integer): A unique identifier for the task. This will be an auto-incrementing integer.
-   `title` (string): The title of the task. This field is mandatory.
-   `description` (string): A detailed description of the task. This field is optional.
-   `completed` (boolean): The completion status of the task. Defaults to `False`.

### Relationships

The `Task` entity has no relationships with other entities.

### State Transitions

A `Task` can be in one of two states:
-   Incomplete (`completed = False`)
-   Complete (`completed = True`)

The `mark as complete/incomplete` feature will toggle the `completed` field.
