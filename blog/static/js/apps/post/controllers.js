'use strict';

angular.module('blog.post.controllers', [])
  .controller('PostListCtrl', ['$scope', '$http', '$location',
    function($scope, $http, $location){
    $scope.url = '/api/entries/';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
    }).error(function(data, status, header, config) {});
  }])
  .controller('PostDetailCtrl', ['$scope', '$routeParams', '$http', '$location',
    function($scope, $routeParams, $http, $location){
    $scope.url = '/api/entries/' + $routeParams.id + '/';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.entry = data;
    }).error(function(data, status, header, config) {});
  }]);
