<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="{{ LANGUAGE_CODE|default:"en-us" }}" xml:lang="{{ LANGUAGE_CODE|default:"en-us" }}" {% if LANGUAGE_BIDI %}dir="rtl"{% endif %}>
<head>
<title>{% block title %}{% endblock %}</title>
<link rel="stylesheet" type="text/css" href="{% block stylesheet %}{% load adminmedia %}{% admin_media_prefix %}css/base.css{% endblock %}" />
{% block extrastyle %}{% endblock %}
<!--[if lte IE 7]><link rel="stylesheet" type="text/css" href="{% block stylesheet_ie %}{% load adminmedia %}{% admin_media_prefix %}css/ie.css{% endblock %}" /><![endif]-->
{% if LANGUAGE_BIDI %}<link rel="stylesheet" type="text/css" href="{% block stylesheet_rtl %}{% admin_media_prefix %}css/rtl.css{% endblock %}" />{% endif %}
<script type="text/javascript">window.__admin_media_prefix__ = "{% filter escapejs %}{% admin_media_prefix %}{% endfilter %}";</script>
{% block extrahead %}{% endblock %}
{% block blockbots %}<meta name="robots" content="NONE,NOARCHIVE" />{% endblock %}
</head>
{% load i18n %}

<body class="{% if is_popup %}popup {% endif %}{% block bodyclass %}{% endblock %}">

<!-- Container -->
<div id="container">

    {% if not is_popup %}
    <!-- Header -->
    <div id="header">
        <div id="branding">
        {% block branding %}{% endblock %}
        </div>
        <div id="user-tools">
            {% trans 'Welcome' %}
            <strong>{% filter force_escape %}{% firstof user.first_name user.username %}{% endfilter %}</strong>.
            {% block userlinks %}
                {% url django-admindocs-docroot as docsroot %}
                {% if docsroot %}
                    <a href="{{ docsroot }}">{% trans 'Documentation' %}</a> /
                {% endif %}
                {% url admin:password_change as password_change_url %}
                {% if password_change_url %}
                    <a href="{{ password_change_url }}">
                {% else %}
                    <a href="{{ root_path }}password_change/">
                {% endif %}
                {% trans 'Change password' %}</a> /
                {% url admin:logout as logout_url %}
                {% if logout_url %}
                    <a href="{{ logout_url }}">
                {% else %}
                    <a href="{{ root_path }}logout/">
                {% endif %}
                {% trans 'Log out' %}</a>
            {% endblock %}
        </div>
        {% block nav-global %}{% endblock %}
    </div>
    <!-- END Header -->
    {% block breadcrumbs %}<div class="breadcrumbs"><a href="/">{% trans 'Home' %}</a>{% if title %} &rsaquo; {{ title }}{% endif %}</div>{% endblock %}
    {% endif %}

        {% if messages %}
        <ul class="messagelist">{% for message in messages %}
          <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
	{% endfor %}</ul>
        {% endif %}

    <!-- Content -->
    <div id="content" class="{% block coltype %}colM{% endblock %}">
        {% block pretitle %}{% endblock %}
        {% block content_title %}{% if title %}<h1>{{ title }}</h1>{% endif %}{% endblock %}
        {% block content %}
        {% block object-tools %}{% endblock %}
        {{ content }}
        {% endblock %}
        {% block sidebar %}{% endblock %}
        <br class="clear" />
    </div>
    <!-- END Content -->

    {% block footer %}<div id="footer"></div>{% endblock %}
</div>
<!-- END Container -->

</body>
</html>