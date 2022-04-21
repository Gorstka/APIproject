from django.db import models


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ("-pub_date",)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="replies",
        null=True,
        blank=True
    )

    class Meta:
        ordering = ("-created",)

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
