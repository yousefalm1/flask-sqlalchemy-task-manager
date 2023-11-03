from taskmanager import db

# Define the Category class, representing categories of tasks


class Category(db.Model):
    # Define the structure of the Category table in the database

    # 'id' will be a unique identifier for each category
    id = db.Column(db.Integer, primary_key=True)

    # 'category_name' is a column to store the name of the category
    category_name = db.Column(db.String(25), unique=True, nullable=False)

    # 'tasks' is a relationship to the Task model, representing tasks in this category
    tasks = db.relationship("Task", backref="category",
                            cascade="all, delete", lazy=True)

    # __repr__ method defines how a Category object should represent itself as a string
    def __repr__(self):
        return self.category_name

# Define the Task class, representing individual tasks


class Task(db.Model):
    # Define the structure of the Task table in the database

    # 'id' will be a unique identifier for each task
    id = db.Column(db.Integer, primary_key=True)

    # 'task_name' is a column to store the name of the task
    task_name = db.Column(db.String(50), unique=True, nullable=False)

    # 'task_description' is a column to store the description of the task
    task_description = db.Column(db.Text, nullable=False)

    # 'is_urgent' is a column to store whether the task is urgent or not
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)

    # 'due_date' is a column to store the due date of the task
    due_date = db.Column(db.Date, nullable=False)

    # 'category_id' is a foreign key column linking tasks to their respective categories
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)

    # __repr__ method defines how a Task object should represent itself as a string
    def __repr__(self):
        return f"{self.id} - Task:{self.task_name} | Urgent:{self.is_urgent}"
