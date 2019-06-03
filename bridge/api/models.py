from django.db import models


class Keyword(models.Model):
    word = models.TextField()

    def __str__(self):
        return f"{self.word}"


class Author(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"


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
        return (
            f"Posted: {self.posted} Author: {self.author}"
            f"Platform: {self.platform}"
        )
