from django.db import models

# Create your models here.
class StudentClassInfo(models.Model):
    dept_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.dept_name


class StudentSectionInfo(models.Model):
    section_name = models.CharField(max_length=20)

    def __str__(self):
        return self.section_name


class StudentShiftInfo(models.Model):
    shift_name = models.CharField(max_length=100)

    def __str__(self):
        return self.shift_name


class StudentInfo(models.Model):
    academic_year = models.CharField(max_length=100)
    admission_date = models.DateField()
    admission_id = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    dept_name= models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    section_type = models.ForeignKey(StudentSectionInfo, on_delete=models.CASCADE)
    shift_type = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    student_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    qrcode = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fees = models.IntegerField(unique=True)
    level = models.CharField(max_length=100)

    class Meta:
        unique_together = ["admission_id", "dept_name"]

    def __str__(self):
        return self.full_name


class AttendanceManager(models.Manager):
    def create_attendance(self, student_class, student_id):
        student_obj = StudentInfo.objects.get(
            dept_name=student_class,
            admission_id=student_id
        )
        attendance_obj = Attendance.objects.create(student=student_obj, status=1)
        return attendance_obj


class Attendance(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)

    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return self.student.admission_id

        # # for integer field
        # return str(self.student.mothers_nid)
