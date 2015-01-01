'use strict';

angular.module('blog.user.controllers', [])
  .controller('UserListCtrl', ['$scope', '$http', '$location', '$routeParams',
    function($scope, $http, $location, $routeParams) {
    console.log($routeParams.id);
    $scope.url = '/api/entries/';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
    }).error(function(data, status, header, config) {});
  }])
  .controller('AuthCtrl', ['$scope', '$rootScope', '$location', '$http',
    function($scope, $rootScope, $location, $http){
    $scope.message = {};
    $scope.signin = function(){
      $scope.url = '/api/auth/signin/';
      $http.post($scope.url, $scope.user).success(function(data, status, header, config){
        $rootScope.authuser = data.user;
        $location.path('/');
      }).error(function(data, status, header, config) {
        $scope.message = data;
      });
    };

    $scope.hidealert = function(){
      $scope.message = null;
    };
  }]);
