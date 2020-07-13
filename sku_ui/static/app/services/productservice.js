angular.module('productService',[])

.service('productService',['$http', function($http){

    var  listing = {}

    listing.getProductDetails = function(success, failure){
        $http.get('api/getallproducts/').then(success, failure)
    }


    listing.product = function(product,success,failure){
        $http.post('api/addproduct/',{
            'product' : product.product,
            'subcategory' : product.subcategory,
            'category': product.category,
        }).then(success, failure)

    }

     listing.getSubCatagoryDetails = function(success, failure){
        $http.get('api/getcategories/').then(success, failure)
    }

    return listing;

 }])