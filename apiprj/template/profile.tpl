{%extends "base.tpl"%}

{% block title %}
	동네API - 상태
{% endblock %}

{% block content %}
	<h1>내 애플리케이션</h1>
	<div class='side_by_side_left'>
		<h2>내 계정으로 접근을 허용한 애플리케이션</h2>
		{% for token in tokens %}
		<div class='app'>
			<h3>{{ token.consumer.name|escape }} by {{ token.consumer.user_id }}</h3>
			<p>
				 {{ token.consumer.description|escape }} -
				 since {{ token.created|timesince }}
			</p>
		
			{% if user.username == token.consumer.user_id %}
				<p>
					본인이 개발 중인 애플리케이션에 한해 개발의 편의를 위해 
					Access Token을 본 페이지에서 조회할 수 있도록 하였습니다.
					<strong>
						절대로 Access Token을 남에게 알려주지 마세요.
					</strong><br/>
					Access Token: ({{ token.key }}, {{ token.secret }})
				</p>
			{% endif %}
		</div>
		{% endfor %}
	</div>

	<div class='side_by_side_right'>
		<h2>내가 개발하는 애플리케이션</h2>
		{% for consumer in consumers %}
		<div class='app'>
			<h3>{{ consumer.name|escape }}</h3>
			<p>
				{{ consumer.description|escape }} -
				since {{ consumer.created|timesince }}
			</p>
			<p>
		        consumer key, secret pair: ({{ consumer.key|escape }}, {{ consumer.secret|escape }})
			</p>
		</div>
		{% endfor %}
	</div>

{%endblock%}