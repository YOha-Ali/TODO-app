# Tasks: Todo Console App

**Input**: Design documents from `specs/001-todo-console-app/`

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 Create project structure per implementation plan (`src` and `tests` directories and subdirectories).

---

## Phase 2: Foundational (Blocking Prerequisites)

- [ ] T002 Implement the `Task` class in `src/model/task.py`.
- [ ] T003 Create unit tests for the `Task` class in `tests/unit/test_task.py`.
- [ ] T004 Implement the `TaskManager` class in `src/logic/task_manager.py` with an in-memory list to store tasks.

---

## Phase 3: User Story 1 - Add a new task (Priority: P1)

### Tests for User Story 1
- [ ] T006 [US1] Create unit tests for `add_task` in `tests/unit/test_task_manager.py`.

### Implementation for User Story 1
- [ ] T005 [US1] Implement the `add_task` method in `TaskManager`.
- [ ] T007 [US1] Implement the UI for adding a task in `src/ui/console.py`.

---

## Phase 4: User Story 2 - View all tasks (Priority: P1)

### Tests for User Story 2
- [ ] T009 [US2] Create unit tests for `get_all_tasks` in `tests/unit/test_task_manager.py`.

### Implementation for User Story 2
- [ ] T008 [US2] Implement the `get_all_tasks` method in `TaskManager`.
- [ ] T010 [US2] Implement the UI for viewing tasks in `src/ui/console.py`.

---

## Phase 5: User Story 3 - Update an existing task (Priority: P2)

### Tests for User Story 3
- [ ] T012 [US3] Create unit tests for `update_task` in `tests/unit/test_task_manager.py`.

### Implementation for User Story 3
- [ ] T011 [US3] Implement the `update_task` method in `TaskManager`.
- [ ] T013 [US3] Implement the UI for updating a task in `src/ui/console.py`.

---

## Phase 6: User Story 4 - Delete a task (Priority: P2)

### Tests for User Story 4
- [ ] T015 [US4] Create unit tests for `delete_task` in `tests/unit/test_task_manager.py`.

### Implementation for User Story 4
- [ ] T014 [US4] Implement the `delete_task` method in `TaskManager`.
- [ ] T016 [US4] Implement the UI for deleting a task in `src/ui/console.py`.

---

## Phase 7: User Story 5 - Mark a task as complete/incomplete (Priority: P2)

### Tests for User Story 5
- [ ] T018 [US5] Create unit tests for `toggle_task_completion` in `tests/unit/test_task_manager.py`.

### Implementation for User Story 5
- [ ] T017 [US5] Implement the `toggle_task_completion` method in `TaskManager`.
- [ ] T019 [US5] Implement the UI for marking a task as complete/incomplete in `src/ui/console.py`.

---

## Phase 8: Main Application

- [x] T020 Implement the main application loop in `src/main.py` to display the menu and handle user input.
