(function($) {

    "use strict";

    function moveProductSlide(index) {
        var imageLink;
        var $thumbs = $(".product-images-list li");
        var $next = $thumbs.filter('.active').next();
        var $prev = $thumbs.filter('.active').prev();
        var $active = index == -1 ? $prev : $next;

        imageLink = $active.find('img').attr('src');
        console.log(imageLink);
        if ( imageLink ) {
            $("#product_image").addClass('fade-out').attr('src', imageLink);
            $active.addClass('active').siblings().removeClass('active');
            if ($active.is(':last-child')) {
                $('.product-img-arrows .next').hide();
            } else {
                $('.product-img-arrows .next').show();
            }

            if ($active.is(':first-child')) {
                $('.product-img-arrows .previous').hide();
            } else {
                $('.product-img-arrows .previous').show();
            }


            setTimeout(function(){
                $("#product_image").removeClass('fade-out');
            }, 320);
        }
    }

    $(document).on('click', '.product-img-arrows .next', function() {
        moveProductSlide(1);
    });
    $(document).on('click', '.product-img-arrows .previous', function() {
        $(".product-images-list li.active").index;
        moveProductSlide(-1);
    });

    $("#product_image").on('click', function() {
        $(this).parents('a').trigger('click');
    });

})(jQuery);