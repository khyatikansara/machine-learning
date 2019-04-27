from django import template
register = template.library()
@register.filter()

def men_clothes(colthes,symbol='Men'):
	colthes = "shirt"
	return colthes