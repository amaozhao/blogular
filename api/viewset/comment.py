# coding: utf-8
'''
Created on 2015年1月9日

@author: amaozhao
'''

from blog.models import Entry, Comment
from api.serializers.comment import CommentSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets


class CommentViewSet(viewsets.ModelViewSet):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    paginate_by = 20

    def perform_create(self, serializer):
        entry_id = int(self.kwargs['entry'])
        serializer.save(
            author=self.request.user,
            entry=Entry.objects.get(id=entry_id)
        )

    def get_queryset(self):
        entry_id = int(self.kwargs['entry'])
        return Comment.objects.filter(entry=entry_id)
