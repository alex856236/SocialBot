$(document).ready(function(){
	$('#sidebar > .worker').on('click', function(){
		$(this).parent().find('.worker').removeClass('active');
		$(this).toggleClass('active');
	});

	$('#backend').on('click', function(){
		window.location.href = '../backend/data_training.html';
		console.log('123');
	});

	$('#add_project').on('click', function(){
		window.location.href = 'dashboard.php';
	});

	$('.c-project').on('click', function(){
		window.location.href = 'dashboard.php';
	});
});