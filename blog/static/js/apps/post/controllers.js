'use strict';

angular.module('blog.post.controllers', [])
  .controller('PostListCtrl', ['$scope', '$rootScope', '$http', '$location',
  function($scope, $rootScope, $http, $location){
    $scope.url = '/api/entries/';
    $rootScope.title = '首页';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.data = data;
    }).error(function(data, status, header, config) {});

    $scope.delete = function(entry) {
      $http.delete($scope.url + entry.id + '/').success(function(data, status, header, config){
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

    $scope.config = {
      create: true,
      valueField: 'name',
      labelField: 'name',
      delimiter: '|',
      placeholder: '添加标签'
    };

    $http.get('/api/tags/').success(function(data, status, header, config){
      $scope.tags = data.results;
      angular.forEach($scope.tags, function(tag) {
        this.push(tag.name);
      }, data.results);
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
  .controller('PostEditCtrl', ['$scope', '$rootScope', '$routeParams', '$http', '$window',
  function($scope, $rootScope, $routeParams, $http, $window){
    $http.get('/api/tags/').success(function(data, status, header, config){
      $scope.tags = data.results;
      angular.forEach($scope.tags, function(tag) {
        this.push(tag.name);
      }, data.results);
    }).error(function(data, status, header, config) {});

    $scope.url = '/api/entries/' + $routeParams.id + '/';
    $http.get($scope.url).success(function(data, status, header, config){
      $scope.entry = data;
      var tags = $scope.entry.tags;
      $scope.entry.tags = [];
      angular.forEach(tags, function(tag) {
        this.push(tag.name);
      }, $scope.entry.tags);
      $rootScope.title = data.title;
    }).error(function(data, status, header, config) {});

    $scope.config = {
      create: true,
      valueField: 'name',
      labelField: 'name',
      delimiter: '|',
      placeholder: '添加标签',
      onInitialize: function(selectize){
        // receives the selectize object as an argument
      },
    };

    $scope.save = function(){
      $http.put($scope.url, $scope.entry).success(function(data, status, header, config){
        $window.history.back();
      }).error(function(data, status, header, config) {});
    };

    $scope.cancel = function(){
      $window.history.back();
    };
  }]);
