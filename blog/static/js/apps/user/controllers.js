'use strict';

angular.module('blog.user.controllers', [])
  .controller('UserListCtrl', ['$scope', '$rootScope', '$http', '$routeParams',
    function($scope, $rootScope, $http, $routeParams) {
    $scope.url = '/api/users/' + $routeParams.id + '/';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
      $rootScope.title = '用户';
    }).error(function(data, status, header, config) {});
  }])
  .controller('AuthCtrl', ['$scope', '$rootScope', '$location', '$http',
    function($scope, $rootScope, $location, $http){
    $scope.message = {};
    $rootScope.title = '用户登陆';
    $scope.signin = function(){
      $scope.url = '/rest-auth/login/';
      $http.post($scope.url, $scope.user).success(function(data, status, header, config){
        $rootScope.authuser = data;
        $location.path('/');
      }).error(function(data, status, header, config) {
        $scope.message = data;
      });
    };

    $scope.hidealert = function(){
      $scope.message = null;
    };
  }]);
