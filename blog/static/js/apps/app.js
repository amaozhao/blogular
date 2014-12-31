'use strict';

var blog = angular.module('blog', [
  'ngRoute',
  'ngSanitize',
  'ngCookies',
  'hc.marked',
  'angular-loading-bar',
  'blog.post.controllers'
]);

blog.config(['$routeProvider', '$locationProvider', '$httpProvider', 'markedProvider',
  function($routeProvider, $locationProvider, $httpProvider, markedProvider) {
  $routeProvider.when('/', {
    templateUrl: '/static/js/partials/post/list.html',
    controller: 'PostListCtrl'
  }).when('/post/:id', {
    templateUrl: '/static/js/partials/post/detail.html',
    controller: 'PostDetailCtrl'
  })
  .otherwise({redirectTo: '/'});

  markedProvider.setOptions({
    gfm: true,
    tables: true,
    highlight: function (code) {
      return hljs.highlightAuto(code).value;
    }
  });

  $locationProvider.html5Mode({enabled: true, requireBase: false});

  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
