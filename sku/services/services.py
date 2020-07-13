from sku.models import Category,SubCategory,Product

class productService:
    @classmethod

    def listCategories(cls):
        try:
            listqry = Category.objects.all()
            sublistqry = SubCategory.objects.all()

            categorieslist=[]
            subcategorerylist = []

            for values in listqry:
                categorieslist.append({
                    'id': values.id,
                    'name': values.name,
                })

            for values in sublistqry:
                subcategorerylist.append({

                    "sub_catagory_id":values.id,
                    "sub_catagory_name": values.name,
                    "category":values.category.name,
                })


            return {
                "category" : categorieslist,
                "subcategory" : subcategorerylist,
            }

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    def listSubcategory(cls,catagory_id):
        try:
            listqry = SubCategory.objects.filter(category=catagory_id)

            subcategorieslist=[]

            for values in listqry:
                subcategorieslist.append({
                    'id': values.id,
                    'name': values.name,
                    'category': values.category.name,
                })
            return subcategorieslist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj
    def listProductsSubcategoty(cls,sub_catagory_id):
        try:
            listqry = Product.objects.filter(sub_category=sub_catagory_id)

            productssubcategorieslist=[]

            for values in listqry:
                productssubcategorieslist.append({
                    'id': values.id,
                    'name': values.name,
                    # 'category': values.category.name,
                    'sub_category': values.sub_category.name,

                })
            return productssubcategorieslist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj


    def listProducts(cls,catagory_id):
        try:
            listqry = Product.objects.filter(category=catagory_id)

            subcategorieslist=[]

            for values in listqry:
                subcategorieslist.append({
                    'id': values.id,
                    'name': values.name,
                    'category': values.category.name,
                    'sub_category': values.sub_category.name,

                })
            return subcategorieslist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj
    def addProduct(self,product_name,category_id,sub_catagory_id):
        try:
            catagory_obj = Category.objects.get(id=category_id)
            sub_catagory = SubCategory.objects.get(id=sub_catagory_id)
            product_obj = Product(name=product_name,sub_category=sub_catagory,category=catagory_obj)
            product_obj.save()


            saveqrysuccessobj = {

                "response" : "success"

            }
            return saveqrysuccessobj

        except Exception as err:
            saveqryfailureobj = {

                "response" : "failure"
            }
            return saveqryfailureobj


    def listAllProducts(self):
        try:
            listqry=Product.objects.all()
            productList = []

            for values in listqry:
                productList.append({
                    'id': values.id,
                    'name': values.name,
                    'category': values.category.name,
                    'sub_category': values.sub_category.name,

                })
            return productList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj







