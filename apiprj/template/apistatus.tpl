{%extends "base.tpl"%}

{% block title %}
	동네API - 시스템 상태
{% endblock %}

{% block breadcrumbs %}
	<div class="breadcrumbs">
		<a href="../">홈</a> &rsaquo; 
		시스템 상태
	</div>
{% endblock %}

{% block content %}

	<h1>동네API 시스템 상태</h1>
	<p>로그 분석을 통해 실시간 동네API의 상태를 알려 드리는 서비스를 준비 중 입니다.</p>
	
	{% if consumers %}
	<div class='module'>
		<h2>등록된 애플리케이션 목록</h2>
		{% for consumer in consumers %}
		<div class='app'>
			<h3>{{ consumer.name|escape }}<span class='small'>
				by{{ consumer.user_id }}
				with {{ consumer.num_tokens }} users 
				since {{ consumer.created }}
			</span></h3>
			<p>{{ consumer.description|urlize|linebreaks|escape }}</p> 
			<hr/>
		</div>
		{% endfor %}
	</div>
	{% endif %}
	
{% endblock %} 