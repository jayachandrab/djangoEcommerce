from django.views.generic import ListView,DetailView
from django.http import Http404
from django.shortcuts import render,get_object_or_404
# Create your views here.
from carts.models import Cart
from .models import Product

class ProductFeaturedListView(ListView):
   
    template_name="products/list.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset= Product.objects.all().featured()

    template_name="products/featured-detail.html"

   # def get_queryset(self,*args,**kwargs):
    #    request=self.request
     #   return Product.objects.featured()


class ProductListView(ListView):
   
    template_name="products/list.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    print("========")
    print(queryset)
    context = {
        'object_list':queryset
    }
    return render(request,"products/list.html",context)

class ProductDetailSlugView(DetailView):
    queryset=Product.objects.all()
    template_name="products/detail.html"

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
        request=self.request
        cart_obj,new_obj=Cart.objects.new_or_get(request)
        context['cart']=cart_obj
        return context
    def get_object(self,*args,**kwargs):
        request = self.request
        slug=self.kwargs.get('slug')
        instance=None
        #instance =get_object_or_404(Product,slug=slug,active=True)
        try:
            instance=Product.objects.get(slug=slug,active=True)
        except Product.DoesNotExist:
            raise Http404("not found product using slug")
        except Product.MultipleObjectsReturned:
            qs=Product.objects.filter(slug=slug,active=True)
            instance=qs.first()
        except:
            raise Http404("hmmmm")
        return instance

class ProducDetailView(DetailView):
    
    print("=========detailview===========")
    queryset=Product.objects.all()
    template_name="products/detail.html"

    def get_object(self,*args,**kwargs):
        request = self.request
        pk=self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("product doesn't exists")
        return instance
    #def get_queryset(self,*args,**kwargs):
     #   request = self.request
    #  pk=self.kwargs.get('pk')
       # return Product.objects.filter(pk=pk)


def product_detail_view(request,pk=None, *args,**kwargs):
    print("=========detailview in fbv===========")
    print(args)
    print(kwargs)
    #instance = Product.objects.get(pk=pk)
    #instance=None
    instance=Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("no product found")
    context = {"object":instance}
   #  try:
        
     #   instance = Product.objects.get(id=pk)
     #   context['object']=instance
    #except Product.DoesNotExist:
      #  print("no product found")
       # raise Http404("Product not found")
   # except:
    #    print("hi")


   # print("========")
   # print(context.get('object')) """
    
    return render(request,"products/detail.html",context)