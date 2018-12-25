from django.db import models

# Create your models here.

class Home (models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home')
    message = models.TextField()

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"

    def __str__(self):
        return self.title
class About_message(models.Model):
    description = models.TextField()


    class Meta:
        verbose_name = "About Description"
        verbose_name_plural = "About Description"

    def __str__(self):
        return self.description


class Core_value(models.Model):
    image = models.ImageField(upload_to='values')
    description = models.TextField()

    class Meta:
        verbose_name = "Core Value"
        verbose_name_plural = "Core Values"

    def __str__(self):
        return self.description

class Expertise (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Expertise"
        verbose_name_plural = "Expertises"

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    names = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Testimonial')
    testimony = models.TextField()

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.names

class Team (models.Model):
    names = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team')

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Team"

    def __str__(self):
        return self.names

class Contact_info (models.Model):
    info_type = models.CharField(max_length=200)
    info = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.info_type


