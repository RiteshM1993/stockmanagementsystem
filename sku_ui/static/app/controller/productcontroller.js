angular.module('productCtrl', [])

.controller('productCtrl',['productService','$scope',"$state",function(productService,$scope,$state){

    $scope.getallproduct =function(){
      var success = function(response) {
        console.log("success")
        $scope.productData=response.data.data
        console.log(response.data.data)
    }

      var failure = function(response){
            console.log('failure')
            console.log(response)

    }

     productService.getProductDetails(success,failure)
    }


    $scope.getSubCatagoryCatagotyData =function(){
       var success = function(response) {
        $scope.getSubCatagoryCatagoryData=response.data.data
    }

      var failure = function(response){
            console.log(response)
            console.log('failure')


    }

     productService.getSubCatagoryDetails(success,failure)
    }



    $scope.addProduct = function(){

      var product={
           'product' : $scope.product,
           'subcategory' : $scope.sub_catagory_id,
           'category': $scope.id,
     }

     var success = function(response){
            console.log(response)
            console.log('success')
            $scope.successmsg = true
            $scope.errormsg = false

          $state.go("listProduct")

        }


        var failure = function(response){
            console.log(response)
            console.log('failure')
            $scope.successmsg = false
            $scope.errormsg = true
        }

         productService.product(product,success,failure)


    }

}]);