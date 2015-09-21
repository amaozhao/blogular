'use strict';

angular.module('blog.archive.controllers', [])
  .controller('ArchiveListCtrl', ['$scope', '$rootScope', '$http', '$location', '$routeParams',
  function($scope, $rootScope, $http, $location, $routeParams){
    $scope.url = '/api/archives/' + $routeParams.year + '/' + $routeParams.month + '/';
    $rootScope.title = '日志归档 - ' + $routeParams.year + ' - ' + $routeParams.month;
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
    }).error(function(data, status, header, config) {});

    $scope.delete = function(entry) {
      $http.delete('/api/entries/' + entry.id + '/').success(function(data, status, header, config){
        $scope.data.results.splice($scope.data.results.indexOf(entry), 1);
      }).error(function(data, status, header, config){});
    };

    $scope.next = function() {
      $http.get($scope.data.next).success(function(data, status, header, config){
        $scope.data = data;
      }).error(function(data, status, header, config) {});
    };

    $scope.previous = function() {
      $http.get($scope.data.previous).success(function(data, status, header, config){
        $scope.data = data;
      }).error(function(data, status, header, config) {});
    };
  }]);
