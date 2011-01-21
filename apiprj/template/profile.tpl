{%extends "base.tpl"%}

{% block title %}
	동네API - 내 애플리케이션 관리
{% endblock %}

{% block breadcrumbs %}
	<div class="breadcrumbs">
		<a href="../">홈</a> &rsaquo; 
		내 애플리케이션 관리
	</div>
{% endblock %}

{% block content %}
	<h1>내 애플리케이션 관리</h1>
	<div class='module'>
		<h2>내가 등록한 애플리케이션 - 
		{{ user.username }}님이 등록하신 애플리케이션이 {{ consumers.count }}개 있습니다.
		</h2>
		{% for consumer in consumers %}
		<div class='app'>
			<h3>{{ consumer.name|escape }}</h3>
			<p>
				{{ consumer.description|urlize|linebreaks|escape }}
			</p>
			<span class='small'>
			<p>
		        consumer key: {{ consumer.key|escape }} <br/>
		        consumer secret: {{ consumer.secret|escape }} <br/>
			</p>
			<p>
				since {{ consumer.created }}
			</p>
			</span>
			<p>
			<a href="/consumer/edit/{{ consumer.key }}" class="changelink">편집</a> |
			<a href="/consumer/delete/{{ consumer.key }}" class="deletelink">삭제</a>
			</p>
			<hr/>
		</div>
		{% endfor %}
		
		<div class="submit-row">
		<p><a href="/consumer/create" class="addlink">새 애플리케이션 등록</a></p> 
		</div>

	</div>
	
	<hr/>
	
	<div class='module'>
		<h2>Access Token -
			{% if tokens.count %}
				{{ user.username }}님이 발행하신 {{ tokens.count }}개의 
				Access Token이 다음의 애플리케이션에서 사용되고 있습니다.
			{% else %}
				{{ user.username }}님이 발행한 access token이 없습니다.
			{% endif %}
		</h2>
		{% for token in tokens %}
		<div class='app'>
			<h3>{{ token.consumer.name|escape }} 
			<span class='small'>
				by {{ token.consumer.user_id }}
			</span></h3>

			{% if user.username == token.consumer.user_id %}
				<p class='small'>
				Access Token Key: {{ token.key }} <br/> 
				Access Token Secret: {{ token.secret }}
				</p>
			{% endif %}
			<p class='small'>
				since {{ token.created }}
			</p>

			<div class="submit-row">
			<p class="deletelink-box"><a href="/token/delete/{{ token.key }}" class="deletelink">삭제</a></p> 
			</div>
			
			<hr/>
		</div>
		{% endfor %}
	</div>


{%endblock%}