'use strict';

angular.module('blog.tag.controllers', [])
  .controller('TagListCtrl', ['$scope', '$http', '$location', '$routeParams',
    function($scope, $http, $location, $routeParams) {
    $scope.url = '/api/entries/';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
      $scope.title = '标签: ' + '';
    }).error(function(data, status, header, config) {});
  }]);
