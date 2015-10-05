$(document).ready(function() {
  if($("#id_content").length) {
    var editor = $.UIkit.htmleditor($("#id_content"), {mode:'tab', markdown:true});
  }
  $('.uk-htmleditor-fullscreen').css('z-index', 9999);
});
