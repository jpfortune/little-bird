from django.db import models


class Keyword(models.Model):
    word = models.TextField()


class Author(models.Model):
    name = models.TextField()


class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    posted = models.DateTimeField()
    author = models.ForeignKey(
        Author, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    platform = models.TextField()
    keywords = models.ManyToManyField(Keyword, blank=True)

    def __str__(self):
        # return f"{self.created} {self.user} {self.platform}"
        return f"{self.created}"


# class Album(models.Model):
#    album_name = models.CharField(max_length=100)
#    artist = models.CharField(max_length=100)
#
#
# class Track(models.Model):
#    album = models.ForeignKey(Album, related_name="tracks", on_delete=models.CASCADE)
#    order = models.IntegerField()
#    title = models.CharField(max_length=100)
#    duration = models.IntegerField()
#
#    class Meta:
#        unique_together = ("album", "order")
#        ordering = ["order"]
#
#    def __str__(self):
#        return "%d: %s" % (self.order, self.title)
