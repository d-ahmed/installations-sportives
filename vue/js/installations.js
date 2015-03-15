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
			e.preventDefault();
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
			if($(".reponce")){
				$(".reponce").remove();
			}
			$.ajax({
				url:"http://localhost:8001/installation"+requette,
				dataType: 'JSON',
    			//jsonpCallback: 'callback',
    			//type: 'GET',
				success: function (responce) {
					$('#error').hide();
					$.each(responce, function(index,responce) {
						$.each(responce,function(i){
						//console.log(responce[i].installation);
						$('<div/>',{id:""+(i),class:"reponce"}).appendTo($('#container'));
						$('<div/>',{class:"panel panel-primary"}).appendTo($("#"+(i)));
						$('<div/>',{class:"panel-heading"}).text(responce[i].installation+" "+responce[i].code_postal+" "+responce[i].ville).appendTo($("#"+(i)).find('.panel-primary'));
						$('<div/>',{class:"panel-body"}).appendTo($("#"+(i)).find('.panel-primary'));
						$('<p/>').text("Activite : "+responce[i].activite).appendTo($("#"+(i)).find('.panel-body'));
						$('<p/>').text("Adresse : "+responce[i].adresse+" "+responce[i].code_postal+" "+responce[i].ville).appendTo($("#"+(i)).find('.panel-body'));
						})
					})
				},

				error: function (data, xhr, status, err) {
					 console.log(data);
					$('#recherche').find('div').each(function(i){
						if(i<2){
							$(this).addClass('has-error');
						}
					});
					$('<div/>',{id:'error', class:'col-md-12'}).appendTo('#container');
					$('<p/>').text("Erreur lors du chargement de l'installation ...").appendTo($('#error'));
				}, 
			});
			
		});
	//});
});

function base(arg){
	console.log(arg);
}