from django.db import models



class exam(models.Model):

    name = models.TextField()
    examgroup = models.TextField()
    class_no= models.TextField()

class Meta:  
    db_table = "myprojectdata" 


class paper(models.Model):

    question = models.TextField()
    op1 = models.TextField()
    op2 = models.TextField()
    op3 = models.TextField()
    op4 = models.TextField()

    ans = models.TextField()

    point= models.TextField()

    time=models.IntegerField()


    owner = models.ForeignKey("exam", on_delete=models.SET_NULL, null=True)

class login(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password= models.CharField(max_length=50)



