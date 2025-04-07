from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        'Автор', User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        'Картинка', upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        'Группа', Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:21]


class Comment(models.Model):
    author = models.ForeignKey(
        'Автор', User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        'Пост', Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Текст')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    user = models.ForeignKey(
        'Подписчик', User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        'Пользователь', User,
        on_delete=models.CASCADE, related_name='following'
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} follows {self.following}'
