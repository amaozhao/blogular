# coding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from taggit.models import Tag


class FriendShipManager(models.Manager):

    def get_following(self, user):
        """Get the `user's following users."""
        return self.filter(from_user=user)

    def get_followed(self, user):
        """Get the `user's followed users."""
        return self.filter(to_user=user)


@python_2_unicode_compatible
class FriendShip(models.Model):

    """ Model to represent Friendships """
    to_user = models.ForeignKey(User, related_name='to_user')
    from_user = models.ForeignKey(User, related_name='from_user')
    created = models.DateTimeField(auto_now_add=True)

    objects = FriendShipManager()

    class Meta:
        verbose_name = _('Friend')
        verbose_name_plural = _('Friends')
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return "User #%s is following #%s" % (self.from_user, self.to_user)

    def save(self, *args, **kwargs):
        # Ensure users can't be friends with themselves
        if self.to_user == self.from_user:
            raise ValidationError("Users cannot be friends with themselves.")
        super(FriendShip, self).save(*args, **kwargs)


@python_2_unicode_compatible
class FollowingTag(models.Model):
    author = models.ForeignKey(User, related_name='followingtags')
    tags = models.ManyToManyField(
        Tag, related_name='tags', blank=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = _('FollowingTag')
        verbose_name_plural = _('FollowingTag')
