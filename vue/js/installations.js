$(document).ready(function(){

	//$('#installations').click(function(){
		/*$('#recherche').remove();
		$('<form/>',{methode:'get',id:'recherche'}).appendTo($("#container"));

		$('<div/>',{class:'row', id:'row'}).appendTo("#recherche");
		$('<div/>',{class:'col-xs-6 col-md-4', id:'col1'}).appendTo("#row");
		$('<div/>',{class:'col-xs-6 col-md-4', id:'col2'}).appendTo("#row");
		$('<div/>',{class:'col-xs-6 col-md-4', id:'col3'}).appendTo("#row");
		
		$('<p/>',{text:'Ville ', id:'p1'}).appendTo($("#col1"));
		$("<input/>",{type:'text', id:'ville'}).appendTo($('#p1'));
		$('<p/>',{text:'Activite ',id:'p2'}).appendTo($("#col2"));
		$("<input/>",{type:'text', id:'activite'}).appendTo($('#p2'));
		$("<input/>",{type:'submit', value:'recherche'}).appendTo($('#col3'));
		*/

		$('#recherche').submit(function(e){
			if($('#error')){
				$('#error').remove();
			}	
			var requette="";
			if($('#ville').val() && $('#activite').val()){
				//alert($('#ville').html());
				requette='?ville='+$('#ville').val()+"&activite="+$('#activite').val();
			}
			$('#ville').val("");
			$('#activite').val("");
			//$('#recherche').css({display:'none'});
			$.ajax({
				type: 'GET',
				url:'http://localhost:8080/installation'+requette,
				dataType: 'json',
				success: function (data) {
					$('#error').hide();
					$('<p/>',{text:data.numero,class:'reponce'}).appendTo($("#container"));
					$('<p/>',{text:data.nom,class:'reponce'}).appendTo($("#container"));
				},

				error: function (data, xhr, status, err) {
					$('#recherche').find('div').each(function(i){
						if(i<2){
							$(this).addClass('has-error');
						}
					});
					$('<div/>',{id:'error', class:'col-md-12'}).appendTo('#container');
					$('<p/>').text("Erreur lors du chargement de l'installation ...").appendTo($('#error'));
				}
			});
			e.preventDefault();
		});
	//});
});