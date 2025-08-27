from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ThoughtEntrySerializer, MessageEntrySerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import ThoughtEntry, MessageEntry

# Create your views here.


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class OwnerThoughtsList(generics.ListAPIView):
    serializer_class = ThoughtEntrySerializer

    def get_queryset(self):
        return ThoughtEntry.objects.all()


class MessageListCreate(generics.ListCreateAPIView):
    serializer_class = MessageEntrySerializer
    permission_classes = [IsAuthenticated] # 仅登录用户可留言和查看自己的留言

    def get_queryset(self):
        if self.request.user.username == 'admin':
            return MessageEntry.objects.all.order_by('-date')
        return MessageEntry.objects.filter(is_public=True).order_by('-date')
    def perform_create(self, serializer):
        # 自动将发送者设置为当前登录用户
        serializer.save(sender=self.request.user)

# 前端发布日志（POST）
class ThoughtsCreate(generics.CreateAPIView):
    serializer_class = ThoughtEntrySerializer
    permission_classes = [IsAuthenticated]  # 仅登录用户可发布

    def perform_create(self, serializer):
        # 自动绑定作者为当前登录用户
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            raise serializers.ValidationError("数据出错了哦，不能保存。")

class NoteDelete(generics.DestroyAPIView):
    serializer_class = ThoughtEntrySerializer
    permission_classes = [IsAuthenticated]  # 仅登录用户可删除

    def get_queryset(self):
        user = self.request.user 
        return ThoughtEntry.objects.filter(author=user)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("不可以删除别人写的东西嘞。")
        instance.delete()