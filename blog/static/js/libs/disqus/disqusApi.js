(function () {
  'use strict';

  angular.module('ngDisqusApi', []);

  /*
   * ngDisqus Provider
   */

  angular.module('ngDisqusApi').provider('$disqusApi', disqusApiProvider);

  /*jshint validthis: true */
  function disqusApiProvider() {
    var forumName;
    var disqusApiKey;
    var disqusApiBaseUrl = 'https://disqus.com/api/3.0/';

    this.setForumName = function (name) {
      forumName = name;
    };

    this.setApiKey = function (apiKey) {
      disqusApiKey = apiKey;
    };

    this.getApiKey = function () {
      return disqusApiKey;
    };

    this.getApiUrl = function () {
      return disqusApiBaseUrl;
    };

    this.getForumName = function () {
      return forumName;
    };

    this.$get = function () {
      return {
        setForumName: this.setForumName,
        setApiKey: this.setApiKey,
        getApiKey: this.getApiKey,
        getApiUrl: this.getApiUrl,
        getForumName: this.getForumName
      };
    };
  }

  angular.module('ngDisqusApi').factory('disqusApi', disqusApiService);

  disqusApiService.$inject = ['$http', '$q', '$log', '$disqusApi'];

  function disqusApiService($http, $q, $log, $disqusApi) {
    var apiKey = $disqusApi.getApiKey();
    var apiUrl = $disqusApi.getApiUrl();
    var forumName = $disqusApi.getForumName();

    var requiredParams = {
      forum: forumName,
      api_key: apiKey
    };
    var service = {
      get: getRequest
    };

    return service;

    function getRequest(category, method, params) {
      var deferred = $q.defer();
      $http({
        method: 'GET',
        url: apiUrl + '/' + category + '/' + method + '.json',
        params: angular.extend(requiredParams, params)
      }).success(function (data) {
        deferred.resolve(data.response);
      }).error(function (error) {
        deferred.reject(error);
      });
      return deferred.promise;
    }
  }

  /*
   * Recent Comments Directive
   */
  angular.module('ngDisqusApi').directive('recentComments', recentCommentsDirective);

  function recentCommentsDirective() {
    return {
      restrict: 'EA',
      replace: true,
      templateUrl: "/static/js/partials/comment/recent.html",
      scope: {
        params: '='
      },
      controller: ['$scope', 'disqusApi', function ($scope, disqusApi) {
        var params = $scope.params || {};
        disqusApi.get('forums', 'listPosts', params).then(function (comments) {
          $scope.comments = comments;
        });
      }]
    };
  }
})();
