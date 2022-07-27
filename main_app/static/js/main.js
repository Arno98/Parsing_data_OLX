$(document).on('submit', '.update_form', function(e){
				
	e.preventDefault();
						
	let form = $(this).closest('.update_form');
						
	$.ajax({
		type: 'POST',
		url: '/update',
		datatype: 'json',
		headers: {'X-CSRFToken': csrftoken},
		formElement: form,
		success: function(data) {
			$('.table').html(data.data);
		}
	});
});
		
$(document).on('submit', '.delete_form', function(e){
	
	e.preventDefault();
							
	let form = $(this).closest('.delete_form');

	$.ajax({
		type: 'POST',
		url: '/delete',
		datatype: 'json',
		headers: {'X-CSRFToken': csrftoken},
		formElement: form,
		success: function() {
			$(form).closest('tr').remove();
		}
	});
});
