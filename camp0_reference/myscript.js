var fade_time = 500;
var wait_time = 3000;

$(document).ready(function() {
	show_first_image();
});

function show_first_image() {
	hide_image(fade_time)
	show_image("codelab-logo.png", fade_time);
	setTimeout(show_second_image, wait_time);
}

function show_second_image() {
	hide_image(fade_time)
	show_image("codelab-pic1.jpg", fade_time);
	setTimeout(show_third_image, wait_time);
}

function show_third_image() {
	hide_image(fade_time)
	show_image("codelab-pic2.jpg", fade_time);
	setTimeout(show_fourth_image, wait_time);
}

function show_fourth_image() {
	hide_image(fade_time)
	show_image("codelab-pic3.jpg", fade_time);
	setTimeout(show_first_image, wait_time); // cycle back
}





// helpers, ignore stuff below this line
function hide_image(time) {
	$('img').fadeOut(time);
}

function show_image(theimage, time) {
	$('img').queue(function() { $('img').attr('src', theimage); $(this).dequeue(); });
	$('img').fadeIn(time);
}