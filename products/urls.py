from django.urls import path
from .views import Home, ProductDetail, CategoryDetail, ProductCreate, ProductUpdate, ProductDelete, CreateCommentView, \
    CommentUpdate, CommentDelete


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('product/create/', ProductCreate.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDelete.as_view(), name='product_delete'),
    path('product/<int:pk>/comment/', CreateCommentView.as_view(), name='add_comment'),
    path('comment/edit/<int:pk>/', CommentUpdate.as_view(), name='comment_edit'),
    path('comment/delete/<int:pk>/', CommentDelete.as_view(), name='comment_delete')

]

