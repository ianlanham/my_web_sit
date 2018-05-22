from django.db import models

# Create your models here.

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    email = models.EmailField('email')

class Person(models.Model):
    male = 'M'
    female = 'F'
    
    choice_gender = (
                    (male, 'Male'),
                    (female, 'Female'),
                    )
    
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    nationalid = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email  = models.EmailField('email')
    address = models.CharField(max_length=200)
    
    gender = models.CharField(
        max_length=1,
        choices=choice_gender,
        default=female,
    )
    dob = models.DateTimeField('date of birth')

class Student(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)


class Legal_Rep(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)


class Payment(models.Model):
    value = models.IntegerField(default=0)
    currency = models.CharField(max_length=10)
    payment_made = models.DateTimeField('date when payment made to legal rep')
    
class Attendance(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_lessons = models.DateTimeField('date/time started lessions')
    finish_lessions = models.DateTimeField('date/time finished lessions')
     