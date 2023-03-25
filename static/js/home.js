var txtArea = $("#target-textarea");
if (txtArea) {
  txtArea.each(function () {
    $(this).height(this.scrollHeight);
  });
}
