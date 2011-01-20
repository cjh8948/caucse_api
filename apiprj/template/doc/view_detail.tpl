{% extends "base.tpl" %}

{% load i18n %}

{% block breadcrumbs %}
	<div class="breadcrumbs">
		<a href="../../">홈</a> &rsaquo; 
		<a href="../">API 레퍼런스</a> &rsaquo; {{ name }}
	</div>
{% endblock %}


{% block title %}동네 API - {{ name }}{% endblock %}

{% block content %}

<!--h1>{{ name }}</h1-->

<h2 class="subhead">{{ summary }}</h2>

<p>{{ body }}</p>

{% if meta.Context %}
<h3>Context:</h3>
<p>{{ meta.Context }}</p>
{% endif %}

{% if meta.Templates %}
<h3>Templates:</h3>
<p>{{ meta.Templates }}</p>
{% endif %}

<p class="small">
	<a href="/apireference">&lsaquo; API 레퍼런스로 돌아가기</a>
</p>
{% endblock %}