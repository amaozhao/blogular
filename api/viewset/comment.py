# coding: utf-8
'''
Created on 2015年1月9日

@author: amaozhao
'''

from blog.models import Entry, Comment
from api.serializers.comment import CommentSerializer, RecentCommentSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from api.permissions import ReadOnly
from rest_framework.response import Response


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


class RecentCommentView(ListAPIView):
    model = Comment
    serializer_class = RecentCommentSerializer
    permission_classes = (ReadOnly,)

    def get_queryset(self):
        return Comment.objects.all()[:5]

    def post(self, request, *args, **kwargs):
        return Response({}, status=403)
