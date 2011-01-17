{%extends "base_zero.tpl"%}

{% block title %}
	동네API
{% endblock %}

{% block navibar %} 
    <li class='nav'>
        <a href='/apistatus'>시스템 상태</a>
    </li>
    <li class='nav'>
        <a href='/apireference'>API 레퍼런스</a>
    </li>
    {% if user.is_authenticated %}
        <li class='nav'>
            <a href='/accounts/profile'>내 애플리케이션</a>
        </li>
        <li class='nav'>
            {% if oauth_token %}
            	<a href='/accounts/logout?next=/oauth/authorize?oauth_token={{oauth_token}}'>logout</a>
            {% else %}
            	<a href='/accounts/logout_then_login'>로그아웃</a>
            {% endif %}
        </li>
    {% else %}
        <li class='nav'>
            <a href='/accounts/login'>로그인</a>
        </li>
    {% endif %}
{% endblock %}                        
                        
{% block footer %} 
<p>문의: 이덕준 (<a href='mailto:gochist@gmail.com'>gochist@gmail.com</a>)</p>
{% endblock %}