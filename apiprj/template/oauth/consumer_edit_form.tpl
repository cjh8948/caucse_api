{%extends "base.tpl"%}

{% block breadcrumbs %}
	<div class="breadcrumbs">
		<a href="/">홈</a> &rsaquo; 
		<a href="/accounts/profile">내 애플리케이션 관리</a> &rsaquo; 
		애플리케이션 편집
	</div>
{% endblock %}

{% block content %}
	<h1>애플리케이션 편집</h1>
	<fieldset class="module aligned "> 
	<h2>애플리케이션</h2>
	<form method="post">
		{%csrf_token%}
		<table> 
		{{ form.as_table }}
		</table>
		<p>
		    <input type='submit' value='변경'/><input type='hidden' name='oauth_token' value='{{ oauth_token }}'/>
		</p>
	</form>
	</fieldset>
{% endblock %} 