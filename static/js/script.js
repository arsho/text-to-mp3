$("document").ready(function(){
  $("#share_url_copy_btn").on("click", function(){
    var share_url_text = document.getElementById("share_url");
    share_url_text.select();
    document.execCommand("copy");
  });
  $('.popover-dismiss').popover({
    trigger: 'focus'
  });
})
