from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ThoughtEntrySerializer, MessageEntrySerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import ThoughtEntry, MessageEntry
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse("Welcome to the backend API!")

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "is_superuser": user.is_superuser,
            "email": user.email,
            # 根据需要添加其他字段
        })


class ThoughtsListCreateView(generics.ListCreateAPIView):
    serializer_class = ThoughtEntrySerializer

    def get_queryset(self):
        # 如果是GET请求，只显示公开的日志
        if self.request.method == 'GET':
            return ThoughtEntry.objects.filter(is_public=True).order_by('-timestamp')
        
        # 如果是POST请求，或者请求者是已认证用户，返回所有日志（以便创建时绑定作者）
        return ThoughtEntry.objects.all()

    def perform_create(self, serializer):
        """
        在创建新日志时，自动将作者设置为当前登录用户。
        """
        # 确保只有已认证用户可以创建
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            # 如果未认证用户尝试创建，抛出权限拒绝异常
            raise PermissionDenied("你必须登录才能发布日志。")

    # 未登录用户可以查看列表
    permission_classes = [AllowAny]


class MessageListCreate(generics.ListCreateAPIView):
    serializer_class = MessageEntrySerializer
    permission_classes = [IsAuthenticated] # 仅登录用户可留言和查看自己的留言

    def get_queryset(self):
        if self.request.user.username == 'admin':
            return MessageEntry.objects.all().order_by('-timestamp')
        return MessageEntry.objects.filter(is_public=True).order_by('-date')
    def perform_create(self, serializer):
        # 自动将发送者设置为当前登录用户
        serializer.save(sender=self.request.user)


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