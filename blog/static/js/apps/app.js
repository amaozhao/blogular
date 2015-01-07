'use strict';

var blog = angular.module('blog', [
  'ngRoute',
  'ngSanitize',
  'ngCookies',
  'ui.bootstrap',
  'uikit.editor',
  'hc.marked',
  'angularMoment',
  'angular-loading-bar',
  'selectize',
  'blog.user.controllers',
  'blog.tag.controllers',
  'blog.nav.controllers',
  'blog.post.controllers'
]);

blog.config(['$routeProvider', '$locationProvider', '$httpProvider', 'markedProvider',
  function($routeProvider, $locationProvider, $httpProvider, markedProvider) {
  $routeProvider.when('/', {
    templateUrl: '/static/js/partials/post/list.html',
    controller: 'PostListCtrl'
  }).when('/posts/:id', {
    templateUrl: '/static/js/partials/post/detail.html',
    controller: 'PostDetailCtrl'
  }).when('/post/add', {
    templateUrl: '/static/js/partials/post/edit.html',
    controller: 'PostAddCtrl'
  }).when('/tags/:id', {
    templateUrl: '/static/js/partials/post/list.html',
    controller: 'TagListCtrl'
  }).when('/users/:id', {
    templateUrl: '/static/js/partials/post/list.html',
    controller: 'UserListCtrl'
  }).when('/signin', {
    templateUrl: '/static/js/partials/auth/signin.html',
    controller: 'AuthCtrl'
  })
  .when('/find', {
    templateUrl: '/static/js/partials/post/list.html',
    controller: 'FindListCtrl'
  })
  .otherwise({redirectTo: '/'});

  markedProvider.setOptions({
    gfm: true,
    highlight: function (code) {
      return hljs.highlightAuto(code).value;
    }
  });

  $locationProvider.html5Mode({enabled: true, requireBase: false});

  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]).run(function(amMoment) {
  amMoment.changeLocale('zh-cn');
});
