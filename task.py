class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def mark_as_not_completed(self):
        self.completed = False

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Описание: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    def change_task_status(self, description, completed):
        for task in self.tasks:
            if task.description == description:
                if completed:
                    task.mark_as_completed()
                else:
                    task.mark_as_not_completed()
                return True  # Статус задачи успешно изменен
        return False  # Задача с данным описанием не найдена

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def __str__(self):
        if not self.tasks:
            return "Нет задач"
        return "\n".join(str(task) for task in self.tasks)


# Пример использования
task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2024-08-05")
task_manager.add_task("Сдать проект", "2024-08-10")
task_manager.add_task("Позвонить другу", "2024-08-07")

print("Все задачи:")
print(task_manager)

print("\nОтметка задачи как выполненной:")
task_manager.change_task_status("Купить продукты", True)

print("\nТекущие задачи:")
for task in task_manager.get_pending_tasks():
    print(task)

print("\nВсе задачи:")
print(task_manager)

print("\nСнятие отметки о выполнении задачи:")
task_manager.change_task_status("Купить продукты", False)

print("\nВсе задачи:")
print(task_manager)
