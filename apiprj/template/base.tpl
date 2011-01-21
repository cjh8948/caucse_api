{% extends "base_zero.tpl" %}

{% block title %}
	동네API
{% endblock %}

{% block branding %}
<h1 id="site-name">동네API</h1>
{% endblock %}

{% block userlinks %} 
    {% if user.is_active and user.is_staff %}
    	<a target='_blank' href='/admin'>관리</a> /
    {% endif %}
    <a href='/apistatus'>시스템 상태</a> /
    <a href='/apireference'>API 레퍼런스</a> / 
    {% if user.is_authenticated %}
        <a href='/accounts/profile'>내 애플리케이션 관리</a> /
        {% if oauth_token %}
        	<a href='/accounts/logout?next=/oauth/authorize?oauth_token={{oauth_token}}'>로그아웃</a>
        {% else %}
        	<a href='/accounts/logout_then_login'>로그아웃</a>
        {% endif %}
	{% else %}
        <a href='/accounts/login'>로그인</a>
    {% endif %}
{% endblock %}                        
                        
{% block footer %} 
<div id="footer">
<p>문의: 이덕준 (<a href='mailto:gochist@gmail.com'>gochist@gmail.com</a>)</p>
</div>
{% endblock %}