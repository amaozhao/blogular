'use strict';

angular.module('blog.post.controllers', [])
  .controller('PostListCtrl', ['$scope', '$rootScope', '$http', '$location',
  function($scope, $rootScope, $http, $location){
    $scope.url = '/api/entries/';
    $rootScope.title = '首页';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
    }).error(function(data, status, header, config) {});
  }])
  .controller('PostDetailCtrl', ['$scope', '$rootScope', '$routeParams', '$http', '$location',
  function($scope, $rootScope, $routeParams, $http, $location){
    $scope.url = '/api/entries/' + $routeParams.id + '/';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.entry = data;
      $rootScope.title = data.title;
    }).error(function(data, status, header, config) {});
  }])
  .controller('PostAddCtrl', ['$scope', '$rootScope', '$http', '$window',
  function($scope, $rootScope, $http, $window){
    $scope.url = '/api/entries/';
    $rootScope.title = '新建日志';
    $scope.entry = {};

    $http.get('/api/tags/').success(function(data, status, header, config){
      $scope.tags = data;
    }).error(function(data, status, header, config) {});

    $scope.save = function(){
      $http.post($scope.url, $scope.entry).success(function(data, status, header, config){
        $window.history.back();
      }).error(function(data, status, header, config) {});
    };

    $scope.cancel = function(){
      $window.history.back();
    };
  }])
  .controller('FindListCtrl', ['$scope', '$rootScope', '$http', '$location',
  function($scope, $rootScope, $http, $location){
    $scope.url = '/api/find/';
    $rootScope.title = '发现';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
    }).error(function(data, status, header, config) {});
  }]);
