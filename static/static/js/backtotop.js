$(document).ready(function () {
    !function (l) {
        "use strict";
        l("div#main-content-ishop").on(
            "scroll", function () {
                100 < l(this).scrollTop() ? l("#backToTop").fadeIn() : l("#backToTop").fadeOut();
            }
        ),
        l("div#main-content-ishop").click(function () {
                console.log(l(this).scrollTop());
            }
        ),
            l(document).on(
                "click", "button#backToTop",
                function (e) {
                    var o = l(this);
                    l("html, div#main-content-ishop").stop().animate({ scrollTop: 0 },
                        1e3, //this gives slow motion effect
                        "easeInOutExpo"),
                        e.preventDefault();
                }
            )
    }(jQuery);

});