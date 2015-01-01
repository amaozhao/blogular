'use strict';

angular.module('blog.tag.controllers', [])
  .controller('TagListCtrl', ['$scope', '$http', '$location', '$routeParams',
    function($scope, $http, $location, $routeParams) {
    console.log($routeParams.id);
    $scope.url = '/api/entries/';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
    }).error(function(data, status, header, config) {});
  }]);
