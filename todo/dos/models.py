from django.db import models

class Do(models.Model):
    title = models.CharField(max_length = 128)
    completed = models.BooleanField(default = False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def update_completion(self):
        self.completed = not self.completed