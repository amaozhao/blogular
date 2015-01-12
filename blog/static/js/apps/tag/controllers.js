'use strict';

angular.module('blog.tag.controllers', [])
  .controller('TagListCtrl', ['$scope', '$rootScope', '$http', '$location',
    function($scope, $rootScope, $http, $location){
    $scope.url = '/api/tags/';
    $rootScope.title = '发现';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
    }).error(function(data, status, header, config) {});

    $scope.add = function(tag) {
      console.log(tag.name);
    };
  }])
  .controller('TagDetailCtrl', ['$scope', '$rootScope', '$http', '$location', '$routeParams',
    function($scope, $rootScope, $http, $location, $routeParams) {
    $scope.url = '/api/tags/' + $routeParams.id + '/';
    console.log($routeParams.id)
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
      $rootScope.title = '标签';
    }).error(function(data, status, header, config) {});
  }]);
