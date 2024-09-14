from django.db import models


from django.contrib.auth.models import User

# Create your models here.
class Master(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True,verbose_name="Active")
    created_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
        abstract = True
        ordering = ['-isactive']

class Transaction(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Course(Master):
    course = models.CharField(max_length=200, unique=True)
    class Meta:
        verbose_name_plural = "Course"
    def __str__(self):
        return self.course

class Day(Master):
	day=models.CharField(max_length=10,unique=True)
	
	class Meta:
		verbose_name_plural = "Day"
	def __str__(self):
		return self.day

class Syllabus(Master):
    syllabus = models.CharField(max_length=200, unique=True,)

    class Meta:
        verbose_name_plural = "Syllabus"

    def __str__(self):
            return self.syllabus

class CourseSyllabus(Transaction):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    day = models.ForeignKey(Day, on_delete=models.CASCADE, null=True, limit_choices_to={"isactive": True})
    syllabus = models.ManyToManyField(Syllabus, blank=True, limit_choices_to={"isactive": True})
    percentage = models.IntegerField()

    def __str__(self):
            return f"Course : {self.course} Day : {self.day}"


