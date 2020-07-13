import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder


from sku.services.services import productService



@api_view(['GET'])
def getCategories(request):
    productService_obj = productService()
    result = productService_obj.listCategories()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def getSubCategory(request):
    catagory_id=request.GET['id']
    productService_obj = productService()
    result = productService_obj.listSubcategory(catagory_id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



@api_view(['GET'])
def getProducts(request):
    catagory_id=request.GET['id']
    productService_obj = productService()
    result = productService_obj.listProducts(catagory_id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def getProductSubCategory(request):
    sub_catagory_id=request.GET['id']
    productService_obj = productService()
    result = productService_obj.listProductsSubcategoty(sub_catagory_id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['POST'])
def newproduct(request):
    product_name = request.data['product']
    category_id = request.data['category']
    sub_catagory_id=request.data['subcategory']
    productService_obj = productService()
    result = productService_obj.addProduct(product_name,category_id,sub_catagory_id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def getAllProducts(request):
    productService_obj = productService()
    result = productService_obj.listAllProducts()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

