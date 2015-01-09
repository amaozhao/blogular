'use strict';

angular.module('blog.comment.controllers', [])
.controller('CommentListCtrl', ['$scope', '$rootScope', '$routeParams', '$http', '$location',
function($scope, $rootScope, $routeParams, $http, $location){
  $scope.comment = {};
  $scope.url = '/api/comments/' + $routeParams.id + '/';
  $http.get($scope.url).success(function(data, status, header, config){
    $scope.data = data;
  }).error(function(data, status, header, config) {});

  $scope.add = function() {
    $http.post($scope.url, $scope.comment).success(function(data, status, header, config){
      $scope.data.results.unshift(data);
      $scope.comment.content = '';
    }).error(function(data, status, header, config){});
  };

  $scope.edit = function(comment) {
    comment.edit = true;
  };

  $scope.save = function(comment) {
    $http.put($scope.url + comment.id + '/', comment).success(function(data, status, header, config){
      comment.edit = false;
    }).error(function(data, status, header, config){});
  };

  $scope.cancel = function(comment) {
    comment.edit=false;
  };

  $scope.delete = function(comment) {
    $http.delete($scope.url + comment.id + '/').success(function(data, status, header, config){
      $scope.data.results.splice($scope.data.results.indexOf(comment), 1);
    }).error(function(data, status, header, config){});
  };
}]);
