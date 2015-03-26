$(document).ready(function(){
	var villes = [];
	var activites = [];

	$.ajax({
		url:"/ville",
		dataType: 'JSON',
    	type: 'GET',

		success: function (response) {
			$.each(response,function(i) {
				villes[i] = response[i].ville;
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

		success: function (response) {
			$.each(response,function(i) {
				activites[i] = response[i].activite;
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
		
		$('#recherche').submit(function(e) {
			e.preventDefault();

			if($('#error')) {
				$('#error').remove();
			}	

			var request="";
			if($('#ville').val() && $('#activite').val()) {
				request='?ville='+$('#ville').val()+"&activite="+$('#activite').val();
			}

			// On efface les données dans les champs activité et ville
			$('#ville').val("");
			$('#activite').val("");

			$.ajax({
				url:"/installation"+request,
				dataType: 'JSON',
    			type: 'GET',

				success: function (response) {
					// Efface les anciens panels
					$(".monPanel").remove();
					// Enlève un précédent message d'erreurs si besoin
					$('#error').hide();

					$.each(response, function(index, response) {
						if(response[0]){
							$.each(response,function(i){
								$('<div/>',{id:""+(response[i].numeroEquipement),class:"monPanel"}).appendTo($('.documents'));
								$('<div/>',{class:"panel panel-primary"}).appendTo($("#"+(response[i].numeroEquipement)));
								
								// Titre d'un panel
								$('<div/>',{class:"panel-heading"}).text('#'+i+" "+response[i].nom).appendTo($("#"+(response[i].numeroEquipement)).find('.panel-primary'));
								// Création d'un body pour le panel
								$('<div/>',{class:"panel-body"}).appendTo($("#"+(response[i].numeroEquipement)).find('.panel-primary'));
								
								// Adresse
								if (response[i].voie == '0') {
									$("#"+(response[i].numeroEquipement)).find('.panel-body').append('<span class="glyphicon glyphicon-home" aria-hidden="true"></span>'+" "+response[i].adresse+" "+response[i].codePostal+" "+response[i].ville);
								}	
								else {
									$("#"+(response[i].numeroEquipement)).find('.panel-body').append('<span class="glyphicon glyphicon-home" aria-hidden="true"></span>'+" "+response[i].voie+", "+response[i].adresse+" "+response[i].codePostal+" "+response[i].ville);
								}
								// Equipement
								getEquipement($("#"+(response[i].numeroEquipement)),$("#"+(response[i].numeroEquipement)).attr('id'));

							})
						}
						else{
							// Activité non pratiquée dans la ville
							$('<div/>',{id:'error'}).appendTo('.documents');
							$('<div/>',{class: 'alert alert-warning'}).text("Cette activite n'est pas pratiqué dans cette ville.").appendTo($('#error'));
							$('.alert').prepend('<strong>Dommage!</strong> ');
						}
					});
				},

				error: function (data, xhr, status, err) {
					 //console.log(data);
					$('#recherche').find('div').each(function(i){
						if(i<2){
							$(this).addClass('has-error');
						}
					});
					$('<div/>',{class: 'alert alert-warning'}).text("L'installation n'a pas pu être chargée").appendTo($('#error'));
					$('.alert').prepend('<strong>Erreur!</strong> ');
				}, 
			});
			
		});
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

		success: function (response) {
			$('#equipement').remove();
			equipement.find('.panel-body').append('<br><br><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span>'+" "+response);
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