from django.db import models


# Create models of University Campus.
class UniversityCampus(models.Model):
    Campus_ID = models.IntegerField(default="", blank=True, null=False)
    Campus_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=5, default="", blank=True, null=False)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the State and Campus Name
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.Campus_ID:} {0.Campus_Name} {0.State}'
        return display_campus.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"