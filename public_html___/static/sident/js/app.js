
$(document).ready(function () {



	$('.tablebodytext').remove();


	$('.fancybox').fancybox();

	$('a[href*="#"]').bind("click", function(e){	
		var anchor = $(this);
		if ($(anchor.attr('href')).length>0){				
			$('html, body').stop().animate({
				scrollTop: $(anchor.attr('href')).offset().top
			}, 700);
			e.preventDefault();
		}
	});


	$(window).scroll(function(event) {
		if ($(window).scrollTop()>$(window).height()){
			$('.scroll_up').css('opacity', 1);
		}else{
			$('.scroll_up').css('opacity', 0);
		}
	});


	$('.scroll_up').click(function(event) {
		$("body,html").animate({
			scrollTop:0
		}, 800);
	
	});


function getName (str){
	if (str.lastIndexOf('\\')){var i = str.lastIndexOf('\\')+1;}
	else{var i = str.lastIndexOf('/')+1;}						
	var filename = str.slice(i);			
	var uploaded = document.getElementById("fileformlabel");
	uploaded.innerHTML = filename;
}


$(window).load(function() {	


	$('.main-slider .owl-buttons > div').height($('.main-slider').height());

	var mx = 0;
	$('.service-list .item').each(function(index, el) {
		mx = Math.max(mx, $(el).find('.desc').height());
	});	
	$('.service-list .item .desc').height(mx);


	$('.service-list .item .subsections').slideUp(0);

	$('.service-list .item').hover(function() {		
		if ( $(this).find('.subsections').length>0){
			$(this).find('.subsections').slideDown(300);
			$(this).find('.announce').slideUp(300);
		}
	}, function() {
		if ( $(this).find('.subsections').length>0){
			$(this).find('.subsections').slideUp(300);		
			$(this).find('.announce').slideDown(300);
		}
	});			




	$('.dropmenu-bttn').click(function(event) {
		if ($('.header .menu').hasClass('active'))
			$('.header .menu').removeClass('active');
		else
			$('.header .menu').addClass('active');
	});



});

//Lightbox
$(document).on("click", '[data-toggle="lightbox"]', function(event) {
  event.preventDefault();
  $(this).ekkoLightbox();
});


//Callback button 
$(function(){ 
    $('.call_back_button_image').delay(2500)
                .show(1000);
	$('.call_back_button').delay(2600)
                .show(1000);
});

//Floating menu bar
$(function(){
  var topPos = $('#floating').offset().top;
  $(window).scroll(function() { 
  var top = $(document).scrollTop(),
      pip = $('footer').offset().top;
      height = $('#floating').outerHeight();
  if (top > topPos && top < pip - height) {$('#floating').addClass('fixed').removeAttr("style");}
  else if (top > pip - height) {$('#floating').removeClass('fixed').css({'position':'absolute','bottom':'0'});}
  else {$('#floating').removeClass('fixed');}
  });
});


//Blur
$("#buttonId").blur();

//Phone masc
 $(".phone").mask("+99(999)999-9999");

//Testimonials appears
$(function(){ 
var TestimPos = $('.testimonials').offset().top;
$(window).scroll(function() { 
	var top = $(document).scrollTop(),
      pip = $('footer').offset().top;
      height = $('.testimonials').outerHeight();
  if (top > TestimPos && top < pip - height) {$('.testimonials').show(1000);}
});
});


 //Contact form
 function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
 function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


    // $(function(){

    //   $('#subb4').click(function(event){

    //       event.preventDefault();
    //       var csrftoken = getCookie('csrftoken');

    //       var $feedback_form = $('#feedback4');

    //       var namecb1 = $('#fname4').val();
    //       var phonecb1 = $('#fphone4').val();
    //       var time = $('#ftime4').val();
    //       var date = $('#datepicker').val();
    //       var chbox1 = document.getElementById('check_feed4');

    //       var flag = true;
    //       if(!chbox1.checked){

    //           $('#err4').append('Необходимо согласие на обработку персональных данных<br>');
    //           flag = false;
    //       }
    //       if(namecb1 ===''){

    //           $('#err4').append('Необходимо заполнить поле Имя<br>');
    //           flag = false;
    //       }
    //       if(phonecb1 ===''){
    //                      event.preventDefault();
    //           $('#err4').append('Необходимо заполнить поле Телефон<br>');
    //           flag = false;
    //       }
    //           if(flag){

    //       $.ajax({
    //           beforeSend: function(xhr, settings) {
    //     if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
    //         xhr.setRequestHeader("X-CSRFToken", csrftoken);
    //         }
    //     },
    //         method: 'post',
    //         url: $feedback_form.attr('action'),
    //         data: $feedback_form.serialize(),

    //     });
    //     $('#confirm4').append('Ваше сообщение успешно отправлено!<br>');
    //     $feedback_form.addClass("hidden");
    //   }
    //   });
    // });

