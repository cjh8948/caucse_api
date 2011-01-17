<!doctype HTML>
<html>
<head>
    <title>
    
    	{% block title %}
		{% endblock %}
    
    </title>
    <meta content='text/html; charset=UTF-8'>
    <link rel="stylesheet" type="text/css" href="/api_static/css/caucse_api.css" />
</head>
<body>
<div id='container'>

	<div id='header'>
	    <div id='logo'>
	        <a href='/'>
	        	<img src='http://www.caucse.net/page/images/home_menu_logo.gif'>
	        </a>
	    </div>
	    <div id='nav'>
	        <ul class='nav'>
	        
	            {% block navibar %} 
	            {% endblock %}
	            
	        </ul>
	    </div>
	</div>

    <div id='content'>
    
        {% block content %} 
    	{% endblock %}
    	
    </div>
    
    <div id='footer'>

    	{% block footer %}
    	{% endblock %}

    </div>
    
</div>

</body>
</html>
