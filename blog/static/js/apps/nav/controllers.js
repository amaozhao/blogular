'use strict';

angular.module('blog.nav.controllers', [])
  .controller('HeaderCtrl', ['$scope', '$rootScope', '$http',
  function($scope, $rootScope, $http) {
    $scope.auth_url = '/api/auth-user/';
    $http.get($scope.auth_url).success(function(data, status, header, config){
      if(data && data.username){
        $rootScope.authuser = data;
      }
    }).error(function(data, status, header, config) {});

    $scope.find = function(){
      console.log('Header nav controller.');
    };

    $scope.signout = function(){
      $http.get('/api/auth/signout/').success(function(data, status, header, config){
        $rootScope.authuser = null;
      }).error(function(data, status, header, config) {});
    };
  }])
  .controller('SidebarCtrl', ['$scope', function($scope) {
    console.log('Sidebar controller.');
  }]);
