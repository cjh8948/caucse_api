{%extends "base.tpl"%}

{% block title %}
	동네API - 상태
{% endblock %}

{% block breadcrumbs %}
	<div class="breadcrumbs">
		<a href="../">홈</a> &rsaquo; 
		내 애플리케이션
	</div>
{% endblock %}

{% block content %}
	<h1>내 애플리케이션</h1>
	<div class='side_by_side_left'>
		<h2>Access Token</h2>
		{% if tokens.count %}
			<p>{{ user.username }}님은 {{ tokens.count }}개의 Access Token을 
			발행하여 다음의 애플리케이션에서 사용되고 있습니다.</p>
		{% else %}
			<p>{{ user.username }}님이 발행한 access token이 없습니다.</p>
		{% endif %}
		{% for token in tokens %}
		<div class='app'>
			<h3>{{ token.consumer.name|escape }} by {{ token.consumer.user_id }}</h3>
			<p>
				 {{ token.consumer.description|escape }}
			</p>
		
			{% if user.username == token.consumer.user_id %}
				<p>
					Access Token: ({{ token.key }}, {{ token.secret }})
				</p>
			{% endif %}
			
			<p>
				since {{ token.created }}
			</p>
		</div>
		{% endfor %}
	</div>

	<div class='side_by_side_right'>
		<h2>내 애플리케이션</h2>
		{{ user.username }}님이 등록하신 애플리케이션이 {{ consumers.count }}개 있습니다.
		{% for consumer in consumers %}
		<div class='app'>
			<h3>{{ consumer.name|escape }}</h3>
			<p>
				{{ consumer.description|escape }}
			</p>
			<p>
		        consumer key:{{ consumer.key|escape }} <br/>
		        consumer secret: {{ consumer.secret|escape }}
			</p>
			<p>
				since {{ consumer.created|timesince }}
			</p>
		</div>
		{% endfor %}
	</div>

{%endblock%}