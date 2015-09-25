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
  'ngHolder',
  'ngDisqusApi',
  'angularUtils.directives.dirDisqus',
  'blog.user.controllers',
  'blog.tag.controllers',
  'blog.nav.controllers',
  'blog.post.controllers',
  'blog.archive.controllers',
  'blog.comment.controllers',
  'blog.friendship.controllers'
]);

blog.config(['$routeProvider', '$locationProvider', '$httpProvider', 'markedProvider', '$disqusApiProvider',
  function($routeProvider, $locationProvider, $httpProvider, markedProvider, $disqusApiProvider) {
  $routeProvider.when('/', {
    templateUrl: '/static/js/partials/post/list.html',
    controller: 'PostListCtrl'
  }).when('/posts/:id', {
    templateUrl: '/static/js/partials/post/detail.html',
    controller: 'PostDetailCtrl'
  }).when('/post/add', {
    templateUrl: '/static/js/partials/post/edit.html',
    controller: 'PostAddCtrl'
  }).when('/post/:id', {
    templateUrl: '/static/js/partials/post/edit.html',
    controller: 'PostEditCtrl'
  }).when('/archive/:year/:month', {
    templateUrl: '/static/js/partials/post/list.html',
    controller: 'ArchiveListCtrl'
  }).when('/tags', {
    templateUrl: '/static/js/partials/tag/list.html',
    controller: 'TagListCtrl'
  }).when('/tags/:id', {
    templateUrl: '/static/js/partials/post/list.html',
    controller: 'TagDetailCtrl'
  }).when('/users/:id', {
    templateUrl: '/static/js/partials/post/list.html',
    controller: 'UserListCtrl'
  }).when('/following', {
    templateUrl: '/static/js/partials/friendship/list.html',
    controller: 'FollowingListCtrl'
  }).when('/followed', {
    templateUrl: '/static/js/partials/friendship/list.html',
    controller: 'FollowedListCtrl'
  }).when('/signin', {
    templateUrl: '/static/js/partials/auth/signin.html',
    controller: 'AuthCtrl'
  }).otherwise({redirectTo: '/'});

  markedProvider.setOptions({
    gfm: true,
    highlight: function (code) {
      return hljs.highlightAuto(code).value;
    }
  });

  $locationProvider.html5Mode({enabled: true, requireBase: false});
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $disqusApiProvider.setApiKey('t7ooOuVaSSY3OI5cJtGfm1e0S7J3xpKn9L35yIqA73IOMMo6yyvxRjGeSTSmRxHO');
  $disqusApiProvider.setForumName('amaozhao');
}]).run(function(amMoment) {
  amMoment.changeLocale('zh-cn');
});
