{% extends "base.tpl" %}
{% load i18n %}
{% block breadcrumbs %}
	<div class="breadcrumbs">
		<a href="../">홈</a> &rsaquo; 
		API 레퍼런스
	</div>
{% endblock %}

{% block title %}동네API - API 레퍼런스{% endblock %}

{% block content %}

<h1>API 레퍼런스</h1>
<p>
</p>
<div id="content-main">

{% for group, views in view_dict.items %}
<div class="module">
<h2>{{ group }}</h2>
{% for view in views|dictsort:"url" %}
<h3><a href="{{ view.module }}.{{ view.name }}/">{{ view.url }}</a></h3>
<p>{{ view.title }}</p>
<hr />
{% endfor %}
</div>
{% endfor %}
</div>
{% endblock %}

