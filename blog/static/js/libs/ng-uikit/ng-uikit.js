'use strict';

/**
* Binds a UiKit Editor widget to a <textarea> element.
*/

angular.module('uikit.editor', [])
.constant('uikitEditorConfig', {mode:'tab', markdown:true})
.directive('uikitEditor', ['$timeout', 'uikitEditorConfig', function($timeout, uikitEditorConfig) {
  return {
    restrict: 'EA',
    require: '?ngModel',
    priority: 1,
    link: function(scope, iElement, iAttrs, ngModel) {
      var options = JSON.parse(iAttrs.options) || uikitEditorConfig;
      var editor = $.UIkit.htmleditor(iElement[0], options);
      ngModel.$render = function() {
        var safeViewValue = ngModel.$viewValue || '';
        editor.editor.setValue(safeViewValue);
      };
      editor.editor.on('change', function (instance) {
        var newValue = instance.getValue();
        if (newValue !== ngModel.$viewValue) {
          scope.$apply(function() {
            ngModel.$setViewValue(newValue);
          });
        };
      });
    }
  };
}]);
