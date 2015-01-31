function showhidden(id) {
var winWidth = window.innerWidth;
if(winWidth > 990) {
			document.getElementById(id).style.width = "100%";
			document.getElementById("hidden-block").style.height = "500px";
			document.getElementById("hidden-block").style.margin = "20px 0";
			document.getElementById("featured-btn1").style.display = "none";
			document.getElementById("reset2").style.display = "block";
			document.getElementById("hidden1").style.position = "absolute";
	  } else {
			document.getElementById("reset1").style.display = "block";
			document.getElementById("hidden-block").style.height = "500px";
			document.getElementById("hidden-block").style.margin = "20px 0";
			document.getElementById("featured-btn1").style.display = "none";
	}
}

function reset(id) {
var winWidth = window.innerWidth;
			document.getElementById("reset1").style.display = "none";
			document.getElementById("reset2").style.display = "none";
			document.getElementById("featured-btn1").style.display = "block";
			document.getElementById("hidden-block").style.height = "0";
			document.getElementById("hidden-block").style.margin = "0";
if(winWidth > 990) {
			document.getElementById(id).style.width = "calc(40% - 50px)";
			document.getElementById("hidden1").style.position = "relative";
	} else {
	}
}