var txtArea = document.querySelector(".target-textarea");
if (txtArea) {
  txtArea.each(function () {
    $(this).height(this.scrollHeight);
  });
}
