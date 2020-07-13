from django.conf.urls import url

from sku.controllers.controller import getCategories, getSubCategory,getProducts,getProductSubCategory,newproduct,getAllProducts

urlpatterns = [
    url('getcategories/$', getCategories),
    url('getsubcategory/$', getSubCategory),
    url('listproducts/$', getProducts),
    url('listproductssubcatagory/$', getProductSubCategory),
    url('addproduct/$', newproduct),
    url('getallproducts/$', getAllProducts),

]
