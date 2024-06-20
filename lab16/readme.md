
# Лабораторна робота №16: Advanced TODO List<br>
**Мета роботи:** Розробити клас `Task` для управління завданнями, та клас `Schedule` для управління списком завдань з різними функціональними можливостями, такими як сортування, фільтрація, збереження та завантаження завдань.

**Завдання:**<br>
> Створити клас `Task` з атрибутами: назва, опис, дата виконання.

> Додати метод `is_due_today()` до класу `Task`.

> Створити клас `Schedule` для управління завданнями.

> Додати метод `list_overdue_tasks()` до класу `Schedule`.

> Додати метод `list_tasks_due_today()` до класу `Schedule`.

> Додати метод `sort_tasks_by_due_date()` до класу `Schedule`.
 
> Додати метод `update_task()` до класу `Schedule`.
 
> Додати атрибут `status` до класу `Task`.
 
> Додати метод `weekly_schedule()` до класу `Schedule`.
 
> Додати метод `monthly_schedule()` до класу `Schedule`.
 
> Додати атрибут `priority` до класу `Task`.
 
> Додати метод `list_tasks_by_priority()` до класу `Schedule`.
 
> Додати метод `save_to_file()` до класу `Schedule`.
 
> Додати метод `load_from_file()` до класу `Schedule`.
 
> Додати атрибут `notes` до класу `Task`.
 
> Додати метод `list_tasks_with_notes()` до класу `Schedule`.
 
> Додати метод `mark_as_completed()` до класу `Schedule`.
 
> Додати метод `list_completed_tasks()` до класу `Schedule`.
 
> Додати метод `find_task_by_keyword()` до класу `Schedule`.
 
> Додати метод `check_deadlines()` до класу `Schedule`.

> Додати метод `list_all_tasks()` до класу `Schedule`.

> Додати атрибут `duration` до класу `Task`.

> Додати метод `list_tasks_by_duration()` до класу `Schedule`.

> Додати метод `task_history()` до класу `Schedule`.

> Додати метод `clear_completed_tasks()` до класу `Schedule`.

> Додати атрибут `recurrence` до класу `Task`.

> Додати метод `list_recurring_tasks()` до класу `Schedule`.

> Додати метод `set_reminder()` до класу `Schedule`.

> Додати метод `completion_percentage()` до класу `Schedule`.

> Додати атрибут `dependencies` до класу `Task`.
**Виконання роботи:**
Кожне завдання було реалізовано окремою функцією. Для перевірки правильності роботи функцій використовувалися тестові випадки.

**Використання:**<br>

``` Python
from datetime import datetime, timedelta

task1 = Task(
    title="Buy groceries",
    description="Milk, Bread, Eggs",
    due_date=datetime(2024, 6, 21),
    status='incomplete',
    priority='high',
    notes="Remember to check for discounts",
    duration=2,
    recurrence="weekly"
)

task2 = Task(
    title="Submit assignment",
    description="Math assignment",
    due_date=datetime(2024, 6, 20),
    status='incomplete',
    priority='medium'
)

print(task1.is_due_today())  # False, якщо сьогодні не 2024-06-21

schedule = Schedule()

schedule.add_task(task1)
schedule.add_task(task2)

overdue_tasks = schedule.list_overdue_tasks()
for task in overdue_tasks:
    print(f"Overdue: {task.title}")

tasks_due_today = schedule.list_tasks_due_today()
for task in tasks_due_today:
    print(f"Due today: {task.title}")

schedule.sort_tasks_by_due_date()
for task in schedule.tasks:
    print(f"Task: {task.title}, Due Date: {task.due_date}")

schedule.update_task("Buy groceries", description="Milk, Bread, Eggs, Cheese", due_date=datetime(2024, 6, 22))

task1.status = "completed"
print(task1.status)  # completed

start_date = datetime(2024, 6, 19)
weekly_tasks = schedule.weekly_schedule(start_date)
for task in weekly_tasks:
    print(f"Weekly Task: {task.title}")

monthly_tasks = schedule.monthly_schedule(2024, 6)
for task in monthly_tasks:
    print(f"Monthly Task: {task.title}")

print(task1.priority)  # high

high_priority_tasks = schedule.list_tasks_by_priority("high")
for task in high_priority_tasks:
    print(f"High Priority Task: {task.title}")

schedule.save_to_file("schedule.json")

new_schedule = Schedule()
new_schedule.load_from_file("schedule.json")

print(task1.notes)  # Remember to check for discounts

tasks_with_notes = schedule.list_tasks_with_notes()
for task in tasks_with_notes:
    print(f"Task with notes: {task.title}")

schedule.mark_as_completed("Submit assignment")

completed_tasks = schedule.list_completed_tasks()
for task in completed_tasks:
    print(f"Completed Task: {task.title}")

found_tasks = schedule.find_task_by_keyword("assignment")
for task in found_tasks:
    print(f"Found Task: {task.title}")

tasks_with_deadlines = schedule.check_deadlines()
for task in tasks_with_deadlines:
    print(f"Task due soon: {task.title}")

all_tasks = schedule.list_all_tasks()
for task in all_tasks:
    print(f"All Tasks: {task.title}")

print(task1.duration)  # 2 години

tasks_by_duration = schedule.list_tasks_by_duration(1, 3)
for task in tasks_by_duration:
    print(f"Task by duration: {task.title}")

task_history = schedule.task_history()
for entry in task_history:
    print(f"Task history: {entry}")

schedule.clear_completed_tasks()

print(task1.recurrence)  # weekly

recurring_tasks = schedule.list_recurring_tasks()
for task in recurring_tasks:
    print(f"Recurring Task: {task.title}")

schedule.set_reminder("Buy groceries", datetime(2024, 6, 20))

completion_percentage = schedule.completion_percentage()
print(f"Completion Percentage: {completion_percentage}%")

task3 = Task(
    title="Prepare breakfast",
    description="Use groceries to prepare breakfast",
    due_date=datetime(2024, 6, 22),
    dependencies=[task1]
)
print(task3.dependencies)  # [task1]

```
**Резульятати:** Створено класи Task та Schedule.
Додано методи для управління завданнями.
Тестування методів показало, що вони працюють згідно з очікуваннями.

**Висновки:** Мета роботи була досягнута. В процесі виконання були виявлені деякі помилки, які були успішно вирішені шляхом додавання додаткових перевірок і тестування коду.

**Інструкції з запуску:**
> Вимоги до середовища: Python 3.<br>
> Необхідні бібліотеки: всі необхідні бібліотеки є стандартними для Python 3.
