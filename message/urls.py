# messages/urls.py
from django.urls import path
from .views import MessageListCreateView, MessageUpvoteView, CommentCreateView, LoginView, MessageDeleteView
from .views import MessageUpvoteView

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/upvote/', MessageUpvoteView.as_view(), name='message-upvote'),
    path('messages/<int:message_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('login/', LoginView.as_view(), name='login'),
        path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),
]
