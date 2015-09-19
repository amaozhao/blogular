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
      $http.post('/api/tagfollowing/', {'id': tag.id}).success(function(data, status, header, config){
        tag.added = true;
      }).error(function(data, status, header, config){});
    };

    $scope.delete = function(tag) {
      $http.delete('/api/tagfollowing/' + tag.id + '/').success(function(data, status, header, config){
        tag.added = false;
      }).error(function(data, status, header, config){});
    };
  }])
  .controller('TagDetailCtrl', ['$scope', '$rootScope', '$http', '$location', '$routeParams',
    function($scope, $rootScope, $http, $location, $routeParams) {
    $scope.url = '/api/tags/' + $routeParams.id + '/';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
      $rootScope.title = '标签';
    }).error(function(data, status, header, config) {});
  }]);
