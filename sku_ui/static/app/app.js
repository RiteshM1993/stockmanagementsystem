var routerApp = angular.module('skuApp',[
    'ngMaterial',
    'ui.router',
    'smart-table',
    'productCtrl',
    'productService'
    ])


.config(function($stateProvider,$urlRouterProvider){

    $urlRouterProvider.otherwise('listProduct');

    $stateProvider

    .state('listProduct',{
        url: '/listProduct',
        templateUrl: '/static/views/listProduct.html',
        controller: 'productCtrl',
    })

    .state('addproducts',{
        url: '/addproducts',
        templateUrl: '/static/views/addproducts.html',
        controller: 'productCtrl',
    })




});