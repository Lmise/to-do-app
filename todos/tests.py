from django.test import TestCase
from .models import Todo


class ModelTestCase(TestCase):
  
    def setUp(self):
        self.todo_name = "write world class code"
        self.todo = Todo(self.name=self.todo_name)

    def test_model_can_create_a_todo(self):
        old_count = Todo.objects.count()
        self.todo.save()
        new_count = Todo.objects.count()
        self.assertNotEqual(old_count, new_count)

