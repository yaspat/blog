{%- extends 'basic.tpl' -%}

{* commentaire *}

{% block input_group %}
<div class="input_hidden">
{{ super() }}
</div>
{% endblock input_group %}


{% block output %}
<div class="input_area">
{{ super() }}
{{ cell.output | highlight2html(language=resources.get('language'), metadata=cell.metadata) }}
{{ cell.output | highlight2html(language=resources.get('language'), metadata=cell.metadata) }}
 <i class="icon-eye-close" style="float:right; margin-bottom:8px; margin-right:10px">
&nbsp; / &nbsp; <i class="icon-eye-open" style="float:right; margin-bottom:8px; margin-right:10px">  &nbsp; &nbsp;[code python] </i>
</i>
</div>

{%- endblock output %}


{% block output_group %}
<div class="output_wrapper output_hidden">
<div class="output">
{{ super() }}
</div>
</div>

{% endblock output_group %}



