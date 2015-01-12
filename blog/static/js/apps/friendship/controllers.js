'use strict';

angular.module('blog.friendship.controllers', [])
.controller('FollowingListCtrl', ['$scope', '$rootScope', '$http', '$location',
function($scope, $rootScope, $http, $location){
  $rootScope.title = "关注我的好友";
  $scope.editable = true;
  $scope.url = '/api/following/';
  $http.get($scope.url).success(function(data, status, header, config){
    $scope.data = data;
  }).error(function(data, status, header, config) {});

  $scope.delete = function(friend) {
    $http.delete($scope.url + friend.id + '/').success(function(data, status, header, config) {
      $scope.data.results.splice($scope.data.results.indexOf(friend), 1);
    }).error(function(data, status, header, config) {});
  };
}])
.controller('FollowedListCtrl', ['$scope', '$rootScope', '$http', '$location',
function($scope, $rootScope, $http, $location){
  $rootScope.title = "我关注的好友";
  $scope.editable = false;
  $scope.url = '/api/followed/';
  $http.get($scope.url).success(function(data, status, header, config){
    $scope.data = data;
  }).error(function(data, status, header, config) {});
}]);
