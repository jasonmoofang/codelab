$(document).ready(function() {
	show_first_image();
	setTimeout(show_second_image, 3000);
	setTimeout(show_third_image, 6000);
	setTimeout(show_fourth_image, 9000);
});

function show_first_image() {
	hide_image(500)
	show_image("codelab-logo.png", 500);
}

function show_second_image() {
	hide_image(500)
	show_image("codelab-pic1.jpg", 500);
}

function show_third_image() {
	hide_image(500)
	show_image("codelab-pic2.jpg", 500);
}

function show_fourth_image() {
	hide_image(500)
	show_image("codelab-pic3.jpg", 500);
}





// helpers, ignore stuff below this line
function hide_image(time) {
	$('img').fadeOut(time);
}

function show_image(theimage, time) {
	$('img').queue(function() { $('img').attr('src', theimage); $(this).dequeue(); });
	$('img').fadeIn(time);
}