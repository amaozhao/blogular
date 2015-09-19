'use strict';

angular.module('blog.nav.controllers', [])
  .controller('HeaderCtrl', ['$scope', '$rootScope', '$http', '$location',
  function($scope, $rootScope, $http, $location) {
    $scope.auth_url = '/rest-auth/user/';
    $http.get($scope.auth_url).success(function(data, status, header, config){
      if(data && data.username){
        $rootScope.authuser = data;
      };
    }).error(function(data, status, header, config) {});

    $scope.isActive = function(route) {
      return route === $location.path();
    };

    $scope.signout = function(){
      $http.post('/rest-auth/logout/').success(function(data, status, header, config){
        $rootScope.authuser = null;
      }).error(function(data, status, header, config) {});
    };
  }])
  .controller('SidebarCtrl', ['$scope', '$http', function($scope, $http) {
    $scope.recententries_url = '/api/recententries/';
    $http.get($scope.recententries_url).success(function(data, status, header, config){
      $scope.recententries = data;
    }).error(function(data, status, header, config){});

    $scope.recentcomments_url = '/api/recentcomments/';
    $http.get($scope.recentcomments_url).success(function(data, status, header, config){
      $scope.recentcomments = data;
    }).error(function(data, status, header, config){});
  }]);
