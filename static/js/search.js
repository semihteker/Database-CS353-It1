$(function(){
	$('#button_search').click(function(){

		$.ajax({
			url: '/searchFunc',
			data: $('form').serialize(),
			type: 'POST', 
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
