$(document).ready(function(){
	var villes = [];
	var activites = [];

	$.ajax({
		url:"/ville",
		dataType: 'JSON',
    	type: 'GET',

		success: function (responce) {
			//console.log("responce ville"+responce);
			$.each(responce,function(i){
				villes[i]=responce[i].ville;
				//console.log(responce[i]);
			});
			$('#ville').autocomplete({
				minLength:3,
        		source:cleanArray(villes)
    		});
		},

		error: function (data, xhr, status, err) {
			//console.log("err "+err);
		}, 
	});

	$.ajax({
		url:"/activite",
		dataType: 'JSON',
    	type: 'GET',

		success: function (responce) {
			//console.log("responce activite"+responce);
			$.each(responce,function(i){
				activites[i]=responce[i].activite;
				//console.log(responce[i]);
			});
			$('#activite').autocomplete({
				minLength:3,
        		source:cleanArray(activites)
    		});
		},

		error: function (data, xhr, status, err) {
			//console.log("err "+err);
		}, 
	});
		
		$('#recherche').submit(function(e){
			e.preventDefault();
			if($('#error')){
				$('#error').remove();
			}	
			var requette="";
			if($('#ville').val() && $('#activite').val()){
				requette='?ville='+$('#ville').val()+"&activite="+$('#activite').val();
			}
			$('#ville').val("");
			$('#activite').val("");
			$.ajax({
				url:"/installation"+requette,
				dataType: 'JSON',
    			type: 'GET',
				success: function (responce) {
					console.log(responce);
					$(".reponce").remove();
					$('#error').hide();
					$.each(responce, function(index,responce) {
						if(responce[0]){
							$.each(responce,function(i){
								//console.log(responce[i].installation);
								$('<div/>',{id:""+(responce[i].equipement[0].numero),class:"reponce "}).appendTo($('#container'));
								$('<div/>',{class:"panel panel-primary"}).appendTo($("#"+(responce[i].equipement[0].numero)));
								$('<div/>',{class:"panel-heading"}).text(responce[i].installation+" "+responce[i].code_postal+" "+responce[i].ville).appendTo($("#"+(responce[i].equipement[0].numero)).find('.panel-primary'));
								$('<div/>',{class:"panel-body"}).appendTo($("#"+(responce[i].equipement[0].numero)).find('.panel-primary'));
								//$('<p/>').text("Activite : "+responce[i].activite).appendTo($("#"+(responce[i].equipement[0].numero)).find('.panel-body'));
								$('<p/>').text("Adresse : "+responce[i].adresse+" "+responce[i].code_postal+" "+responce[i].ville).appendTo($("#"+(responce[i].equipement[0].numero)).find('.panel-body'));
							})
						}else{
							$('<div/>',{id:'error', class:'col-md-12'}).appendTo('#container');
							$('<p/>').text("Cette activite n'est pas pratiqué dans cette ville.").appendTo($('#error'));
						}
					});

					$('.reponce').click(function(){
						getEquipement($(this),$(this).attr('id'));
					})

				},

				error: function (data, xhr, status, err) {
					 //console.log(data);
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


function getEquipement(equipement, id){
	$.ajax({
		url:"/equipement?id="+id,
		dataType: 'JSON',
    	//jsonpCallback: 'callback',
    	type: 'GET',

		success: function (responce) {
			$('#equipement').remove();
			equipement.find('.panel-body').append($('<p/>',{id:'equipement'}).text("Equipement : "+responce));
		},

		error: function (data, xhr, status, err) {
			
		}, 
	});
}

//cleanArray removes all duplicated elements
function cleanArray(array) {
  var i, j, len = array.length, out = [], obj = {};
  for (i = 0; i < len; i++) {
    obj[array[i]] = 0;
  }
  for (j in obj) {
    out.push(j);
  }
  return out;
}