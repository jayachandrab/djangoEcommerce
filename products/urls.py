

from django.conf.urls import url

from .views import (
ProductListView,
#product_list_view,
#ProducDetailView,product_detail_view,
#ProductFeaturedDetailView,
#ProductFeaturedListView,
ProductDetailSlugView)

urlpatterns = [
          url(r'^$',ProductListView.as_view(),name="list"),
          url(r'^(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view(),name='detail'),
          
           
      
      ]
