var socket = io.connect('http://' + document.domain + ':' + location.port);

var colorPicker = new iro.ColorPicker("#color-picker-container", {
	// Set the size of the color picker UI
	width: 320,
	height: 320,
	// Set the initial color to red
	color: "#f00",

	css: {
		"h1": {
			"color": "$color"
		}
	}
});

var toggle_buttons = document.querySelectorAll('.toggle');

socket.on('connect_conf', function (data) {
	data = JSON.parse(data)

	for (var i = 0; i < data['button'].length; i++)
	{
		var element = document.querySelectorAll('[data-button="'+data['button'][i][0]+'"]');

		if (data['button'][i][1])
		{
			element[0].classList.add('active');
		}
	}

	colorPicker.color.rgb = {r: parseInt(data['r']), g: parseInt(data['g']), b: parseInt(data['b'])}

	colorPicker.on("color:change", function(color, changes) {
		socket.emit('message', color.rgb);
	});
});

for (var i = 0; i < toggle_buttons.length; i++)
{
	toggle_buttons[i].addEventListener('toggle', function(e){
		var buttonName = e.target.getAttribute('data-button');
		var value = (e.target.classList.contains('active')) ? 1 : 0;

		socket.emit('toggle_button', {button:buttonName,value:value})
	});
}
