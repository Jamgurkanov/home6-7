CREATE_TASKS = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    created_at TEXT NOT NULL
);
"""

INSERT_TASKS = """
INSERT INTO tasks (task, created_at) VALUES (?, ?)
"""

SELECT_TASKS = """
SELECT id, task, created_at FROM tasks
"""

UPDATE_TASKS = """
UPDATE tasks SET task = ? WHERE id = ?
"""

DELETE_TASKS = """
DELETE FROM tasks WHERE id = ?
"""
